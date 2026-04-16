"""
PetroShield Demo TUI v2.5 — Textual-based Interactive Dashboard
================================================================
3 tabs:
  1. Dashboard   — Live metrics, torch animation, agentic loop, event stream,
                   Triple Surface Attack Vector cards, compliance heartbeat
  2. Operations  — Agentic Playbooks table, interactive workflow runner,
                   state inspector, daily routines execution
  3. Analytics   — ASCII data viz, KPIs/OKRs, financial charts, fleet health,
                   Triple Surface breakdown, vendor value-at-risk

Usage:
  cd <project_root>
  python -m scripts.dlp_proxy.demo_ui

Dependencies:
  textual>=0.70
"""

import json
import time
import sys
import os
from typing import List, Dict, Any

# Ensure project root is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, Grid
from textual.widgets import (
    Header, Footer, Static, Button, DataTable, RichLog,
    TabbedContent, TabPane, ProgressBar, Label, Rule,
)
from textual.reactive import reactive
from textual._work_decorator import work
from textual.message import Message
from textual.color import Color

from rich import box
from rich.text import Text
from rich.panel import Panel
from rich.table import Table as RichTable
from rich.json import JSON

# PetroShield imports
from scripts.agentic_soc.theatre import TheatreEngine
from scripts.agentic_soc.mock_data import (
    XR_DEVICES, VENDOR_RISK_DB, FLEET_REGISTRY,
    MONTHLY_METRICS, OKRS, generate_historical_audit_entries,
    get_cumulative_cost_avoided, get_vendor_risk_distribution, get_fleet_health,
    AGENTIC_WORKFLOWS, COMPLIANCE_LEDGER_ENTRIES, INCIDENT_KB,
    TRIPLE_SURFACE_METRICS, get_compliance_summary,
    get_vendor_contract_value_at_risk, get_triple_surface_breakdown,
)

# ---------------------------------------------------------------------------
# PetroShield Palette
# ---------------------------------------------------------------------------
GREEN = "#00FF41"
ORANGE = "#FF6200"
CYAN = "#00FFFF"
AMBER = "#FF9500"
RED = "#FF3333"
BLACK = "#0A0A0A"
PURPLE = "#BF00FF"


# ---------------------------------------------------------------------------
# Helpers: ASCII Charts & Sparklines
# ---------------------------------------------------------------------------

def ascii_bar_chart(title: str, data: Dict[str, float], width: int = 40, unit: str = "") -> Text:
    """Build a simple horizontal ASCII bar chart as Rich Text."""
    lines = Text()
    max_val = max(data.values()) if data else 1
    lines.append(f"{title}\n", style=f"bold {CYAN}")
    for label, value in data.items():
        bar_len = int((value / max_val) * width)
        bar = "█" * bar_len
        color = GREEN if value < max_val * 0.5 else (AMBER if value < max_val * 0.8 else ORANGE)
        lines.append(f"{label:22} ", style="dim")
        lines.append(f"{bar}", style=color)
        lines.append(f" {value:,.0f}{unit}\n", style="white")
    return lines


def ascii_sparkline(values: List[float], width: int = 50) -> Text:
    """Build an ASCII sparkline."""
    blocks = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
    if not values:
        return Text("No data")
    min_v, max_v = min(values), max(values)
    if max_v == min_v:
        return Text("█" * min(width, len(values)), style=GREEN)
    line = Text()
    for v in values[:width]:
        idx = int(((v - min_v) / (max_v - min_v)) * (len(blocks) - 1))
        line.append(blocks[idx], style=GREEN if v < (max_v * 0.6) else ORANGE)
    return line


def metric_card(title: str, value: str, delta: str = "", color: str = GREEN) -> Panel:
    """Rich Panel styled as a metric card."""
    text = Text()
    text.append(f"{value}\n", style=f"bold {color}")
    text.append(title, style="dim white")
    if delta:
        text.append(f"\n{delta}", style=f"dim {color}")
    return Panel(text, border_style=color, box=box.ROUNDED)


