using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("🌍 === Generando Archivos de Grafos === 🌍");

        // Grafo no dirigido combinando ambos conjuntos de aristas
        var undirected = new Graph<string>();

        // Primer conjunto de aristas (del primer archivo original)
        undirected.AddEdge("A", "B", 2.0, false);
        undirected.AddEdge("A", "C", 3.0, false);
        undirected.AddEdge("B", "D", 1.0, false);
        undirected.AddEdge("C", "E", 4.0, false);
        undirected.AddEdge("D", "F", 5.0, false);
        undirected.AddEdge("E", "F", 2.0, false);
        undirected.AddEdge("G", "H", 6.0, false);

        // Segundo conjunto de aristas (del segundo archivo original)
        undirected.AddEdge("C", "F", 2.0, false);
        undirected.AddEdge("C", "H", 2.0, false);
        undirected.AddEdge("D", "E", 3.0, false);
        undirected.AddEdge("E", "F", 1.0, false);

        undirected.ExportToFile("datos/edges_undirected.txt", includeWeights: true, deduplicateUndirected: true);

        // Grafo dirigido combinando ambos conjuntos de aristas
        var directed = new Graph<string>();

        // Primer conjunto de aristas (del primer archivo original)
        directed.AddEdge("A", "G", 1.0);
        directed.AddEdge("B", "H", 3.0);
        directed.AddEdge("C", "D", 2.0);
        directed.AddEdge("F", "E", 4.0);
        directed.AddEdge("H", "A", 5.0);

        directed.AddEdge("A", "B", 2.0);
        directed.AddEdge("B", "A", 2.0);
        directed.AddEdge("A", "C", 3.0);
        directed.AddEdge("C", "A", 3.0);
        directed.AddEdge("B", "D", 1.0);
        directed.AddEdge("D", "B", 1.0);
        directed.AddEdge("C", "E", 4.0);
        directed.AddEdge("E", "C", 4.0);
        directed.AddEdge("D", "F", 5.0);
        directed.AddEdge("F", "D", 5.0);
        directed.AddEdge("E", "F", 2.0);
        directed.AddEdge("F", "E", 2.0);
        directed.AddEdge("G", "H", 6.0);
        directed.AddEdge("H", "G", 6.0);

        // Segundo conjunto de aristas (del segundo archivo original)
        directed.AddEdge("C", "F", 2.0);
        directed.AddEdge("C", "H", 2.0);
        directed.AddEdge("E", "D", 3.0);

        directed.ExportToFile("datos/edges_directed.txt", includeWeights: true);

        Console.WriteLine("🎉 ¡Archivos combinados creados correctamente!");
    }
}
