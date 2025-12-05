using System;
using System.Collections.Generic;
using System.Linq;

public class GraphTraversal
{
    private Dictionary<int, List<int>> adj = new Dictionary<int, List<int>>();

    public void AddEdge(int u, int v)
    {
        if (!adj.ContainsKey(u)) adj[u] = new List<int>();
        if (!adj.ContainsKey(v)) adj[v] = new List<int>();

        // Grafo NO dirigido (como tus tests lo usan)
        adj[u].Add(v);
        adj[v].Add(u);
    }

    public List<int> GetNeighbors(int node)
    {
        if (adj.ContainsKey(node))
            return adj[node];
        return new List<int>();
    }

    public List<int> BFS(int start)
    {
        var visited = new HashSet<int>();
        var result = new List<int>();
        var q = new Queue<int>();

        visited.Add(start);
        q.Enqueue(start);

        while (q.Count > 0)
        {
            int node = q.Dequeue();
            result.Add(node);

            foreach (var n in adj[node])
                if (!visited.Contains(n))
                {
                    visited.Add(n);
                    q.Enqueue(n);
                }
        }

        return result;
    }

    public List<int> DFSRecursive(int start)
    {
        var visited = new HashSet<int>();
        var result = new List<int>();

        void DFS(int v)
        {
            visited.Add(v);
            result.Add(v);

            foreach (var n in adj[v])
                if (!visited.Contains(n))
                    DFS(n);
        }

        DFS(start);
        return result;
    }

    public List<int> DFSIterative(int start)
    {
        var visited = new HashSet<int>();
        var result = new List<int>();
        var stack = new Stack<int>();

        stack.Push(start);

        while (stack.Count > 0)
        {
            var node = stack.Pop();

            if (visited.Contains(node)) continue;

            visited.Add(node);
            result.Add(node);

            var neigh = adj[node].ToList();
            neigh.Reverse();

            foreach (var n in neigh)
                if (!visited.Contains(n))
                    stack.Push(n);
        }

        return result;
    }
}
