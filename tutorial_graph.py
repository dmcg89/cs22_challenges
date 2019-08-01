#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex, visited = False, distance = 9999):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}
        # self.visited = visited
        # self.distance = distance
        # self.path = []

    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        #  check if vertex is already a neighbor
        if vertex in self.neighbors:
            raise ValueError('Item exists in neighbor: {}'.format(vertex))
        #  if not, add vertex to neighbors and assign weight.
        else:
            self.neighbors[vertex] = weight
            # return self.neighbors


    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        #  return the neighbors
        return self.neighbors.keys()

    def get_id(self):
        """return the id of this vertex"""
        return self.id

    def get_edge_weight(self, to_vertex):
        """return the weight of this edge"""
        #  return the weight of the edge from this vertex to the given vertex.
        return self.neighbors[to_vertex]


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vert_dict = {}
        self.num_vertices = 0
        self.edge_list = []

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        #  increment the number of vertices
        self.num_vertices += 1
        #  create a new vertex
        new_vertex = Vertex(key)
        #  add the new vertex to the vertex list
        self.vert_dict[key] = new_vertex
        #  return the new vertex
        # return self

    def get_vertex(self, key):
        """return the vertex if it exists"""
        #  return the vertex if it is in the graph
        if key in self.vert_dict:
            return self.vert_dict[key]
        raise ValueError('Vertex not found: {}'.format(key))

    def add_edge(self, key1, key2, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        if key1 not in self.vert_dict or key2 not in self.vert_dict:
            raise ValueError('One of the vertices not in graph')
            # if both vertices in the graph, add the
            # edge by making t a neighbor of f
        else:
            # and using the addNeighbor method of the Vertex class.
            # Hint: the vertex f is stored in self.vertList[f].
            self.vert_dict[key1].add_neighbor(self.vert_dict[key2], cost)
            self.vert_dict[key2].add_neighbor(self.vert_dict[key1], cost)

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_dict.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())


# Driver code

if __name__ == "__main__":
    
    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")
    g.add_vertex("Friend 4")
    g.add_vertex("Friend 5")
    g.add_vertex("Friend 6")
    g.add_vertex("Friend 7")
    g.add_vertex("Friend 8")
    g.add_vertex("Friend 9")
    g.add_vertex("Friend 10")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")
    g.add_edge("Friend 3", "Friend 4")
    g.add_edge("Friend 4", "Friend 5")
    g.add_edge("Friend 5", "Friend 6")
    g.add_edge("Friend 7", "Friend 8")
    g.add_edge("Friend 8", "Friend 9")
    g.add_edge("Friend 9", "Friend 10")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.get_id(), w.get_id()))
