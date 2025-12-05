using System;
using System.Collections.Generic;

public class WeightedGraph
{
    private int n;
    private List<(int, double)>[] adj;

    public WeightedGraph(int nodes)
    {
        n = nodes;
        adj = new List<(int, double)>[nodes];
        for (int i = 0; i < nodes; i++)
            adj[i] = new List<(int, double)>();
    }

    public void AddEdge(int u, int v, double w)
    {
        adj[u].Add((v, w));
        // Si tu grafo es no dirigido usa también:
        // adj[v].Add((u, w));
    }

    // ==========================
    // DIJKSTRA
    // ==========================
    public (double[] dist, int[] parent) Dijkstra(int src)
    {
        if (src < 0 || src >= n)
            throw new ArgumentException("Nodo de origen inválido");

        double[] dist = new double[n];
        int[] parent = new int[n];
        bool[] visited = new bool[n];

        for (int i = 0; i < n; i++)
        {
            dist[i] = double.PositiveInfinity;
            parent[i] = -1;
        }

        dist[src] = 0;

        var pq = new PriorityQueue<(int node, double cost), double>();
        pq.Enqueue((src, 0), 0);

        while (pq.Count > 0)
        {
            var (u, cost) = pq.Dequeue();
            if (visited[u]) continue;
            visited[u] = true;

            foreach (var (v, w) in adj[u])
            {
                if (dist[u] + w < dist[v])
                {
                    dist[v] = dist[u] + w;
                    parent[v] = u;
                    pq.Enqueue((v, dist[v]), dist[v]);
                }
            }
        }

        return (dist, parent);
    }

    // ==========================
    // FLOYD–WARSHALL
    // ==========================
    public double[,] FloydWarshall()
    {
        double[,] dist = new double[n, n];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                dist[i, j] = (i == j) ? 0 : double.PositiveInfinity;

        for (int u = 0; u < n; u++)
            foreach (var (v, w) in adj[u])
                dist[u, v] = w;

        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (dist[i, k] + dist[k, j] < dist[i, j])
                        dist[i, j] = dist[i, k] + dist[k, j];

        // detectar ciclos negativos
        for (int i = 0; i < n; i++)
            if (dist[i, i] < 0)
                throw new Exception("Ciclo negativo detectado");

        return dist;
    }
}