def mini_stat(label: str, value: str, color: str = CYAN) -> Text:
    t = Text()
    t.append(f"{value}", style=f"bold {color}")
    t.append(f" {label}", style="dim")
    return t


# ---------------------------------------------------------------------------
# Torch Animation Widget
# ---------------------------------------------------------------------------

TORCH_FRAMES = [
    "  🔥\n  |\n  |\n [|]",
    " 🔥🔥\n  |\n  |\n [|]",
    "🔥🔥🔥\n  |\n  |\n [|]",
    "🔥🔥🔥🔥\n  |\n  |\n [|]",
]


class Torch(Static):
    """Animated ASCII torch."""

    frame_index = reactive(0)

    def on_mount(self) -> None:
        self.set_interval(0.3, self.advance_frame)

    def advance_frame(self) -> None:
        self.frame_index = (self.frame_index + 1) % len(TORCH_FRAMES)
        self.update(Panel(
            Text(TORCH_FRAMES[self.frame_index], justify="center", style=ORANGE),
            title="[bold]PetroShield[/]",
            border_style=ORANGE,
            box=box.ROUNDED,
        ))


# ---------------------------------------------------------------------------
# Messages for cross-thread updates
# ---------------------------------------------------------------------------

class NodeTransition(Message):
    """Posted when the Theatre engine transitions between graph nodes."""
    def __init__(self, node_name: str, state: dict) -> None:
        self.node_name = node_name
        self.state = state
        super().__init__()


class WorkflowComplete(Message):
    """Posted when a workflow run finishes execution."""
    def __init__(self, result: dict) -> None:
        self.result = result
        super().__init__()


# ---------------------------------------------------------------------------
# Tab 1: Dashboard Content
# ---------------------------------------------------------------------------

