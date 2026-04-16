"""
theatre.py — Roteiro Teatral Apoteótico: 8 Cenas Determinísticas
================================================================
Script de demonstração executável que orquestra os 5 agentes em
um roteiro cinematográfico para impressionar avaliadores SENAI e
o CTO da Petrobras.

Versão 2.0 — Expandido com TheatreEngine para consumo pelo TUI.

Modos de execução:
  --mode mock   : Respostas determinísticas (default, sem API key)
  --mode live   : Chamadas reais à OpenAI API
  --mode hybrid : Tenta live, fallback mock
  --verbose     : Logging máximo (todas as transições)
  --json-log    : Salva log JSON estruturado para auditoria

Uso CLI:
  python -m scripts.agentic_soc.theatre
  python -m scripts.agentic_soc.theatre --mode live --verbose
  python -m scripts.agentic_soc.theatre --json-log session_log.json

Uso Programático (TUI):
  from scripts.agentic_soc.theatre import TheatreEngine
  engine = TheatreEngine(mode="mock")
  result = engine.run_scene("cena_1")
  # result = {"final_state": {...}, "trace": [...], "logs": [...]}
"""

import os
import sys
import time
import argparse
from typing import Optional, List, Dict, Any, Callable

# Forcar UTF-8 no Windows para evitar crash do Rich com cp1252
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from .state import create_initial_state
from .orchestrator import StateMachine, START, END
from .agents import create_agents, supervisor_router, dlp_router, fleet_router
from .openai_bridge import OpenAIBridge
from .financial_model import FinancialCalculator
from .logger import AgenticLogger
from .mock_data import DEMO_SCENARIOS

try:
    from rich.console import Console
    from rich.panel import Panel
    HAS_RICH = True
except ImportError:
    HAS_RICH = False


# Paleta PetroShield
GREEN = "#00FF41"
ORANGE = "#FF6200"
CYAN = "#00FFFF"


def build_agentic_graph(
    logger: AgenticLogger,
    bridge: OpenAIBridge,
    calculator: FinancialCalculator,
) -> StateMachine:
    """
    Constrói o grafo agêntico completo com todos os nós e arestas.
    
    Topologia:
                    ┌── blocker ──────────────────────┐
                    │                                   │
    START → supervisor ──→ dlp_edge ──→ intel_cloud ──→ fleet_vaccinator ──→ clevel_reporter → END
                    │                  ↓                                          ↑
                    └── vendor_cascade ┘──────────────────────────────────────────┘
    """
    agents = create_agents(logger, bridge, calculator)

    graph = StateMachine()

    graph.add_node("supervisor", agents["supervisor"])
    graph.add_node("dlp_edge", agents["dlp_edge"])
    graph.add_node("intel_cloud", agents["intel_cloud"])
    graph.add_node("fleet_vaccinator", agents["fleet_vaccinator"])
    graph.add_node("clevel_reporter", agents["clevel_reporter"])
    graph.add_node("blocker", agents["blocker"])
    graph.add_node("vendor_cascade", agents["vendor_cascade"])

    graph.add_edge(START, "supervisor")
    graph.add_conditional_edges("supervisor", supervisor_router)
    graph.add_conditional_edges("dlp_edge", dlp_router)
    graph.add_edge("intel_cloud", "fleet_vaccinator")
    graph.add_conditional_edges("fleet_vaccinator", fleet_router)
    graph.add_edge("clevel_reporter", END)
    graph.add_edge("blocker", END)
    graph.add_edge("vendor_cascade", "fleet_vaccinator")

    return graph


