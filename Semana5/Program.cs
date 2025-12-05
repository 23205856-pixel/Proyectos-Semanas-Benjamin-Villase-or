using System;

class Program
{
    static void Main()
    {
        var g = new GraphTraversal();

        // Crear el grafo
        g.AddEdge(1, 2);
        g.AddEdge(1, 3);
        g.AddEdge(2, 4);
        g.AddEdge(2, 5);
        g.AddEdge(3, 6);

        Console.WriteLine("===== BFS =====");
        Console.WriteLine(string.Join(" → ", g.BFS(1)));

        Console.WriteLine("\n===== DFS Recursivo =====");
        Console.WriteLine(string.Join(" → ", g.DFSRecursive(1)));

        Console.WriteLine("\n===== DFS Iterativo =====");
        Console.WriteLine(string.Join(" → ", g.DFSIterative(1)));

        var pf = new PathFinder(g);

        Console.WriteLine("\n===== Camino más corto 1 → 5 =====");
        var camino = pf.ShortestPath(1, 5);

        if (camino != null)
            Console.WriteLine(string.Join(" → ", camino));
        else
            Console.WriteLine("No existe camino entre esos nodos.");
    }
}
