"""
orchestrator.py — Motor de Orquestração StateMachine (Python Puro)
==================================================================
Reimplementação minimalista do padrão LangGraph StateGraph
SEM usar LangGraph como dependência.

Conceitos implementados:
  - StateGraph: Grafo direcionado com nós (funções) e arestas (transições)
  - ConditionalEdges: Roteamento dinâmico baseado no estado
  - CompiledGraph: Grafo compilado com .invoke() e .stream()
  - State Merging: Cada nó retorna um patch; o motor faz o merge

Complexidade:
  - Tempo: O(V + E) por traversal do grafo
  - Espaço: O(S) onde S = tamanho do estado

Dependências: ZERO (Python puro — usa apenas typing e dataclasses da stdlib)

Uso:
  python -m scripts.agentic_soc.orchestrator [--test]
"""

from typing import Dict, Callable, Any, Optional, Generator, List, Tuple
import time


# Sentinelas especiais para START e END
START = "__START__"
END = "__END__"


class StateMachine:
    """
    Reimplementação minimalista do LangGraph StateGraph.
    
    Um grafo direcionado onde:
      - Cada NÓ é uma função (state) -> dict (patch parcial do estado)
      - Cada ARESTA é uma transição entre nós
      - ARESTAS CONDICIONAIS usam uma função (state) -> str para decidir o próximo nó
    
    O grafo é compilado em um CompiledGraph para execução.
    """

    def __init__(self, state_schema: type = dict):
        """
        Parâmetros:
          state_schema: TypedDict que define a forma do estado (para documentação)
        """
        self.state_schema = state_schema
        self._nodes: Dict[str, Callable] = {}
        self._edges: Dict[str, str] = {}
        self._conditional_edges: Dict[str, Callable] = {}
        self._entry_point: Optional[str] = None

    def add_node(self, name: str, fn: Callable):
        """
        Adiciona um nó ao grafo.
        
        Parâmetros:
          name: Identificador único do nó
          fn: Função (state: dict) -> dict que processa o estado
        """
        if name in (START, END):
            raise ValueError(f"'{name}' é um nome reservado.")
        self._nodes[name] = fn

    def add_edge(self, source: str, target: str):
        """
        Adiciona uma aresta fixa (incondicional) entre dois nós.
        
        Parâmetros:
          source: Nó de origem (ou START para ponto de entrada)
          target: Nó de destino (ou END para ponto de saída)
        """
        if source == START:
            self._entry_point = target
        else:
            self._edges[source] = target

    def add_conditional_edges(self, source: str, router: Callable):
        """
        Adiciona arestas condicionais a partir de um nó.
        
        Parâmetros:
          source: Nó de origem
          router: Função (state: dict) -> str que retorna o nome do próximo nó
                  Pode retornar END para encerrar o grafo.
        """
        self._conditional_edges[source] = router

    def compile(self) -> 'CompiledGraph':
        """
        Compila o grafo em um CompiledGraph executável.
        
        Validações:
          - Deve ter pelo menos um nó
          - Deve ter um ponto de entrada (START -> algum nó)
          - Todos os targets de arestas devem existir como nós (ou END)
        """
        if not self._nodes:
            raise ValueError("O grafo não possui nós. Use add_node() antes de compilar.")

        if not self._entry_point:
            raise ValueError("O grafo não possui ponto de entrada. Use add_edge(START, 'nome_do_nó').")

        if self._entry_point not in self._nodes:
            raise ValueError(f"Ponto de entrada '{self._entry_point}' não existe como nó.")

        # Validar targets das arestas fixas
        for src, tgt in self._edges.items():
            if tgt != END and tgt not in self._nodes:
                raise ValueError(f"Aresta {src} -> {tgt}: nó '{tgt}' não existe.")

        return CompiledGraph(
            nodes=dict(self._nodes),
            edges=dict(self._edges),
            conditional_edges=dict(self._conditional_edges),
            entry_point=self._entry_point,
        )

    def get_topology(self) -> dict:
        """Retorna a topologia do grafo como dict serializável (para API/visualização)."""
        return {
            "nodes": list(self._nodes.keys()),
            "edges": dict(self._edges),
            "conditional_edges": list(self._conditional_edges.keys()),
            "entry_point": self._entry_point,
        }