class DashboardContent(Container):
    """Central live dashboard with metrics, torch, loop, event stream, Triple Surface."""

    def compose(self) -> ComposeResult:
        # Top row: Torch + 6 metrics
        with Horizontal(id="dash-top"):
            yield Torch(id="dash-torch")
            yield Static(id="metric-1")
            yield Static(id="metric-2")
            yield Static(id="metric-3")
            yield Static(id="metric-4")
            yield Static(id="metric-5")
            yield Static(id="metric-6")

        with Horizontal(id="dash-mid"):
            # Agentic Loop
            with Vertical(id="agentic-loop-panel"):
                yield Label("[b cyan]Agentic Loop[/b cyan]")
                yield Static(id="agentic-loop")

            # Triple Surface Attack Vector
            with Vertical(id="triple-surface-panel"):
                yield Label("[b orange]Triple Surface Attack Vector[/b orange]")
                yield Static(id="triple-surface")

        # Compliance heartbeat + vendor spotlight
        with Horizontal(id="dash-sub"):
            with Vertical(id="compliance-panel"):
                yield Label("[b green]Compliance Heartbeat[/b green]")
                yield Static(id="compliance-stats")
            with Vertical(id="vendor-spotlight-panel"):
                yield Label("[b red]Vendor Spotlight[/b red]")
                yield Static(id="vendor-spotlight")

        # Bottom: Live Event Stream
        with Vertical(id="event-stream-panel"):
            yield Label("[b green]Live Event Stream — Agentic Daily Routines[/b green]")
            yield RichLog(id="event-log", highlight=True, markup=True)

    def on_mount(self) -> None:
        self.update_metrics()
        self.update_agentic_loop()
        self.update_triple_surface()
        self.update_compliance()
        self.update_vendor_spotlight()
        self.start_event_stream()

    def update_metrics(self) -> None:
        latest = MONTHLY_METRICS[-1]
        cumulative_cost = get_cumulative_cost_avoided()
        fleet = get_fleet_health()
        compliance = get_compliance_summary()

        cards = [
            ("metric-1", "Active Sessions", str(len([d for d in XR_DEVICES.values() if d["mdm_enrollment_status"] != "compromised"])), "Zero Trust Auth", GREEN),
            ("metric-2", "Leaks Prevented (MoM)", str(latest["leaks_prevented"]), "+12% vs last month", GREEN),
            ("metric-3", "Biometric Re-Auths", str(latest["biometric_reauths"]), "Gaze liveness verified", CYAN),
            ("metric-4", "Shadow IT Blocks", str(latest["shadow_it_blocks"]), "Tunnels isolated", RED),
            ("metric-5", "Cost Avoided YTD", f"R$ {cumulative_cost/1_000_000:.2f}M", "ROI > 1200%", AMBER),
            ("metric-6", "Fleet Coverage", f"{fleet['coverage_pct']}%", f"{fleet['online']}/{fleet['total_nodes']} nodes online", GREEN),
        ]
        for widget_id, title, value, delta, color in cards:
            self.query_one(f"#{widget_id}", Static).update(metric_card(title, value, delta, color))

    def update_agentic_loop(self) -> None:
        phases = ["MONITOR", "DETECT", "ANALYSE", "RESPOND", "HUNT", "LESSONS"]
        lines = Text()
        for phase in phases:
            lines.append("✓ ", style=GREEN)
            lines.append(f"{phase}  ", style=CYAN)
        self.query_one("#agentic-loop", Static).update(Panel(lines, border_style=CYAN, box=box.ROUNDED))

    def update_triple_surface(self) -> None:
        ts = TRIPLE_SURFACE_METRICS
        text = Text()
        text.append("Triple Surface Blocks (30d)\n", style=f"bold {ORANGE}")
        for key, data in ts.items():
            label = data["label"].split("(")[0].strip()
            count = data["blocks_30d"]
            alerts = data["active_alerts"]
            color = GREEN if alerts < 3 else (AMBER if alerts < 5 else RED)
            text.append(f"{label:28} ", style="dim")
            text.append(f"{count:3} blocks", style=color)
            text.append(f"  ({alerts} alert{'s' if alerts!=1 else ''})\n", style="dim")
        self.query_one("#triple-surface", Static).update(Panel(text, border_style=ORANGE, box=box.ROUNDED))

    def update_compliance(self) -> None:
        summary = get_compliance_summary()
        text = Text()
        text.append("ANPD / LGPD Status\n", style=f"bold {GREEN}")
        text.append(f"Total Items: {summary['total_entries']}\n", style="white")
        text.append(f"Pending:     {summary['pending_notifications']}\n", style=AMBER if summary['pending_notifications'] else GREEN)
        text.append(f"Overdue:     {summary['overdue']}\n", style=RED if summary['overdue'] else GREEN)
        text.append(f"Compliance:  {summary['compliance_rate_pct']}%\n", style=GREEN)
        self.query_one("#compliance-stats", Static).update(Panel(text, border_style=GREEN, box=box.ROUNDED))

    def update_vendor_spotlight(self) -> None:
        critical = [(vid, v) for vid, v in VENDOR_RISK_DB.items() if v["risk_level"] == "CRITICAL"]
        text = Text()
        text.append("Critical Vendors\n", style=f"bold {RED}")
        for vid, v in critical:
            text.append(f"{v['vendor_name']}\n", style=AMBER)
            text.append(f"  Score: {int(v['risk_score'])} | Contract: R$ {v['contract_value_brl']/1_000_000_000:.2f}B\n", style="dim")
        if not critical:
            text.append("No critical vendors right now.", style=GREEN)
        var = get_vendor_contract_value_at_risk()
        text.append(f"\nValue at Risk (HIGH+): R$ {var/1_000_000_000:.2f}B", style=RED)
        self.query_one("#vendor-spotlight", Static).update(Panel(text, border_style=RED, box=box.ROUNDED))

    def start_event_stream(self) -> None:
        log = self.query_one("#event-log", RichLog)
        log.write("[dim]Initializing PetroShield Event Stream...[/dim]")
        self._event_index = 0
        self._events = generate_historical_audit_entries(30)
        self.set_interval(1.0, self._push_next_event)

    def _push_next_event(self) -> None:
        log = self.query_one("#event-log", RichLog)
        if self._event_index < len(self._events):
            e = self._events[self._event_index]
            color = GREEN if e["operator_action"] == "allowed" else (AMBER if e["operator_action"] == "escalated" else RED)
            wf = AGENTIC_WORKFLOWS[self._event_index % len(AGENTIC_WORKFLOWS)]
            log.write(
                f"[{color}]{e['operator_action'].upper()}[/] | "
                f"[cyan]{wf['workflow_name'].split(' ')[0]} {wf['workflow_name'].split(' ')[1] if len(wf['workflow_name'].split(' ')) > 1 else ''}[/] | "
                f"{e['device_id']} | "
                f"score={e['threat_score']} | "
                f"lat={e['latency_ms']}ms"
            )
            self._event_index += 1
        else:
            self._event_index = 0


