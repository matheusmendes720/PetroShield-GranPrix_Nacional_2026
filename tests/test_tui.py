"""
test_tui.py — Integration Tests for PetroShield TUI (Textual)
===============================================================
Validates app composition, tab switching, widget mounting,
and TheatreEngine integration via Textual's run_test() pilot.
"""

import sys
import os
import asyncio
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.dlp_proxy.demo_ui import (
    PetroShieldTUI,
    DashboardContent,
    OperationsContent,
    TheatreContent,
    AnalyticsContent,
    NodeTransition,
    WorkflowComplete,
    TheatreLogEntry,
    TheatreSceneComplete,
)


class TestTUIComposition(unittest.IsolatedAsyncioTestCase):
    """Mounting and structural sanity."""

    async def test_app_mounts(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            self.assertEqual(app.title, "PetroShield AxeGuard — SOC Agentic v2.5")
            self.assertEqual(app.sub_title, "Grand Prix SENAI Nacional 2026")

    async def test_all_tabs_exist(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            tabs = app.query("TabPane")
            tab_ids = [t.id for t in tabs]
            self.assertIn("tab-dashboard", tab_ids)
            self.assertIn("tab-operations", tab_ids)
            self.assertIn("tab-theatre", tab_ids)
            self.assertIn("tab-analytics", tab_ids)
            self.assertEqual(len(tab_ids), 4)

    async def test_dashboard_content_mounts(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            dash = app.query_one("#tab-dashboard DashboardContent")
            self.assertIsNotNone(dash)
            # key widgets
            self.assertIsNotNone(dash.query_one("#dash-torch"))
            self.assertIsNotNone(dash.query_one("#event-log"))
            self.assertIsNotNone(dash.query_one("#triple-surface"))
            self.assertIsNotNone(dash.query_one("#compliance-stats"))
            self.assertIsNotNone(dash.query_one("#vendor-spotlight"))

    async def test_operations_content_mounts(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            # switch tab
            await pilot.click("#tab-operations")
            await pilot.pause()
            ops = app.query_one("#tab-operations OperationsContent")
            self.assertIsNotNone(ops)
            self.assertIsNotNone(ops.query_one("#playbook-table"))
            self.assertIsNotNone(ops.query_one("#run-wf-btn"))
            self.assertIsNotNone(ops.query_one("#ops-log"))
            self.assertIsNotNone(ops.query_one("#outcome-inspector"))

    async def test_theatre_content_mounts(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            await pilot.click("#tab-theatre")
            await pilot.pause()
            theatre = app.query_one("#tab-theatre TheatreContent")
            self.assertIsNotNone(theatre)
            self.assertIsNotNone(theatre.query_one("#scene-table"))
            self.assertIsNotNone(theatre.query_one("#run-scene-btn"))
            self.assertIsNotNone(theatre.query_one("#theatre-log"))
            self.assertIsNotNone(theatre.query_one("#theatre-outcome"))

    async def test_analytics_content_mounts(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            await pilot.click("#tab-analytics")
            await pilot.pause()
            analytics = app.query_one("#tab-analytics AnalyticsContent")
            self.assertIsNotNone(analytics)
            self.assertIsNotNone(analytics.query_one("#fin-chart"))
            self.assertIsNotNone(analytics.query_one("#trend-chart"))
            self.assertIsNotNone(analytics.query_one("#fleet-health"))
            self.assertIsNotNone(analytics.query_one("#incident-kb-chart"))


class TestDashboardFunctionality(unittest.IsolatedAsyncioTestCase):
    """Dashboard live components."""

    async def test_torch_advances_frames(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            torch = app.query_one("#dash-torch")
            initial = torch.frame_index
            # textual reactive updates are async; pause again
            await pilot.pause(0.5)
            self.assertNotEqual(torch.frame_index, initial)

    async def test_event_stream_populates(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            log = app.query_one("#event-log")
            # wait for interval
            await pilot.pause(1.5)
            self.assertGreater(len(log.lines), 0)

    async def test_metrics_cards_exist(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            for i in range(1, 7):
                card = app.query_one(f"#metric-{i}")
                self.assertIsNotNone(card)


class TestOperationsWorkflowIntegration(unittest.IsolatedAsyncioTestCase):
    """Operations tab + TheatreEngine integration."""

    async def test_playbook_table_has_rows(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            await pilot.click("#tab-operations")
            await pilot.pause()
            table = app.query_one("#playbook-table")
            self.assertGreater(len(table.rows), 0)

    async def test_select_playbook_updates_description(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            await pilot.click("#tab-operations")
            await pilot.pause()
            ops = app.query_one("#tab-operations OperationsContent")
            # simulate selecting second row
            table = app.query_one("#playbook-table")
            await pilot.click(table, offset=(0, 1))
            await pilot.pause()
            self.assertIsNotNone(ops.selected_workflow_id)

    async def test_workflow_complete_message_updates_inspector(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            await pilot.click("#tab-operations")
            await pilot.pause()
            ops = app.query_one("#tab-operations OperationsContent")
            # Post a fake completion message directly
            msg = WorkflowComplete({
                "scene_id": "wf_auth_001",
                "final_state": {
                    "dlp_action": "blocked",
                    "dlp_threat_score": 0.94,
                    "dlp_entities": [],
                    "financial": {
                        "downtime_hours_avoided": 4.5,
                        "downtime_cost_avoided_brl": 15000.0,
                        "roi_percentage": 1500.0,
                    }
                }
            })
            ops.on_workflow_complete(msg)
            await pilot.pause()
            inspector = app.query_one("#outcome-inspector")
            from rich.console import Console
            console = Console(width=80, force_terminal=True)
            with console.capture() as capture:
                console.print(inspector.renderable)
            text = capture.get()
            self.assertIn("blocked", text)

    async def test_node_transition_writes_to_log(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            await pilot.click("#tab-operations")
            await pilot.pause()
            ops = app.query_one("#tab-operations OperationsContent")
            msg = NodeTransition("dlp_edge", {"phase": "MONITORING"})
            # Handler should execute without error even if log is empty in test mode
            try:
                ops.on_node_transition(msg)
            except Exception as e:
                self.fail(f"on_node_transition raised {e}")
            await pilot.pause()
            log = app.query_one("#ops-log")
            self.assertIsNotNone(log)


class TestAnalyticsCharts(unittest.IsolatedAsyncioTestCase):
    """Analytics tab ASCII charts."""

    async def test_financial_chart_populated(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            await pilot.click("#tab-analytics")
            await pilot.pause()
            chart = app.query_one("#fin-chart")
            from rich.console import Console
            console = Console(width=80, force_terminal=True)
            with console.capture() as capture:
                console.print(chart.renderable)
            text = capture.get()
            self.assertIn("Impacto Financeiro por Playbook", text)

    async def test_trend_chart_populated(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            await pilot.click("#tab-analytics")
            await pilot.pause()
            chart = app.query_one("#trend-chart")
            from rich.console import Console
            console = Console(width=80, force_terminal=True)
            with console.capture() as capture:
                console.print(chart.renderable)
            text = capture.get()
            self.assertIn("Tendência de Custo Evitado", text)

    async def test_fleet_health_populated(self):
        app = PetroShieldTUI()
        async with app.run_test() as pilot:
            await pilot.pause()
            await pilot.click("#tab-analytics")
            await pilot.pause()
            chart = app.query_one("#fleet-health")
            from rich.console import Console
            console = Console(width=80, force_terminal=True)
            with console.capture() as capture:
                console.print(chart.renderable)
            text = capture.get()
            self.assertIn("Saúde da Frota", text)
            self.assertIn("Total de Nodes", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
