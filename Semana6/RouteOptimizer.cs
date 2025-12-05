using System;
using System.Collections.Generic;

public class RouteOptimizer
{
    private WeightedGraph graph;

    public RouteOptimizer(WeightedGraph g)
    {
        graph = g;
    }

    public List<int> GetShortestPathDijkstra(int src, int dst)
    {
        var (dist, parent) = graph.Dijkstra(src);

        if (double.IsInfinity(dist[dst]))
            return new List<int>(); // no hay ruta

        List<int> path = new();
        for (int cur = dst; cur != -1; cur = parent[cur])
            path.Add(cur);

        path.Reverse();
        return path;
    }

    public double GetDistanceDijkstra(int src, int dst)
    {
        return graph.Dijkstra(src).dist[dst];
    }

    public double GetDistanceFW(int src, int dst)
    {
        var dist = graph.FloydWarshall();
        return dist[src, dst];
    }
}