# ---------------------------------------------------------------------------
# Tab 2: Operations Content (Agentic Playbooks)
# ---------------------------------------------------------------------------

class OperationsContent(Container):
    """Interactive agentic workflow runner with playbook table and state inspector."""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.selected_workflow_id: str = AGENTIC_WORKFLOWS[0]["workflow_id"]
        self.engine = TheatreEngine(quiet=True)
        self._running_all: bool = False

    def compose(self) -> ComposeResult:
        with Horizontal(id="ops-layout"):
            # Left: playbook list
            with Vertical(id="playbook-list-panel"):
                yield Label("[b cyan]Agentic Playbooks — Daily SOC Routines[/b cyan]")
                yield DataTable(id="playbook-table", cursor_type="row")
                yield Button("▶ Run Selected Playbook", id="run-wf-btn", variant="primary")
                yield Button("▶▶ Run All Playbooks", id="run-all-wf-btn", variant="success")
                yield Static(id="playbook-desc")

            # Right: output
            with Vertical(id="ops-output-panel"):
                yield Label("[b green]Execution Trace & Narrative[/b green]")
                yield RichLog(id="ops-log", highlight=True, markup=True, max_lines=200)
                yield Label("[b cyan]Outcome Inspector[/b cyan]")
                yield Static(id="outcome-inspector")

    def on_mount(self) -> None:
        table = self.query_one("#playbook-table", DataTable)
        table.add_columns("Playbook", "Type", "Frequency", "MITRE", "Expected")
        for w in AGENTIC_WORKFLOWS:
            mitre = w.get("expected_mitre") or "—"
            table.add_row(
                w["workflow_name"],
                w["workflow_type"],
                w["daily_frequency"],
                mitre,
                w["expected_action"],
                key=w["workflow_id"],
            )
        table.cursor_coordinate = (0, 0)
        self.selected_workflow_id = AGENTIC_WORKFLOWS[0]["workflow_id"]
        self._update_desc()
        self.query_one("#outcome-inspector", Static).update(
            Panel("Select a playbook and press Run.", border_style=CYAN, box=box.ROUNDED)
        )

    def _update_desc(self) -> None:
        wf = next(w for w in AGENTIC_WORKFLOWS if w["workflow_id"] == self.selected_workflow_id)
        text = Text()
        text.append(f"{wf['workflow_name']}\n", style=f"bold {CYAN}")
        text.append(f"{wf['description']}\n\n", style="white")
        text.append("Business Value: ", style="dim")
        text.append(wf["business_value"], style=GREEN)
        self.query_one("#playbook-desc", Static).update(Panel(text, border_style=CYAN, box=box.ROUNDED))

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        self.selected_workflow_id = str(event.row_key.value)
        self._update_desc()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "run-wf-btn":
            self.run_workflow(self.selected_workflow_id)
        elif event.button.id == "run-all-wf-btn":
            self.run_all_workflows()

    def run_workflow(self, workflow_id: str) -> None:
        log = self.query_one("#ops-log", RichLog)
        log.clear()
        wf = next(w for w in AGENTIC_WORKFLOWS if w["workflow_id"] == workflow_id)
        log.write(f"[orange]Initiating {wf['workflow_name']}...[/orange]")
        self.query_one("#run-wf-btn", Button).disabled = True
        self.query_one("#run-all-wf-btn", Button).disabled = True
        self.run_workflow_worker(workflow_id)

    def run_all_workflows(self) -> None:
        log = self.query_one("#ops-log", RichLog)
        log.clear()
        log.write("[orange]Running full daily SOC routine suite...[/orange]")
        self.query_one("#run-wf-btn", Button).disabled = True
        self.query_one("#run-all-wf-btn", Button).disabled = True
        self._running_all = True
        self.run_all_worker()

    @work(exclusive=True, thread=True)
    def run_workflow_worker(self, workflow_id: str) -> None:
        def node_cb(node_name: str, state: dict):
            self.post_message(NodeTransition(node_name, dict(state)))
        # Map workflow_id to corresponding scene_id (they share IDs now)
        result = self.engine.run_scene(workflow_id, node_callback=node_cb)
        self.post_message(WorkflowComplete(result))

    @work(exclusive=True, thread=True)
    def run_all_worker(self) -> None:
        for w in AGENTIC_WORKFLOWS:
            self.post_message(NodeTransition("PLAYBOOK_START", {"workflow_id": w["workflow_id"], "title": w["workflow_name"]}))
            result = self.engine.run_scene(w["workflow_id"])
            self.post_message(WorkflowComplete(result))
        self.post_message(WorkflowComplete({"all_done": True}))

    def on_node_transition(self, event: NodeTransition) -> None:
        log = self.query_one("#ops-log", RichLog)
        if event.node_name == "PLAYBOOK_START":
            log.write(f"\n[b cyan]══ {event.state.get('workflow_id')} ══[/b cyan] {event.state.get('title', '')}")
        else:
            log.write(f"  [dim]→[/dim] [cyan]{event.node_name}[/cyan]")

    def on_workflow_complete(self, event: WorkflowComplete) -> None:
        log = self.query_one("#ops-log", RichLog)
        if event.result.get("all_done"):
            log.write("\n[green bold]All playbooks completed.[/green bold]")
            self._running_all = False
            self.query_one("#run-wf-btn", Button).disabled = False
            self.query_one("#run-all-wf-btn", Button).disabled = False
            return

        final = event.result.get("final_state", {})
        scene_id = event.result.get("scene_id", "N/A")
        wf = next((w for w in AGENTIC_WORKFLOWS if w["workflow_id"] == scene_id), None)

        log.write(
            f"\n[green]Outcome:[/green] action=[b]{final.get('dlp_action', 'N/A')}[/b] | "
            f"threat=[b]{final.get('dlp_threat_score', 0)}[/b] | "
            f"entities=[b]{len(final.get('dlp_entities', []))}[/b]"
        )

        # Update inspector
        inspector = self.query_one("#outcome-inspector", Static)
        financial = final.get("financial", {})
        summary_text = Text()
        if wf:
            summary_text.append(f"Playbook: {wf['workflow_name']}\n", style=f"bold {CYAN}")
            summary_text.append(f"Type: {wf['workflow_type']} | Freq: {wf['daily_frequency']}\n", style="dim")
        summary_text.append(f"Action: {final.get('dlp_action', 'N/A')}\n", style="white")
        summary_text.append(f"Threat Score: {final.get('dlp_threat_score', 0)}\n", style="white")
        summary_text.append(f"Redactions: {len(final.get('dlp_entities', []))}\n", style="white")
        if financial:
            summary_text.append(f"Downtime Avoided: {financial.get('downtime_hours_avoided', 0)}h\n", style=GREEN)
            summary_text.append(f"Cost Avoided: R$ {financial.get('downtime_cost_avoided_brl', 0):,.2f}\n", style=AMBER)
            summary_text.append(f"ROI: {financial.get('roi_percentage', 0)}%\n", style=GREEN)
        inspector.update(Panel(summary_text, border_style=CYAN, box=box.ROUNDED))

        if not self._running_all:
            self.query_one("#run-wf-btn", Button).disabled = False
            self.query_one("#run-all-wf-btn", Button).disabled = False


