using System;
using System.Collections.Generic;

public class PathFinder
{
    private GraphTraversal graph;

    public PathFinder(GraphTraversal g)
    {
        graph = g;
    }

    public List<int>? ShortestPath(int start, int end)
    {
        var visited = new HashSet<int>();
        var parent = new Dictionary<int, int>();
        var queue = new Queue<int>();

        visited.Add(start);
        parent[start] = -1;
        queue.Enqueue(start);

        while (queue.Count > 0)
        {
            int node = queue.Dequeue();

            if (node == end)
                break;

            // Obtener SOLO vecinos REALES
            foreach (var neighbor in graph.GetNeighbors(node))
            {
                if (!visited.Contains(neighbor))
                {
                    visited.Add(neighbor);
                    parent[neighbor] = node;
                    queue.Enqueue(neighbor);
                }
            }
        }

        // No existe camino
        if (!parent.ContainsKey(end))
            return null;

        // Reconstruir ruta
        var path = new List<int>();
        int current = end;

        while (current != -1)
        {
            path.Add(current);
            current = parent[current];
        }

        path.Reverse();
        return path;
    }
}
