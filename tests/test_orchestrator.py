"""
test_orchestrator.py — Unit Tests for StateMachine / CompiledGraph
==================================================================
Tests deterministic traversal, conditional edges, state merging,
stream semantics, trace validation, and error handling.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest

from scripts.agentic_soc.orchestrator import StateMachine, CompiledGraph, START, END


class TestStateMachineBasics(unittest.TestCase):
    """Core graph construction and compilation."""

    def test_add_node_and_compile(self):
        sm = StateMachine()
        sm.add_node("a", lambda s: {"x": 1})
        sm.add_edge(START, "a")
        sm.add_edge("a", END)
        cg = sm.compile()
        self.assertIsInstance(cg, CompiledGraph)
        self.assertEqual(cg._entry_point, "a")

    def test_get_topology(self):
        sm = StateMachine()
        sm.add_node("a", lambda s: {})
        sm.add_node("b", lambda s: {})
        sm.add_edge(START, "a")
        sm.add_edge("a", "b")
        topo = sm.get_topology()
        self.assertEqual(sorted(topo["nodes"]), ["a", "b"])
        self.assertEqual(topo["edges"], {"a": "b"})
        self.assertEqual(topo["entry_point"], "a")

    def test_compile_without_nodes_raises(self):
        sm = StateMachine()
        with self.assertRaises(ValueError) as ctx:
            sm.compile()
        self.assertIn("não possui nós", str(ctx.exception))

    def test_compile_without_entry_point_raises(self):
        sm = StateMachine()
        sm.add_node("a", lambda s: {})
        with self.assertRaises(ValueError) as ctx:
            sm.compile()
        self.assertIn("ponto de entrada", str(ctx.exception))

    def test_compile_missing_target_raises(self):
        sm = StateMachine()
        sm.add_node("a", lambda s: {})
        sm.add_edge(START, "a")
        sm.add_edge("a", "z")
        with self.assertRaises(ValueError) as ctx:
            sm.compile()
        self.assertIn("'z' não existe", str(ctx.exception))

    def test_reserved_node_names_raise(self):
        sm = StateMachine()
        with self.assertRaises(ValueError):
            sm.add_node(START, lambda s: {})
        with self.assertRaises(ValueError):
            sm.add_node(END, lambda s: {})


class TestCompiledGraphInvoke(unittest.TestCase):
    """Deterministic execution via .invoke()"""

    def test_linear_graph(self):
        sm = StateMachine()
        sm.add_node("a", lambda s: {"v": s.get("v", []) + ["a"]})
        sm.add_node("b", lambda s: {"v": s.get("v", []) + ["b"]})
        sm.add_edge(START, "a")
        sm.add_edge("a", "b")
        sm.add_edge("b", END)

        cg = sm.compile()
        result = cg.invoke({})
        self.assertEqual(result["v"], ["a", "b"])
        self.assertEqual(len(cg.trace), 2)
        self.assertEqual(cg.trace[0]["node"], "a")
        self.assertEqual(cg.trace[1]["node"], "b")

    def test_conditional_router(self):
        sm = StateMachine()
        sm.add_node("start", lambda s: {"count": s.get("count", 0) + 1})
        sm.add_node("inc", lambda s: {"count": s.get("count", 0) + 1})
        sm.add_node("done", lambda s: {"flag": True})
        sm.add_edge(START, "start")
        sm.add_conditional_edges("start", lambda s: "done" if s.get("count", 0) >= 2 else "inc")
        sm.add_conditional_edges("inc", lambda s: "done" if s.get("count", 0) >= 3 else "inc")
        sm.add_edge("done", END)

        cg = sm.compile()
        result = cg.invoke({"count": 0})
        self.assertEqual(result["count"], 3)
        self.assertTrue(result["flag"])
        nodes_hit = [t["node"] for t in cg.trace]
        self.assertEqual(nodes_hit, ["start", "inc", "inc", "done"])

    def test_state_merging_preserves_keys(self):
        sm = StateMachine()
        sm.add_node("a", lambda s: {"new": 42})
        sm.add_node("b", lambda s: {"extra": "x"})
        sm.add_edge(START, "a")
        sm.add_edge("a", "b")
        sm.add_edge("b", END)

        cg = sm.compile()
        result = cg.invoke({"existing": 99})
        self.assertEqual(result["existing"], 99)
        self.assertEqual(result["new"], 42)
        self.assertEqual(result["extra"], "x")

    def test_max_steps_prevents_infinite_loop(self):
        sm = StateMachine()
        sm.add_node("loop", lambda s: {"i": s.get("i", 0) + 1})
        sm.add_edge(START, "loop")
        sm.add_edge("loop", "loop")  # infinite

        cg = sm.compile()
        result = cg.invoke({"i": 0}, max_steps=5)
        self.assertEqual(result["i"], 5)
        self.assertEqual(len(cg.trace), 5)

    def test_node_returning_none(self):
        sm = StateMachine()
        sm.add_node("a", lambda s: None)
        sm.add_node("b", lambda s: {"ok": True})
        sm.add_edge(START, "a")
        sm.add_edge("a", "b")
        sm.add_edge("b", END)

        cg = sm.compile()
        result = cg.invoke({})
        self.assertTrue(result["ok"])
        self.assertEqual(cg.trace[0]["patch_keys"], [])

    def test_missing_node_at_runtime_raises(self):
        sm = StateMachine()
        sm.add_node("a", lambda s: {})
        sm.add_conditional_edges("a", lambda s: "nonexistent")
        sm.add_edge(START, "a")

        cg = sm.compile()
        with self.assertRaises(RuntimeError) as ctx:
            cg.invoke({})
        self.assertIn("'nonexistent' não encontrado", str(ctx.exception))


class TestCompiledGraphStream(unittest.TestCase):
    """Incremental execution via .stream()"""

    def test_stream_yields_each_step(self):
        sm = StateMachine()
        sm.add_node("a", lambda s: {"v": s.get("v", []) + ["a"]})
        sm.add_node("b", lambda s: {"v": s.get("v", []) + ["b"]})
        sm.add_edge(START, "a")
        sm.add_edge("a", "b")
        sm.add_edge("b", END)

        cg = sm.compile()
        steps = list(cg.stream({}))
        self.assertEqual(len(steps), 2)
        self.assertEqual(steps[0][0], "a")
        self.assertEqual(steps[0][1]["v"], ["a"])
        self.assertEqual(steps[1][0], "b")
        self.assertEqual(steps[1][1]["v"], ["a", "b"])

    def test_stream_trace_matches(self):
        sm = StateMachine()
        sm.add_node("a", lambda s: {"x": 1})
        sm.add_edge(START, "a")
        sm.add_edge("a", END)

        cg = sm.compile()
        list(cg.stream({}))
        self.assertEqual(len(cg.trace), 1)
        self.assertEqual(cg.trace[0]["node"], "a")
        self.assertIn("elapsed_ms", cg.trace[0])

    def test_stream_isolated_state_snapshots(self):
        sm = StateMachine()
        sm.add_node("a", lambda s: {"x": 1})
        sm.add_node("b", lambda s: {"y": 2})
        sm.add_edge(START, "a")
        sm.add_edge("a", "b")
        sm.add_edge("b", END)

        cg = sm.compile()
        snapshots = [dict(s) for _, s in cg.stream({})]
        # snapshot after 'a' should not contain 'y' yet
        self.assertNotIn("y", snapshots[0])
        self.assertIn("x", snapshots[0])
        self.assertIn("y", snapshots[1])


class TestAgenticGraphSimulation(unittest.TestCase):
    """Higher-level simulation matching the 7-node agentic topology."""

    def test_supervisor_to_blocker_path(self):
        sm = StateMachine()
        sm.add_node("supervisor", lambda s: {"phase": "BLOCKING"})
        sm.add_node("blocker", lambda s: {"resolved": True})
        sm.add_edge(START, "supervisor")
        sm.add_conditional_edges("supervisor", lambda s: "blocker" if s.get("phase") == "BLOCKING" else END)
        sm.add_edge("blocker", END)

        cg = sm.compile()
        result = cg.invoke({})
        self.assertTrue(result["resolved"])
        self.assertEqual([t["node"] for t in cg.trace], ["supervisor", "blocker"])

    def test_supervisor_dlp_intel_fleet_reporter_path(self):
        sm = StateMachine()
        sm.add_node("supervisor", lambda s: {"phase": "MONITORING"})
        sm.add_node("dlp_edge", lambda s: {"phase": "ESCALATING", "threat_score": 0.98})
        sm.add_node("intel_cloud", lambda s: {"phase": "VACCINATING", "mitre": "T0831"})
        sm.add_node("fleet_vaccinator", lambda s: {"phase": "REPORTING", "coverage": 92.8})
        sm.add_node("clevel_reporter", lambda s: {"phase": "RESOLVED", "roi": 1200})

        sm.add_edge(START, "supervisor")
        sm.add_conditional_edges("supervisor", lambda s: "dlp_edge")
        sm.add_conditional_edges("dlp_edge", lambda s: "intel_cloud" if s.get("phase") == "ESCALATING" else END)
        sm.add_edge("intel_cloud", "fleet_vaccinator")
        sm.add_conditional_edges("fleet_vaccinator", lambda s: "clevel_reporter")
        sm.add_edge("clevel_reporter", END)

        cg = sm.compile()
        result = cg.invoke({})
        self.assertEqual(result["phase"], "RESOLVED")
        self.assertEqual(result["mitre"], "T0831")
        self.assertAlmostEqual(result["coverage"], 92.8)
        self.assertEqual(result["roi"], 1200)

    def test_vendor_cascade_to_fleet_reporter_path(self):
        sm = StateMachine()
        sm.add_node("supervisor", lambda s: {"phase": "TRIAGING"})
        sm.add_node("vendor_cascade", lambda s: {"phase": "VACCINATING", "vendor_suspended": True})
        sm.add_node("fleet_vaccinator", lambda s: {"phase": "REPORTING"})
        sm.add_node("clevel_reporter", lambda s: {"phase": "RESOLVED"})

        sm.add_edge(START, "supervisor")
        sm.add_conditional_edges("supervisor", lambda s: "vendor_cascade" if s.get("phase") == "TRIAGING" else END)
        sm.add_edge("vendor_cascade", "fleet_vaccinator")
        sm.add_conditional_edges("fleet_vaccinator", lambda s: "clevel_reporter")
        sm.add_edge("clevel_reporter", END)

        cg = sm.compile()
        result = cg.invoke({})
        self.assertTrue(result["vendor_suspended"])
        self.assertEqual(result["phase"], "RESOLVED")
        self.assertEqual([t["node"] for t in cg.trace],
                         ["supervisor", "vendor_cascade", "fleet_vaccinator", "clevel_reporter"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