# ---------------------------------------------------------------------------
# Tab 3: Analytics Content
# ---------------------------------------------------------------------------

class AnalyticsContent(Container):
    """ASCII data visualization, OKRs, and financial reports."""

    def compose(self) -> ComposeResult:
        with Horizontal(id="analytics-top"):
            # Financial Impact by Playbook
            yield Static(id="fin-chart")
            # Monthly trend sparkline
            yield Static(id="trend-chart")

        with Horizontal(id="analytics-mid"):
            # OKR Progress Bars
            with Vertical(id="okr-panel"):
                yield Label("[b cyan]OKRs & KPIs[/b cyan]")
                for i in range(1, 6):
                    yield Label(id=f"okr-label-{i}")
                    yield ProgressBar(total=100, id=f"okr-bar-{i}", show_eta=False, show_percentage=True)

            # Triple Surface + Vendor Dist
            with Vertical(id="surface-vendor-panel"):
                yield Static(id="surface-chart")
                yield Static(id="vendor-dist-chart")

        with Horizontal(id="analytics-bottom"):
            # Fleet Health
            yield Static(id="fleet-health")
            # Incident KB financial impact
            yield Static(id="incident-kb-chart")

    def on_mount(self) -> None:
        self._update_financial_chart()
        self._update_trend_chart()
        self._update_okrs()
        self._update_surface_chart()
        self._update_vendor_dist()
        self._update_fleet_health()
        self._update_incident_kb_chart()

    def _update_financial_chart(self) -> None:
        chart_data = {
            "Zero Trust Auth": 120_000,
            "DLP Guardian": 350_000,
            "OT Sentinel": 580_000,
            "Vendor Cascade": 420_000,
            "LGPD Engine": 890_000,
            "Phishing Block": 210_000,
            "Geofence Guard": 95_000,
            "Firmware Watch": 310_000,
            "Shadow IT Patrol": 180_000,
            "Biometric Auth": 140_000,
        }
        self.query_one("#fin-chart", Static).update(
            Panel(ascii_bar_chart("Financial Impact by Playbook (R$)", chart_data, width=30, unit=""), border_style=AMBER, box=box.ROUNDED)
        )

    def _update_trend_chart(self) -> None:
        costs = [m["cost_avoided_brl"] / 1_000_000 for m in MONTHLY_METRICS]
        line = ascii_sparkline(costs, width=50)
        text = Text()
        text.append("Cost Avoided Trend (R$ millions)\n", style=f"bold {CYAN}")
        text.append(line)
        text.append(f"\nMin: {min(costs):.1f}M | Max: {max(costs):.1f}M | Avg: {sum(costs)/len(costs):.1f}M", style="dim")
        self.query_one("#trend-chart", Static).update(Panel(text, border_style=CYAN, box=box.ROUNDED))

    def _update_okrs(self) -> None:
        okr_items = list(OKRS.values())[:5]
        for i, okr in enumerate(okr_items, start=1):
            lbl = self.query_one(f"#okr-label-{i}", Label)
            bar = self.query_one(f"#okr-bar-{i}", ProgressBar)
            status_emoji = "✓" if okr["status"] == "on_track" else "⚠"
            lbl.update(f"{status_emoji} [b]{okr['name']}[/b] — Target: {okr['target']} | Current: {okr['current']}")
            bar.progress = okr["progress_pct"]

    def _update_surface_chart(self) -> None:
        breakdown = get_triple_surface_breakdown()
        self.query_one("#surface-chart", Static).update(
            Panel(ascii_bar_chart("Triple Surface Blocks (30d)", breakdown, width=25), border_style=PURPLE, box=box.ROUNDED)
        )

    def _update_vendor_dist(self) -> None:
        dist = get_vendor_risk_distribution()
        self.query_one("#vendor-dist-chart", Static).update(
            Panel(ascii_bar_chart("Vendor Risk Distribution", dist, width=25), border_style=ORANGE, box=box.ROUNDED)
        )

    def _update_fleet_health(self) -> None:
        health = get_fleet_health()
        text = Text()
        text.append("Fleet Health\n", style=f"bold {GREEN}")
        text.append(f"Total Nodes: {health['total_nodes']}\n", style="white")
        text.append(f"Online:      {health['online']} ({health['coverage_pct']}%)\n", style=GREEN)
        text.append(f"Offline:     {health['offline']}\n", style=RED)
        text.append(f"Up-to-Date:  {health['up_to_date']}\n", style=GREEN)
        text.append(f"Outdated:    {health['outdated']}\n", style=AMBER)
        self.query_one("#fleet-health", Static).update(Panel(text, border_style=GREEN, box=box.ROUNDED))

    def _update_incident_kb_chart(self) -> None:
        data = {inc["title"][:22]: inc["financial_impact_brl"] for inc in INCIDENT_KB}
        self.query_one("#incident-kb-chart", Static).update(
            Panel(ascii_bar_chart("Incident KB — Impact (R$)", data, width=30), border_style=RED, box=box.ROUNDED)
        )


