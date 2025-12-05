using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("=== SEMANA 6: PRUEBAS DE GRAFOS PONDERADOS ===\n");

        // Crear grafo de prueba
        WeightedGraph graph = new WeightedGraph(6);

        graph.AddEdge(0, 1, 10);
        graph.AddEdge(0, 2, 5);
        graph.AddEdge(2, 3, 2);
        graph.AddEdge(1, 3, 3);
        graph.AddEdge(2, 4, 8);
        graph.AddEdge(3, 4, 4);
        graph.AddEdge(4, 5, 7);

        RouteOptimizer optimizer = new RouteOptimizer(graph);

        // PRUEBA DIJKSTRA
        Console.WriteLine(">>> DIJKSTRA: Ruta más corta de 0 a 5\n");

        double dist = optimizer.GetDistanceDijkstra(0, 5);
        List<int> path = optimizer.GetShortestPathDijkstra(0, 5);

        Console.WriteLine($"Distancia mínima 0 → 5 = {dist}");
        Console.Write("Camino: ");

        foreach (int nodo in path)
            Console.Write($"{nodo} ");

        Console.WriteLine("\n");


        // PRUEBA FLOYD–WARSHALL
    
        Console.WriteLine(">>> FLOYD–WARSHALL: Matriz de distancias\n");

        double[,] fw = graph.FloydWarshall();

        for (int i = 0; i < 6; i++)
        {
            for (int j = 0; j < 6; j++)
            {
                if (double.IsInfinity(fw[i, j]))
                    Console.Write(" INF ");
                else
                    Console.Write($"{fw[i, j],4} ");
            }
            Console.WriteLine();
        }

        Console.WriteLine("\nFin de pruebas.");
    }
}
