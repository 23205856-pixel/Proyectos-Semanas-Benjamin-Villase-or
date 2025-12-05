# main.py
import argparse
from mst import GraphMST
import json
import sys

def pretty_print_edges(edges):
    return ", ".join([f"({u}-{v}:{w})" for u,v,w in edges])

def run(path: str, start: int = 0, out_prefix: str = "out"):
    g = GraphMST.from_json(path)

    edges_p, cost_p = g.prim_mst(start)
    edges_k, cost_k = g.kruskal_mst()

    full_cost = g.full_network_cost()

    print("RESULTADOS")
    print("----------")
    print(f"Nodos: {g.V}")
    print(f"Aristas totales (entrada): {len(g.edges)}")
    print()
    print("Prim MST:")
    print(" Edges:", pretty_print_edges(edges_p))
    print(" Cost:", cost_p)
    print()
    print("Kruskal MST:")
    print(" Edges:", pretty_print_edges(edges_k))
    print(" Cost:", cost_k)
    print()
    print(f"Costo red totalmente conectada (suma aristas listadas): {full_cost}")
    if cost_p == float('inf') or cost_k == float('inf'):
        print("\nAtención: el grafo no es conexo (alguno de los MST devolvió inf).")
    else:
        print(f"Ahorro respecto a red 'completamente' (suma aristas): {full_cost - cost_k:.2f}")

    # exportar mermaid
    mermaid_k = g.to_mermaid(edges_k)
    with open(f"{out_prefix}_graph_mermaid.md", "w", encoding="utf-8") as f:
        f.write("### Grafo y MST (Kruskal)\n\n```mermaid\n")
        f.write(mermaid_k)
        f.write("\n```\n")
    print(f"\nMermaid exportado a: {out_prefix}_graph_mermaid.md")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecutar MST (Prim & Kruskal)")
    parser.add_argument("graph", help="Archivo JSON con grafo (sample_graphs.json)")
    parser.add_argument("--start", type=int, default=0, help="Nodo inicio para Prim")
    parser.add_argument("--out", default="out", help="Prefijo de archivos de salida")
    args = parser.parse_args()
    run(args.graph, args.start, args.out)