# ---------------------------------------------------------------------------
# Main App
# ---------------------------------------------------------------------------

class PetroShieldTUI(App):
    """Main Textual application."""

    CSS = """
    Screen { align: center middle; }

    .tab-container { padding: 1 2; }

    #dash-top { height: auto; }
    #dash-torch { width: 18; }
    Static { margin: 0 1; }

    #dash-mid { height: auto; margin-top: 1; }
    #agentic-loop-panel { width: 50%; }
    #triple-surface-panel { width: 50%; }

    #dash-sub { height: auto; margin-top: 1; }
    #compliance-panel { width: 50%; }
    #vendor-spotlight-panel { width: 50%; }

    #event-stream-panel { height: 1fr; margin-top: 1; }
    #event-log { height: 1fr; border: solid $primary; }

    #ops-layout { height: 100%; }
    #playbook-list-panel { width: 40%; }
    #ops-output-panel { width: 60%; }
    #ops-log { height: 2fr; border: solid $primary; }
    #outcome-inspector { height: 1fr; margin-top: 1; }
    #playbook-desc { height: auto; margin-top: 1; }

    #analytics-top { height: auto; }
    #analytics-mid { height: auto; margin-top: 1; }
    #okr-panel { width: 50%; }
    #surface-vendor-panel { width: 50%; }
    #analytics-bottom { height: 1fr; margin-top: 1; }
    #fleet-health { width: 50%; }
    #incident-kb-chart { width: 50%; }

    ProgressBar { height: 1; margin: 0 0 1 0; }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with TabbedContent(initial="tab-dashboard"):
            with TabPane("🔥 Dashboard", id="tab-dashboard"):
                yield DashboardContent()
            with TabPane("⚙️ Operations", id="tab-operations"):
                yield OperationsContent()
            with TabPane("📊 Analytics", id="tab-analytics"):
                yield AnalyticsContent()
        yield Footer()

    def on_mount(self) -> None:
        self.title = "PetroShield AxeGuard — SOC Agentic v2.5"
        self.sub_title = "Grand Prix SENAI Nacional 2026"


def main():
    app = PetroShieldTUI()
    app.run()


if __name__ == "__main__":
    main()
