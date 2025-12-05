using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

public class Graph<T> where T : IComparable
{
    private readonly Dictionary<T, List<(T, double)>> adjacencyList = new();

    public void AddVertex(T vertex)
    {
        if (!adjacencyList.ContainsKey(vertex))
        {
            adjacencyList[vertex] = new List<(T, double)>();
        }
    }

    public void AddEdge(T from, T to, double weight = 1.0, bool isDirected = true)
    {
        AddVertex(from);
        AddVertex(to);

        adjacencyList[from].Add((to, weight));

        if (!isDirected)
        {
            adjacencyList[to].Add((from, weight));
        }
    }

    public void ExportToFile(string filename, bool includeWeights = true, bool deduplicateUndirected = false)
    {
        try
        {
            using var writer = new StreamWriter(filename);
            var processedEdges = new HashSet<string>();

            foreach (var vertex in adjacencyList.Keys.OrderBy(v => v))
            {
                foreach (var (neighbor, weight) in adjacencyList[vertex])
                {
                    if (deduplicateUndirected)
                    {
                        var vertexStr = vertex?.ToString() ?? "";
                        var neighborStr = neighbor?.ToString() ?? "";
                        var edgeKey = vertex.CompareTo(neighbor) <= 0
                            ? $"{vertexStr}→{neighborStr}"
                            : $"{neighborStr}→{vertexStr}";
                        if (!processedEdges.Add(edgeKey))
                            continue;
                    }

                    var line = includeWeights
                        ? $"{vertex} {neighbor} {weight:F1}"
                        : $"{vertex} {neighbor}";
                    writer.WriteLine(line);
                }
            }
            Console.WriteLine($"✅ Archivo '{filename}' exportado exitosamente.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"❌ Error al exportar archivo: {ex.Message}");
        }
    }
}
