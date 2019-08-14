# import challenge1
from tutorial import Vertex, Graph
import unittest

class Vertex_Tests(unittest.TestCase):
    def test_add_vertex(self):
        test_vertex = Vertex(1)
        assert test_vertex.id == 1
        assert test_vertex.neighbors == {}
    
    def test_add_neighbors_weighted(self):
        test_vertex = Vertex(1)
        test_vertex.add_neighbor(2, 1)
        assert len(test_vertex.neighbors) == 1
        assert 2 in test_vertex.neighbors.keys()
        assert 1 in test_vertex.neighbors.values()

    # def test_get_neighbors(self):
    #     test_vertex = Vertex(1)
    #     test_vertex.add_neighbor(2, 1)
    #     assert 2 in test_vertex.get_neighbors()
    
    def test_get_id(self):
        test_vertex = Vertex(1)
        assert 1 == test_vertex.get_id()

    def test_get_edge_weight(self):
        test_vertex = Vertex(1)
        test_vertex.add_neighbor(2, 1)
        assert test_vertex.get_edge_weight(2) == 1

class Graph_Tests(unittest.TestCase):
    def test_init(self):
        test_graph = Graph()
        assert test_graph.vert_dict == {}
        assert test_graph.num_vertices == 0
        # assert test_graph.edge_list == []
        
    def test_add_vertex(self):
        test_graph = Graph()
        test_graph.add_vertex(1)
        assert test_graph.vert_dict[1]
        assert test_graph.num_vertices == 1
    
    def test_get_vertex(self):
        test_graph = Graph()
        test_graph.add_vertex(1)
        assert test_graph.get_vertex(1)
    
    def test_add_edge(self):
        test_graph = Graph()
        test_graph.add_vertex(1)
        test_graph.add_vertex(2)
        test_graph.add_edge(1, 2)
        test_vert1 = test_graph.vert_dict[1]
        test_vert2 = test_graph.vert_dict[2]
        assert test_vert1.get_id() == 1
        assert test_vert2.get_id() == 2
        assert test_vert2 in test_vert1.neighbors
        assert test_vert1 in test_vert2.neighbors

    
    # def test_get_vertices(self):
    #     test_graph = Graph()
    #     test_graph.add_vertex(1)
    #     test_graph.add_vertex(2)
    #     assert 1 in test_graph.get_vertices()
    #     assert 2 in test_graph.get_vertices()

if __name__ == '__main__':
    unittest.main()
