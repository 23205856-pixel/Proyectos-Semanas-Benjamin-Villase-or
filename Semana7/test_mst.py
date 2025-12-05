# test_mst.py
import unittest
from mst import GraphMST

class TestMST(unittest.TestCase):
    def test_small_graph(self):
        g = GraphMST(4)
        g.add_edge(0,1,10)
        g.add_edge(0,2,6)
        g.add_edge(0,3,5)
        g.add_edge(1,3,15)
        g.add_edge(2,3,4)
        e1, c1 = g.prim_mst()
        e2, c2 = g.kruskal_mst()
        self.assertAlmostEqual(c1, c2, places=6)
        self.assertEqual(len(e1), 3)
        self.assertEqual(len(e2), 3)

    def test_connected_vs_full_cost(self):
        g = GraphMST(3)
        g.add_edge(0,1,5)
        g.add_edge(1,2,7)
        g.add_edge(0,2,20)
        _, c_p = g.prim_mst()
        _, c_k = g.kruskal_mst()
        self.assertEqual(c_p, c_k)
        self.assertLess(c_k, g.full_network_cost())

    def test_not_connected(self):
        g = GraphMST(4)
        g.add_edge(0,1,1)
        g.add_edge(2,3,2)
        e1, c1 = g.prim_mst()
        e2, c2 = g.kruskal_mst()
        self.assertTrue(c1 == float('inf') or c2 == float('inf'))

if __name__ == "__main__":
    unittest.main()
