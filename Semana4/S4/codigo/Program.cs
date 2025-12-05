using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("🌍 === Generando Archivos de Grafos === 🌍");

        //  SEMANA 3: Generación y exportación de grafos
       

        var undirected = new Graph<string>();

        undirected.AddEdge("A", "B", 2.0, false);
        undirected.AddEdge("A", "C", 3.0, false);
        undirected.AddEdge("B", "D", 1.0, false);
        undirected.AddEdge("C", "E", 4.0, false);
        undirected.AddEdge("D", "F", 5.0, false);
        undirected.AddEdge("E", "F", 2.0, false);
        undirected.AddEdge("G", "H", 6.0, false);

        undirected.AddEdge("C", "F", 2.0, false);
        undirected.AddEdge("C", "H", 2.0, false);
        undirected.AddEdge("D", "E", 3.0, false);
        undirected.AddEdge("E", "F", 1.0, false);

        undirected.ExportToFile("datos/edges_undirected.txt", includeWeights: true, deduplicateUndirected: true);

        var directed = new Graph<string>();

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

     
        directed.AddEdge("C", "F", 2.0);
        directed.AddEdge("C", "H", 2.0);
        directed.AddEdge("E", "D", 3.0);

        directed.ExportToFile("datos/edges_directed.txt", includeWeights: true);

        Console.WriteLine("🎉 ¡Archivos combinados creados correctamente!");



        //  SEMANA 4: Aplicación de Havel–Hakimi y validación
    

        Console.WriteLine("\n🔍 === Semana 4: Validación de Secuencias ===\n");


        var seq = new List<int> { 4, 3, 3, 2, 2, 2, 1, 1 };
        Console.WriteLine("Secuencia propuesta: [4,3,3,2,2,2,1,1]");
        Console.WriteLine($"¿Es gráfica? → {GraphValidator.IsGraphicalSequence(seq)}");


       
        try
        {
            var extracted = GraphValidator.ExtractDegreeSequence(undirected);

            Console.WriteLine($"\nSecuencia extraída del grafo no dirigido:");
            Console.WriteLine($"[{string.Join(", ", extracted)}]");

            Console.WriteLine($"¿Es gráfica? → {GraphValidator.IsGraphicalSequence(extracted)}");
            Console.WriteLine($"¿Consistente? → {GraphValidator.ValidateConsistency(undirected)}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"⚠️ Error al extraer secuencia del grafo: {ex.Message}");
        }



     
        Console.WriteLine("\n📌 === Tests oficiales de la Semana 4 ===");

        var tests = new List<List<int>> {
            new List<int>{4,3,3,2,2,2,1,1},
            new List<int>{3,2,2,1},
            new List<int>{4,3,3,2,2,2},
            new List<int>{0,0,0,0},
            new List<int>{3,3,3,3},
            new List<int>{3,3,3,1},
            new List<int>{5,5,4,3,2,1},
            new List<int>{3,2,1},
            new List<int>{6,1,1,1,1,1,1},
            new List<int>{5,3,2,2,1}
        };

        int i = 1;
        foreach (var test in tests)
        {
            Console.WriteLine($"{i++}. [{string.Join(",", test)}] → {GraphValidator.IsGraphicalSequence(test)}");
        }
    }
}