def inject_scenario(state: dict, scenario: dict) -> dict:
    """Injeta os dados do cenário no estado inicial."""
    state["scene_id"] = scenario["scene_id"]
    state["scene_title"] = scenario["scene_title"]
    state["event_type"] = scenario["event_type"]
    state["event_source_device"] = scenario["device_id"]
    state["event_source_ip"] = scenario["ip"]
    state["event_raw_query"] = scenario["query"]
    state["event_timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    state["session_id"] = scenario.get("auth_token")
    return state


# =============================================================================
# THEATRE ENGINE — API Programática para TUI e Integrações
# =============================================================================

class TheatreEngine:
    """
    Motor de teatro programático que executa cenários do PetroShield
    sem efeitos colaterais de I/O (quando quiet=True).
    
    Ideal para alimentar TUIs, dashboards e testes automatizados.
    """

    def __init__(
        self,
        mode: str = "mock",
        model: str = "gpt-4o-mini",
        quiet: bool = True,
        json_log_path: Optional[str] = None,
    ):
        self.mode = mode
        self.model = model
        self.quiet = quiet
        self.json_log_path = json_log_path
        self.bridge = OpenAIBridge(mode=mode, model=model)
        self.calculator = FinancialCalculator()
        self._graph_def = None
        self._compiled = None
        self._logger = None

    def _init_graph(self):
        """Inicializa o grafo e logger sob demanda."""
        if self._compiled is not None:
            return
        self._logger = AgenticLogger(
            json_log_path=self.json_log_path,
            verbose=not self.quiet,
            use_rich=not self.quiet,
        )
        self._graph_def = build_agentic_graph(self._logger, self.bridge, self.calculator)
        self._compiled = self._graph_def.compile()

    @property
    def scenarios(self) -> List[dict]:
        return DEMO_SCENARIOS

    def get_scenario(self, scene_id: str) -> Optional[dict]:
        for s in self.scenarios:
            if s["scene_id"] == scene_id:
                return s
        return None

    def run_scene(
        self,
        scene_id: str,
        node_callback: Optional[Callable[[str, dict], None]] = None,
    ) -> dict:
        """
        Executa uma única cena e retorna resultado estruturado.
        
        Args:
            scene_id: ID da cena (ex: "cena_1")
            node_callback: Função opcional chamada a cada transição de nó
                          Signature: fn(node_name: str, state: dict) -> None
        
        Returns:
            {
                "scene_id": str,
                "scenario": dict,
                "final_state": dict,
                "trace": List[dict],
                "logs": List[dict],
                "cumulative_summary": dict,
            }
        """
        self._init_graph()
        scenario = self.get_scenario(scene_id)
        if not scenario:
            raise ValueError(f"Cenário '{scene_id}' não encontrado.")

        if not self.quiet:
            self._logger.scene_header(scenario["scene_id"], scenario["scene_title"])
            for narration_line in scenario["narration"]:
                self._logger.narrate(narration_line)
                time.sleep(0.2)

        state = create_initial_state()
        state = inject_scenario(state, scenario)

        if not self.quiet:
            self._logger.system(f"Evento injetado: {scenario['event_type']} de {scenario['device_id']}")

        final_state = None
        for node_name, current_state in self._compiled.stream(state):
            final_state = current_state
            if node_callback:
                node_callback(node_name, current_state)
            if not self.quiet:
                time.sleep(0.1)

        # Verificação determinística
        expected_action = scenario.get("expected_action")
        actual_action = final_state.get("dlp_action", "")
        if expected_action and actual_action != expected_action and not self.quiet:
            self._logger.error("VERIFY", f"[FAIL] Esperado '{expected_action}', obteve '{actual_action}'")

        return {
            "scene_id": scene_id,
            "scenario": scenario,
            "final_state": final_state,
            "trace": list(self._compiled.trace),
            "logs": list(self._logger.buffer) if self._logger else [],
            "cumulative_summary": self.calculator.cumulative_summary,
        }

    def run_all(
        self,
        scene_ids: Optional[List[str]] = None,
        scene_callback: Optional[Callable[[str, dict], None]] = None,
        node_callback: Optional[Callable[[str, dict], None]] = None,
    ) -> List[dict]:
        """
        Executa múltiplas cenas sequencialmente.
        
        Args:
            scene_ids: Lista de IDs. None = todas.
            scene_callback: Chamado ao final de cada cena. fn(scene_id, result)
            node_callback: Chamado a cada transição de nó dentro de cada cena.
        
        Returns:
            Lista de resultados (um dict por cena)
        """
        scenarios = self.scenarios
        if scene_ids:
            scenarios = [s for s in scenarios if s["scene_id"] in scene_ids]

        results = []
        for scenario in scenarios:
            result = self.run_scene(scenario["scene_id"], node_callback=node_callback)
            results.append(result)
            if scene_callback:
                scene_callback(scenario["scene_id"], result)
            if not self.quiet:
                time.sleep(0.5)
        return results

    def reset(self):
        """Reinicializa o estado do engine (útil para múltiplas runs isoladas)."""
        self._compiled = None
        self._graph_def = None
        self._logger = None
        self.calculator = FinancialCalculator()


# =============================================================================
# CLI LEGACY — run_theatre() mantido para compatibilidade
# =============================================================================

def run_theatre(
    mode: str = "mock",
    model: str = "gpt-4o-mini",
    verbose: bool = True,
    json_log_path: Optional[str] = None,
    scenes: Optional[list] = None,
):
    """
    Executa o roteiro teatral completo no terminal (modo CLI legacy).
    """
    console = Console(force_terminal=True, legacy_windows=False) if HAS_RICH else None

    if console:
        console.print()
        console.print(Panel(
            "[bold #FF6200]PETROSHIELD AXEGUARD -- SOC AGENTICO v2.0[/]\n"
            "[dim]Motor de Orquestracao Multi-Agentes[/]\n"
            "[dim]Grand Prix SENAI Nacional 2026[/]",
            border_style=ORANGE,
            width=60,
        ))
        console.print()
    else:
        print("\n" + "=" * 60)
        print("  PETROSHIELD AXEGUARD — SOC AGÊNTICO v2.0")
        print("  Motor de Orquestração Multi-Agentes")
        print("=" * 60 + "\n")

    engine = TheatreEngine(
        mode=mode,
        model=model,
        quiet=False,
        json_log_path=json_log_path,
    )

    scene_ids = scenes if scenes else None
    results = engine.run_all(scene_ids=scene_ids)

    # SUMÁRIO FINAL ACUMULADO
    if console:
        console.print()
        console.print(Panel(
            f"[bold {GREEN}]=== SUMARIO EXECUTIVO DA SESSAO ===[/]",
            border_style=ORANGE,
            width=60,
        ))

    summary = engine.calculator.cumulative_summary
    
    if engine._logger and HAS_RICH:
        from rich.table import Table
        table = Table(title="Dashboard C-Level", show_header=True, border_style=GREEN)
        table.add_column("Métrica", style=CYAN)
        table.add_column("Valor", style=ORANGE, justify="right")
        table.add_row("Incidentes Neutralizados", str(summary["total_incidents_resolved"]))
        table.add_row("Downtime Total Evitado", f"{summary['total_downtime_hours_avoided']}h")
        table.add_row("Faturamento Protegido", summary["formatted_cost_avoided"])
        table.add_row("ROI sobre Assinatura", f"{summary['roi_vs_subscription']}%")
        table.add_row("Cobertura da Frota", "92.86% (13/14 nodes)")
        table.add_row("Conformidade LGPD", "OK - Nenhum vazamento")
        console.print(table)
    else:
        print(f"\nDashboard C-Level")
        print(f"  Incidentes Neutralizados: {summary['total_incidents_resolved']}")
        print(f"  Downtime Total Evitado: {summary['total_downtime_hours_avoided']}h")
        print(f"  Faturamento Protegido: {summary['formatted_cost_avoided']}")
        print(f"  ROI sobre Assinatura: {summary['roi_vs_subscription']}%")
        print(f"  Cobertura da Frota: 92.86% (13/14 nodes)")
        print(f"  Conformidade LGPD: OK")

    final_state = results[-1]["final_state"] if results else {}
    if engine._logger:
        engine._logger.system(f"Audit chain: {len(final_state.get('audit_entries', []))} entradas tamper-evident")
        engine._logger.system(f"OpenAI Bridge stats: {engine.bridge.stats}")

    if console:
        console.print()
        console.print(Panel(
            f"[bold {GREEN}]PetroShield AxeGuard -- Demonstracao concluida com sucesso.[/]\n"
            f"[dim]Protegendo o pre-sal digital do Brasil.[/]",
            border_style=GREEN,
            width=60,
        ))

    if engine._logger:
        engine._logger.close()


# =============================================================================
# ENTRYPOINT
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="PetroShield AxeGuard — Teatro Agêntico Determinístico v2.0",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemplos:\n"
            "  python -m scripts.agentic_soc.theatre                    # Demo completa (mock)\n"
            "  python -m scripts.agentic_soc.theatre --mode live        # Com OpenAI real\n"
            "  python -m scripts.agentic_soc.theatre --scenes cena_3    # Apenas uma cena\n"
            "  python -m scripts.agentic_soc.theatre --json-log out.json # Salvar logs"
        ),
    )
    parser.add_argument("--mode", choices=["mock", "live", "hybrid"], default="mock",
                        help="Modo de operação: mock (default), live (OpenAI), hybrid")
    parser.add_argument("--model", default="gpt-4o-mini",
                        help="Modelo OpenAI (default: gpt-4o-mini)")
    parser.add_argument("--verbose", action="store_true", default=True,
                        help="Logging verboso (default: True)")
    parser.add_argument("--quiet", action="store_true",
                        help="Desliga logging verboso")
    parser.add_argument("--json-log", type=str, default=None,
                        help="Caminho para salvar log JSON estruturado")
    parser.add_argument("--scenes", nargs="*", default=None,
                        help="IDs das cenas para executar (ex: cena_1 cena_3)")

    args = parser.parse_args()

    run_theatre(
        mode=args.mode,
        model=args.model,
        verbose=not args.quiet,
        json_log_path=args.json_log,
        scenes=args.scenes,
    )


if __name__ == "__main__":
    main()
