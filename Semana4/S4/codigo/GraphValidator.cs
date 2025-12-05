using System;
using System.Collections.Generic;
using System.Linq;

public static class GraphValidator
{
    // Havel–Hakimi
    public static bool IsGraphicalSequence(List<int> degrees)
    {
        if (degrees == null || degrees.Count == 0)
            return true;

        
        var seq = degrees.OrderByDescending(x => x).ToList();

        int sum = seq.Sum();
        if (sum % 2 != 0) 
            return false;
        if (seq[0] >= seq.Count) 
            return false;

        while (seq.Count > 0)
        {
            seq.Sort((a, b) => b.CompareTo(a));
            int d = seq[0];
            seq.RemoveAt(0);

            if (d == 0) 
                return true;

            if (d > seq.Count) 
                return false;

            for (int i = 0; i < d; i++)
            {
                seq[i]--;
                if (seq[i] < 0)
                    return false;
            }
        }

        return true;
    }

    public static List<int> ExtractDegreeSequence(Graph<string> graph)
    {
        return graph.GetVertices()
                    .Select(v => graph.GetOutDegree(v))
                    .OrderByDescending(x => x)
                    .ToList();
    }

    public static bool ValidateConsistency(Graph<string> graph)
    {
        int totalDegree = graph.GetVertices()
                               .Sum(v => graph.GetOutDegree(v));
        return totalDegree % 2 == 0;
    }
}
