from bfs import Graph, Vertex
import unittest

class SSP_Test(unittest.TestCase):
    def test_bfs_ssp(self):
        graph = Graph()
        a = Vertex(1)
        b = Vertex(2)
        c = Vertex(3)
        d = Vertex(4)
        e = Vertex(5)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_vertex(c)
        graph.add_vertex(d)
        graph.add_vertex(e)
        graph.add_edge(a, b)
        graph.add_edge(a, d)
        graph.add_edge(b, c)
        graph.add_edge(b, e)
        graph.add_edge(c, e)
        assert graph.bfs(a, e) == [1,2,5]