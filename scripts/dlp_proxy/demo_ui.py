"""
PetroShield Demo TUI — Animated terminal dashboard for live hackathon demo.
Requires: rich
"""

import time
import sys
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.table import Table

console = Console()

# Neon green + fire orange palette
GREEN = "#00FF41"
ORANGE = "#FF6200"
AMBER = "#FF9500"
CYAN = "#00FFFF"

TORCH_FRAMES = [
    """
       🔥
      /|
     / |
    /  |
   |   |
   |   |
   |___|
    """,
    """
      🔥🔥
      /|
     / |
    /  |
   |   |
   |   |
   |___|
    """,
    """
     🔥🔥🔥
      /|
     / |
    /  |
   |   |
   |   |
   |___|
    """,
    """
    🔥🔥🔥🔥
      /|
     / |
    /  |
   |   |
   |   |
   |___|
    """,
]

METRICS = {
    "active_sessions": 14,
    "leaks_prevented": 0,
    "avg_latency_ms": 0,
    "critical_alerts": 0,
}

AGENTIC_LOOP = {
    "phases": ["MONITOR", "DETECT", "ANALYSE", "RESPOND", "HUNT", "LESSONS"],
    "current": -1,
    "completed": [],
    "confidence": 0.0,
}

EVENT_LOG = []

def make_header() -> Panel:
    title = Text("🔥 PETROSHIELD TERMINAL v2047", style=f"bold {GREEN}")
    subtitle = Text("  •  Protegendo o Ouro Negro", style=ORANGE)
    header_text = Text.assemble(title, subtitle)
    return Panel(header_text, style=f"bold {GREEN}")

def make_metrics() -> Panel:
    table = Table(show_header=False, box=None)
    table.add_column("Metric", style=GREEN)
    table.add_column("Value", style=ORANGE, justify="right")
    table.add_row("Active Sessions", str(METRICS["active_sessions"]))
    table.add_row("Leaks Prevented", str(METRICS["leaks_prevented"]))
    table.add_row("Avg Latency", f"{METRICS['avg_latency_ms']}ms")
    table.add_row("Critical Alerts", str(METRICS["critical_alerts"]))
    return Panel(table, title="[bold green]Metrics", border_style=GREEN)

def make_torch(frame_idx: int) -> Panel:
    torch = Text(TORCH_FRAMES[frame_idx % len(TORCH_FRAMES)], style=ORANGE)
    return Panel(torch, title="[bold orange]PetroShield", border_style=ORANGE)

def make_agentic_loop() -> Panel:
    lines = []
    for phase in AGENTIC_LOOP["phases"]:
        if phase == AGENTIC_LOOP.get("active"):
            bar = "▓▓▓▓▓▓▓▓▓▓"
            lines.append(f"[{GREEN}][{phase}]{bar} ← ACTIVE (confidence: {AGENTIC_LOOP['confidence']})[/]")
        elif phase in AGENTIC_LOOP["completed"]:
            bar = "▓▓▓▓▓▓▓▓▓▓"
            lines.append(f"[dim green][{phase}]{bar} ✓[/]")
        else:
            bar = "░░░░░░░░░░"
            lines.append(f"[dim][{phase}]{bar}[/]")
    content = Text("\n".join(lines))
    return Panel(content, title="[bold cyan]Agentic Loop", border_style=CYAN)

def make_event_log() -> Panel:
    lines = EVENT_LOG[-8:] if len(EVENT_LOG) > 8 else EVENT_LOG
    content = Text("\n".join(lines) if lines else "Waiting for events...", style=GREEN)
    return Panel(content, title="[bold green]Event Stream", border_style=GREEN)

def make_layout(frame_idx: int) -> Layout:
    layout = Layout()
    layout.split_column(
        Layout(make_header(), size=3),
        Layout(name="main"),
    )
    layout["main"].split_row(
        Layout(name="left"),
        Layout(name="center"),
        Layout(name="right"),
    )
    layout["left"].split_column(
        Layout(make_metrics(), size=12),
        Layout(make_event_log()),
    )
    layout["center"].update(make_torch(frame_idx))
    layout["right"].update(make_agentic_loop())
    return layout

def log_event(msg: str, color: str = GREEN):
    EVENT_LOG.append(f"[{time.strftime('%H:%M:%S')}] {msg}")
    if len(EVENT_LOG) > 50:
        EVENT_LOG.pop(0)

