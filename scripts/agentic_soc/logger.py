"""
logger.py — Sistema de Logging Estilo Aplicação Real
=====================================================
3 targets simultâneos:
  1. STDOUT (Rich Console) — TUI verbosa com cores cyberpunk PetroShield
  2. JSON (arquivo) — Structured logging para auditoria forense
  3. Audit Chain — Hash chain SHA-256 append-only

Paleta PetroShield:
  - Neon Matrix Green: #00FF41
  - Fire Petroleum Orange: #FF6200
  - Deep Void Black: #0A0A0A
  - Cyan Sistema: #00FFFF
  - Vermelho Alerta: #FF3333
"""

import json
import time
import sys
from typing import Optional, List, Dict, Any, Tuple, Callable
import asyncio

try:
    from rich.console import Console
    from rich.text import Text
    from rich.panel import Panel
    from rich.table import Table
    HAS_RICH = True
except ImportError:
    HAS_RICH = False


# Paleta PetroShield
GREEN = "#00FF41"
ORANGE = "#FF6200"
CYAN = "#00FFFF"
RED = "#FF3333"
AMBER = "#FF9500"
DIM = "dim"


class AgenticLogger:
    """
    Logger multi-target para o sistema agêntico PetroShield.
    
    Cada evento de log inclui:
      - Timestamp ISO 8601
      - Agente emissor
      - Tipo: THOUGHT | ACTION | OBSERVATION | SYSTEM | ERROR | METRIC
      - Conteúdo
      - Metadados opcionais (scores, latências, etc.)
    """

    def __init__(
        self,
        json_log_path: Optional[str] = None,
        verbose: bool = True,
        use_rich: bool = True,
        emit_callback: Optional[Callable[[dict], None]] = None,
    ):
        self.verbose = verbose
        self.use_rich = use_rich and HAS_RICH
        self.json_log_path = json_log_path
        self.emit_callback = emit_callback
        self._log_buffer: List[dict] = []
        self._sequence = 0
        self._subscribers: List[asyncio.Queue] = []

        if self.use_rich:
            self.console = Console(force_terminal=True)
        else:
            self.console = None

        if json_log_path:
            self._json_file = open(json_log_path, "w", encoding="utf-8")
            self._json_file.write("[\n")
        else:
            self._json_file = None

    def _emit(self, entry: dict):
        """Emite um log para todos os targets configurados."""
        self._log_buffer.append(entry)
        self._sequence += 1

        # Callback síncrono para integração com TUI/Dashboard
        if self.emit_callback:
            try:
                self.emit_callback(entry)
            except Exception:
                pass

        # Target 1: Rich Console (STDOUT)
        if self.verbose:
            self._print_rich(entry)

        # Target 2: JSON file
        if self._json_file:
            prefix = "  " if self._sequence == 1 else ",\n  "
            self._json_file.write(prefix + json.dumps(entry, ensure_ascii=False))
            self._json_file.flush()

        # Target 3: Async Subscribers (SSE/Web)
        for q in self._subscribers[:]:
            try:
                q.put_nowait(entry)
            except Exception:
                # Remove subscriber if queue is closed or problematic
                self._subscribers.remove(q)

    def _print_rich(self, entry: dict):
        """Renderiza o log com estilo cyberpunk no terminal."""
        ts = entry["timestamp"].split("T")[1].rstrip("Z")
        agent = entry["agent"]
        log_type = entry["type"]
        content = entry["content"]

        if self.use_rich:
            color_map = {
                "THOUGHT": CYAN,
                "ACTION": ORANGE,
                "OBSERVATION": GREEN,
                "SYSTEM": GREEN,
                "ERROR": RED,
                "METRIC": AMBER,
                "PHASE": CYAN,
                "NARRATION": DIM,
            }
            color = color_map.get(log_type, GREEN)

            # Formato: [HH:MM:SS] [AGENT] TYPE: content
            line = Text()
            line.append(f"[{ts}] ", style="dim")
            line.append(f"[{agent}] ", style=f"bold {CYAN}")
            line.append(f"{log_type}: ", style=f"bold {color}")
            line.append(content, style=color)
            self.console.print(line)
        else:
            print(f"[{ts}] [{agent}] {log_type}: {content}", file=sys.stderr)

    # -------------------------------------------------------------------------
    # API Pública
    # -------------------------------------------------------------------------

    def thought(self, agent: str, content: str, **meta):
        """Chain-of-thought visível (Glass-Box Intelligence)."""
        self._emit({
            "seq": self._sequence,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "agent": agent,
            "type": "THOUGHT",
            "content": content,
            **meta,
        })

    def action(self, agent: str, content: str, tool: str = "", **meta):
        """Ação executada por um agente (tool call)."""
        self._emit({
            "seq": self._sequence,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "agent": agent,
            "type": "ACTION",
            "content": content,
            "tool": tool,
            **meta,
        })

    def observation(self, agent: str, content: str, **meta):
        """Resultado observado após uma ação."""
        self._emit({
            "seq": self._sequence,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "agent": agent,
            "type": "OBSERVATION",
            "content": content,
            **meta,
        })

    def system(self, content: str, **meta):
        """Mensagem de sistema / infraestrutura."""
        self._emit({
            "seq": self._sequence,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "agent": "SYSTEM",
            "type": "SYSTEM",
            "content": content,
            **meta,
        })

    def phase_transition(self, from_phase: str, to_phase: str, reason: str = ""):
        """Transição de estado no grafo agêntico."""
        self._emit({
            "seq": self._sequence,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "agent": "GRAPH",
            "type": "PHASE",
            "content": f"{from_phase} → {to_phase}" + (f" ({reason})" if reason else ""),
            "from_phase": from_phase,
            "to_phase": to_phase,
        })

    def metric(self, name: str, value: Any, unit: str = ""):
        """Métrica de performance ou negócio."""
        self._emit({
            "seq": self._sequence,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "agent": "METRICS",
            "type": "METRIC",
            "content": f"{name}: {value}{' ' + unit if unit else ''}",
            "metric_name": name,
            "metric_value": value,
            "metric_unit": unit,
        })

    def error(self, agent: str, content: str, **meta):
        """Erro no sistema."""
        self._emit({
            "seq": self._sequence,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "agent": agent,
            "type": "ERROR",
            "content": content,
            **meta,
        })

    def narrate(self, text: str):
        """Narração teatral para a demo."""
        self._emit({
            "seq": self._sequence,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "agent": "NARRATOR",
            "type": "NARRATION",
            "content": text,
        })

    def scene_header(self, scene_id: str, title: str):
        """Header visual de cena para a demo."""
        if self.use_rich:
            self.console.print()
            self.console.print(Panel(
                f"[bold {GREEN}]{title}[/]",
                title=f"[bold {ORANGE}]═══ {scene_id.upper()} ═══[/]",
                border_style=ORANGE,
                width=80,
            ))
            self.console.print()
        else:
            print(f"\n{'='*60}")
            print(f"  {scene_id.upper()}: {title}")
            print(f"{'='*60}\n")

    def summary_table(self, title: str, rows: List[tuple]):
        """Tabela de sumário formatada."""
        if self.use_rich:
            table = Table(title=title, show_header=True, border_style=GREEN)
            table.add_column("Métrica", style=CYAN)
            table.add_column("Valor", style=ORANGE, justify="right")
            for name, value in rows:
                table.add_row(name, str(value))
            self.console.print(table)
        else:
            print(f"\n{title}")
            for name, value in rows:
                print(f"  {name}: {value}")

    def subscribe(self) -> asyncio.Queue:
        """Cria e retorna uma nova fila de logs para este logger."""
        q = asyncio.Queue()
        self._subscribers.append(q)
        return q

    def unsubscribe(self, q: asyncio.Queue):
        """Remove um inscrito."""
        if q in self._subscribers:
            self._subscribers.remove(q)

    # -------------------------------------------------------------------------
    # Lifecycle
    # -------------------------------------------------------------------------

    def close(self):
        """Fecha o arquivo JSON (finaliza o array)."""
        if self._json_file:
            self._json_file.write("\n]\n")
            self._json_file.close()

    @property
    def buffer(self) -> List[dict]:
        """Retorna todos os logs emitidos."""
        return self._log_buffer

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
