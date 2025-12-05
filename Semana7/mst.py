# mst.py
from typing import List, Tuple, Dict
import heapq
import json

Edge = Tuple[int, int, float]  # (u, v, weight)

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        ri = self.find(i)
        rj = self.find(j)
        if ri == rj:
            return False
        if self.rank[ri] < self.rank[rj]:
            self.parent[ri] = rj
        elif self.rank[ri] > self.rank[rj]:
            self.parent[rj] = ri
        else:
            self.parent[rj] = ri
            self.rank[ri] += 1
        return True

class GraphMST:
    def __init__(self, vertices: int):
        self.V = vertices
        self.edges: List[Edge] = []
        self.adj: Dict[int, List[Tuple[int, float]]] = {i: [] for i in range(vertices)}

    def add_edge(self, u: int, v: int, w: float):
        if u < 0 or v < 0 or u >= self.V or v >= self.V:
            raise IndexError("Nodo fuera de rango")
        # guardamos cada arista una sola vez (u,v,w)
        self.edges.append((u, v, w))
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # PRIM usando min-heap
    def prim_mst(self, start_node: int = 0) -> Tuple[List[Edge], float]:
        visited = [False] * self.V
        pq = []
        visited[start_node] = True
        for v, w in self.adj[start_node]:
            heapq.heappush(pq, (w, start_node, v))

        mst_edges: List[Edge] = []
        mst_cost = 0.0

        while pq and len(mst_edges) < self.V - 1:
            w, u, v = heapq.heappop(pq)
            if visited[v]:
                continue
            visited[v] = True
            mst_edges.append((u, v, w))
            mst_cost += w
            for nx, nw in self.adj[v]:
                if not visited[nx]:
                    heapq.heappush(pq, (nw, v, nx))

        # Si el grafo no es conexo, prim no cubrirá todos los nodos
        if len(mst_edges) != self.V - 1:
            return mst_edges, float('inf')  # indica no conexo
        return mst_edges, mst_cost

    # KRUSKAL con DSU
    def kruskal_mst(self) -> Tuple[List[Edge], float]:
        dsu = DSU(self.V)
        sorted_edges = sorted(self.edges, key=lambda e: e[2])
        mst_edges: List[Edge] = []
        mst_cost = 0.0
        for u, v, w in sorted_edges:
            if dsu.union(u, v):
                mst_edges.append((u, v, w))
                mst_cost += w
                if len(mst_edges) == self.V - 1:
                    break
        if len(mst_edges) != self.V - 1:
            return mst_edges, float('inf')
        return mst_edges, mst_cost

    # Costo de red completamente conectada (sumatoria de todas las aristas si fueran necesarias)
    def full_network_cost(self) -> float:
        # Para comparación razonable: suma de aristas tal cual están (no duplicadas)
        return sum(w for (_, _, w) in self.edges)

    # Exportar Mermaid para documentación: grafo completo y MST (resaltado)
    def to_mermaid(self, mst_edges: List[Edge]) -> str:
        mst_set = {(min(u,v), max(u,v)) for u,v,_ in mst_edges}
        lines = ["graph LR"]
        # nodos
        for i in range(self.V):
            lines.append(f"    N{i}(({i}))")
        # aristas con peso; resaltamos MST
        for u, v, w in self.edges:
            a, b = min(u, v), max(u, v)
            label = f"{w}"
            if (a, b) in mst_set:
                # marcar como MST (bold en mermaid mediante style lines no directo, usamos ---|peso| para claridad)
                lines.append(f"    N{u} ---|{label} (MST)| N{v}")
            else:
                lines.append(f"    N{u} ---|{label}| N{v}")
        return "\n".join(lines)

    # Cargar grafo desde JSON (formato: {"vertices": n, "edges": [[u,v,w],...]})
    @staticmethod
    def from_json(path: str) -> "GraphMST":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        g = GraphMST(data["vertices"])
        for u, v, w in data["edges"]:
            g.add_edge(int(u), int(v), float(w))
        return g