def run_demo_sequence(live: Live):
    """Simulate the 4 demo scenes with animations."""
    # Scene 0: Idle
    time.sleep(1)

    # Scene 1: Unauthorized access
    log_event("Device quest-vr-001 → /secure-prompt", AMBER)
    AGENTIC_LOOP["active"] = "MONITOR"
    live.update(make_layout(0))
    time.sleep(0.8)

    log_event("Threat T1078 detected — Missing auth", ORANGE)
    AGENTIC_LOOP["completed"] = ["MONITOR"]
    AGENTIC_LOOP["active"] = "DETECT"
    live.update(make_layout(1))
    time.sleep(0.8)

    log_event("Risk Score: 94/100 — BLOCKED", ORANGE)
    AGENTIC_LOOP["completed"] = ["MONITOR", "DETECT"]
    AGENTIC_LOOP["active"] = "RESPOND"
    AGENTIC_LOOP["confidence"] = 0.94
    METRICS["critical_alerts"] += 1
    live.update(make_layout(2))
    time.sleep(0.8)

    AGENTIC_LOOP["completed"] = ["MONITOR", "DETECT", "RESPOND", "HUNT", "LESSONS"]
    AGENTIC_LOOP["active"] = None
    live.update(make_layout(3))
    time.sleep(1.5)

    # Reset for Scene 2
    AGENTIC_LOOP["completed"] = []
    AGENTIC_LOOP["confidence"] = 0.0

    # Scene 2: DLP redaction
    log_event("hololens-047 → authenticated query", GREEN)
    AGENTIC_LOOP["active"] = "MONITOR"
    live.update(make_layout(4))
    time.sleep(0.6)

    log_event("Entities: platform P-93, well alfa-bravo, password", AMBER)
    AGENTIC_LOOP["completed"] = ["MONITOR"]
    AGENTIC_LOOP["active"] = "DETECT"
    live.update(make_layout(5))
    time.sleep(0.6)

    log_event("Redacting P-93 → [ATIVO_RESTRITO]", GREEN)
    log_event("Redacting senha → [CREDENCIAL_BLOQUEADA]", GREEN)
    AGENTIC_LOOP["completed"] = ["MONITOR", "DETECT"]
    AGENTIC_LOOP["active"] = "RESPOND"
    AGENTIC_LOOP["confidence"] = 0.35
    METRICS["leaks_prevented"] += 3
    METRICS["avg_latency_ms"] = 47
    live.update(make_layout(6))
    time.sleep(1.2)

    AGENTIC_LOOP["completed"] = ["MONITOR", "DETECT", "RESPOND", "HUNT", "LESSONS"]
    AGENTIC_LOOP["active"] = None
    live.update(make_layout(7))
    time.sleep(1.5)

    # Reset for Scene 3
    AGENTIC_LOOP["completed"] = []

    # Scene 3: OT Protocol block
    log_event("hololens-047 → 'Modbus FC16 no controlador'", ORANGE)
    AGENTIC_LOOP["active"] = "MONITOR"
    live.update(make_layout(8))
    time.sleep(0.6)

    log_event("⚠️  OT PROTOCOL DETECTED: Modbus FC16", f"bold {ORANGE}")
    AGENTIC_LOOP["completed"] = ["MONITOR"]
    AGENTIC_LOOP["active"] = "DETECT"
    live.update(make_layout(9))
    time.sleep(0.6)

    log_event("CRITICAL RISK — Threat Score: 0.98", f"bold {ORANGE}")
    AGENTIC_LOOP["completed"] = ["MONITOR", "DETECT"]
    AGENTIC_LOOP["active"] = "RESPOND"
    AGENTIC_LOOP["confidence"] = 0.98
    METRICS["critical_alerts"] += 1
    METRICS["leaks_prevented"] += 1
    live.update(make_layout(10))
    time.sleep(1.0)

    log_event("BLOCKED + ESCALATED TO SOC", f"bold {ORANGE}")
    AGENTIC_LOOP["completed"] = ["MONITOR", "DETECT", "RESPOND", "HUNT", "LESSONS"]
    AGENTIC_LOOP["active"] = None
    live.update(make_layout(11))
    time.sleep(1.5)

    # Reset for Scene 4
    AGENTIC_LOOP["completed"] = []

    # Scene 4: Vendor risk cascade
    log_event("Dark web alert: Oceânica Engenharia", ORANGE)
    AGENTIC_LOOP["active"] = "MONITOR"
    live.update(make_layout(12))
    time.sleep(0.8)

    log_event("Vendor risk: 62 → 89 (CRITICAL)", ORANGE)
    AGENTIC_LOOP["completed"] = ["MONITOR"]
    AGENTIC_LOOP["active"] = "DETECT"
    live.update(make_layout(13))
    time.sleep(0.8)

    log_event("Suspending 12 XR sessions...", ORANGE)
    AGENTIC_LOOP["completed"] = ["MONITOR", "DETECT"]
    AGENTIC_LOOP["active"] = "RESPOND"
    AGENTIC_LOOP["confidence"] = 0.92
    METRICS["active_sessions"] -= 12
    live.update(make_layout(14))
    time.sleep(1.0)

    log_event("ANPD ticket: COMP-2026-0413-112", GREEN)
    AGENTIC_LOOP["completed"] = ["MONITOR", "DETECT", "RESPOND", "HUNT", "LESSONS"]
    AGENTIC_LOOP["active"] = None
    live.update(make_layout(15))
    time.sleep(2)

    log_event("DEMO COMPLETE — 4 threats neutralized", f"bold {GREEN}")
    live.update(make_layout(16))


def main():
    console.print("\n[bold green]Starting PetroShield Demo TUI...[/bold green]")
    console.print("[dim]Run the API server in another terminal: uvicorn main:app --reload[/dim]\n")
    time.sleep(1)

    with Live(make_layout(0), screen=True, refresh_per_second=4) as live:
        try:
            frame = 0
            # Run intro animation for a few seconds
            for _ in range(8):
                live.update(make_layout(frame))
                time.sleep(0.3)
                frame += 1

            run_demo_sequence(live)

            # Keep the final frame alive
            while True:
                live.update(make_layout(frame))
                time.sleep(0.3)
                frame += 1
        except KeyboardInterrupt:
            console.print("\n[bold green]PetroShield Demo TUI stopped.[/bold green]")
            sys.exit(0)


if __name__ == "__main__":
    main()
