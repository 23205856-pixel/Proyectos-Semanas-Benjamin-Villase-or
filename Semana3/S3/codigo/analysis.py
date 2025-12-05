from collections import defaultdict
from typing import Dict, List, Tuple
import os

# ===============================================
#  RUTAS ROBUSTAS — ¡ESTA ES LA CORRECCIÓN CLAVE!
# ===============================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))    # carpeta /codigo
DATA_DIR = os.path.join(BASE_DIR, "..", "datos")         # carpeta /datos

UNDIRECTED_FILE = os.path.join(DATA_DIR, "edges_undirected.txt")
DIRECTED_FILE = os.path.join(DATA_DIR, "edges_directed.txt")


def load_graph(file_path: str, is_directed: bool = True) -> Dict[str, List[Tuple[str, float]]]:
    adjacency_list = defaultdict(list)

    if not os.path.exists(file_path):
        print(f"❌ Error: El archivo '{file_path}' no existe.")
        return adjacency_list

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()

                if not line or line.startswith('#'):
                    continue

                parts = line.split()
                if len(parts) < 2:
                    print(f"⚠️  Línea {line_num}: '{line}' ignorada (faltan vértices)")
                    continue

                from_vertex, to_vertex = parts[0], parts[1]

                try:
                    weight = float(parts[2]) if len(parts) > 2 else 1.0
                except ValueError:
                    print(f"⚠️  Línea {line_num}: peso inválido, usando 1.0")
                    weight = 1.0

                adjacency_list[from_vertex].append((to_vertex, weight))

                if not is_directed:
                    adjacency_list[to_vertex].append((from_vertex, weight))

    except Exception as e:
        print(f"❌ Error inesperado: {e}")

    return dict(adjacency_list)


def get_neighbors(graph, vertex):
    return graph.get(vertex, [])


def has_edge(graph, from_vertex, to_vertex):
    neighbors = graph.get(from_vertex, [])
    return any(neighbor == to_vertex for neighbor, _ in neighbors)


def get_out_degree(graph, vertex):
    return len(graph.get(vertex, []))


def get_in_degree(graph, vertex):
    in_degree = 0
    for neighbors in graph.values():
        in_degree += sum(1 for neighbor, _ in neighbors if neighbor == vertex)
    return in_degree


def analyze_graph(graph, graph_type):
    print(f"\n{'='*50}")
    print(f"🔍 Análisis del Grafo {graph_type}")
    print(f"{'='*50}")

    if not graph:
        print("⚠️  El grafo está vacío")
        return

    vertices = sorted(graph.keys())
    total_edges = sum(len(neighbors) for neighbors in graph.values())

    print(f"📊 Estadísticas generales:")
    print(f"   • Vértices: {len(vertices)}")
    print(f"   • Aristas: {total_edges}")

    max_possible_edges = len(vertices) * (len(vertices) - 1)
    if max_possible_edges > 0:
        density = total_edges / max_possible_edges
        print(f"   • Densidad: {density:.3f}")

    print("\n🔍 Detalles por vértice:")
    for vertex in vertices:
        out_deg = get_out_degree(graph, vertex)
        in_deg = get_in_degree(graph, vertex)
        neighbors = get_neighbors(graph, vertex)
        neighbor_str = ", ".join([f"{n}({w:.1f})" for n, w in neighbors])

        print(f"   {vertex}: Out={out_deg}, In={in_deg}")
        print(f"      Vecinos: [{neighbor_str}]")


def find_most_connected_vertex(graph):
    if not graph:
        return ""

    best = ""
    max_deg = -1

    for vertex in graph:
        total = get_in_degree(graph, vertex) + get_out_degree(graph, vertex)
        if total > max_deg:
            max_deg = total
            best = vertex

    return best


def main():
    print("🌍 === Análisis de Mapas de Tráfico - Proyecto Semana 3 ===")

    undirected_graph = load_graph(UNDIRECTED_FILE, is_directed=False)
    analyze_graph(undirected_graph, "No Dirigido")

    directed_graph = load_graph(DIRECTED_FILE, is_directed=True)
    analyze_graph(directed_graph, "Dirigido")

    print("\n" + "="*50)
    print("🔗 Pruebas de Conectividad")
    print("="*50)

    if directed_graph:
        print(f"A→G: {has_edge(directed_graph, 'A', 'G')}")
        print(f"G→A: {has_edge(directed_graph, 'G', 'A')}")
        print(f"OutDegree(A): {get_out_degree(directed_graph, 'A')}")
        print(f"InDegree(A): {get_in_degree(directed_graph, 'A')}")

        most = find_most_connected_vertex(directed_graph)
        print(f"Vértice más conectado: {most}")

    print("\n🎉 ¡Análisis completado exitosamente!")


if __name__ == "__main__":
    main()