class CompiledGraph:
    """
    Grafo compilado e executável.
    
    Métodos:
      .invoke(state) -> state_final   — Executa o grafo até END
      .stream(state) -> Generator     — Executa com yield a cada transição
    """

    def __init__(
        self,
        nodes: Dict[str, Callable],
        edges: Dict[str, str],
        conditional_edges: Dict[str, Callable],
        entry_point: str,
    ):
        self._nodes = nodes
        self._edges = edges
        self._conditional_edges = conditional_edges
        self._entry_point = entry_point
        self._execution_trace: List[dict] = []

    def invoke(self, state: dict, max_steps: int = 50) -> dict:
        """
        Executa o grafo até END ou max_steps.
        
        Algoritmo:
          1. current_node = entry_point
          2. LOOP:
             a. Executar nó: patch = node_fn(state)
             b. Merge: state = {**state, **patch}
             c. Resolver próximo nó (aresta fixa ou condicional)
             d. Se próximo = END ou steps > max_steps: BREAK
          3. Retornar state final
        
        Complexidade: O(steps × node_complexity)
        """
        self._execution_trace = []
        current = self._entry_point
        steps = 0

        while current != END and steps < max_steps:
            node_fn = self._nodes.get(current)
            if not node_fn:
                raise RuntimeError(f"Nó '{current}' não encontrado no grafo compilado.")

            # Executar nó
            start_time = time.time()
            patch = node_fn(state) or {}
            elapsed_ms = int((time.time() - start_time) * 1000)

            # Merge do patch no estado
            state = {**state, **patch}

            # Registrar trace
            self._execution_trace.append({
                "step": steps,
                "node": current,
                "elapsed_ms": elapsed_ms,
                "patch_keys": list(patch.keys()),
            })

            # Resolver próximo nó
            if current in self._conditional_edges:
                router = self._conditional_edges[current]
                next_node = router(state)
            elif current in self._edges:
                next_node = self._edges[current]
            else:
                next_node = END

            current = next_node
            steps += 1

        return state

    def stream(self, state: dict, max_steps: int = 50) -> Generator[Tuple[str, dict], None, None]:
        """
        Executa o grafo com yield a cada transição.
        
        Yields: (node_name, state_snapshot) a cada passo
        Permite visualização em tempo real no TUI.
        """
        self._execution_trace = []
        current = self._entry_point
        steps = 0

        while current != END and steps < max_steps:
            node_fn = self._nodes.get(current)
            if not node_fn:
                raise RuntimeError(f"Nó '{current}' não encontrado no grafo compilado.")

            start_time = time.time()
            patch = node_fn(state) or {}
            elapsed_ms = int((time.time() - start_time) * 1000)

            state = {**state, **patch}

            self._execution_trace.append({
                "step": steps,
                "node": current,
                "elapsed_ms": elapsed_ms,
                "patch_keys": list(patch.keys()),
            })

            yield current, dict(state)

            # Resolver próximo nó
            if current in self._conditional_edges:
                router = self._conditional_edges[current]
                next_node = router(state)
            elif current in self._edges:
                next_node = self._edges[current]
            else:
                next_node = END

            current = next_node
            steps += 1

    @property
    def trace(self) -> List[dict]:
        """Retorna o trace de execução do último invoke/stream."""
        return self._execution_trace


# =============================================================================
# SELF-TEST
# =============================================================================

def _self_test():
    """Teste de integridade do StateMachine."""
    print("=" * 60)
    print("  StateMachine Self-Test -- PetroShield AxeGuard")
    print("=" * 60)

    # Definir nós simples
    def node_a(state):
        return {"visited": state.get("visited", []) + ["A"], "count": state.get("count", 0) + 1}

    def node_b(state):
        return {"visited": state.get("visited", []) + ["B"], "count": state.get("count", 0) + 1}

    def node_c(state):
        return {"visited": state.get("visited", []) + ["C"], "count": state.get("count", 0) + 1}

    def router(state):
        if state.get("count", 0) >= 2:
            return END
        return "node_b"

    # Construir grafo
    sm = StateMachine()
    sm.add_node("node_a", node_a)
    sm.add_node("node_b", node_b)
    sm.add_node("node_c", node_c)
    sm.add_edge(START, "node_a")
    sm.add_edge("node_a", "node_b")
    sm.add_conditional_edges("node_b", router)

    # Compilar e executar
    graph = sm.compile()
    result = graph.invoke({})

    # Validar
    assert result["visited"] == ["A", "B"], f"Expected ['A', 'B'], got {result['visited']}"
    assert result["count"] == 2, f"Expected 2, got {result['count']}"
    assert len(graph.trace) == 2, f"Expected 2 steps, got {len(graph.trace)}"

    print(f"  [OK] Grafo executado: {result['visited']}")
    print(f"  [OK] Steps: {len(graph.trace)}")
    print(f"  [OK] Estado final: count={result['count']}")

    # Testar stream
    states_seen = list(graph.stream({}))
    assert len(states_seen) == 2, f"Expected 2 yields, got {len(states_seen)}"
    print(f"  [OK] Stream: {len(states_seen)} transicoes")

    # Testar topologia
    topo = sm.get_topology()
    assert len(topo["nodes"]) == 3
    print(f"  [OK] Topologia: {topo['nodes']}")

    print("\n  [PASS] TODOS OS TESTES PASSARAM")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        _self_test()
    else:
        print("Uso: python -m scripts.agentic_soc.orchestrator --test")
        print("Para a demo completa: python -m scripts.agentic_soc.theatre")
