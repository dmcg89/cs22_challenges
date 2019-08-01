#!python
from collections import deque

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
        # return self.neighbors.keys()
        keys = []
        for key in self.neighbors:
            keys.append(key.id)
        return keys

    def get_neighbors_ids(self):
        return self.neighbors.keys()

    def get_id(self):
        """return the id of this vertex"""
        return self.id

    def get_edge_weight(self, vertex):
        """return the weight of this edge"""
        #  return the weight of the edge from this vertex to the given vertex.
        # return self.neighbors[to_vertex]
        if vertex in self.neighbors:
            return self.neighbors[vertex]
        else:
            raise ValueError('Vertex not in Graph')


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
        self.cliques = []

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())

    def __str__(self):
      
        return str(self.vert_dict) 

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
        return new_vertex

    def get_vertex(self, key):
        """return the vertex if it exists"""
        #  return the vertex if it is in the graph
        if key in self.vert_dict:
            return self.vert_dict[key]
        else:
            raise KeyError('Vertex not found: {}'.format(key))

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
        return str(self.vert_dict.keys())
    
    def is_clique(self, start_id):
        """ Determines if a set exists around a given start_id"""
        remain_verts = []
        clique = []
        # Add start id to potential clique list
        clique.append(start_id)

        # Add all other verts to remain_vert
        for key in self.vert_dict:
            if key != start_id:
                remain_verts.append(key)
        
        for vert_id in remain_verts:
            # Get vertex object from id
            curr_vert = self.get_vertex(vert_id)

            # Returns true if each member of the clique is in curr_verts neighbors
            is_member = all(member in curr_vert.get_neighbors() for member in clique)

            # If true, append vert_id to clique
            if is_member == True:
                clique.append(vert_id)
            sorted_clique = set(sorted(clique))

            # Make sure clique is not already in list and is at least 3 verts
            if sorted_clique not in self.cliques and len(sorted_clique) > 2:
                self.subset_clique_check(sorted_clique)
        return self

    def subset_clique_check(self, clique_set):
        ''' Checks if clique being added to cliques list is a subset or a superset of a 
        preexisting clique in list'''
        # keep track of index to pop subsets when the larger set needs to be added
        index = 0

        for item in self.cliques:

            # if item to add is a subset, disregard it
            if clique_set.issubset(item):
                return

            # if item to add is a superset, pop the old subset and append superset
            elif item.issubset(clique_set):
                self.cliques.pop(index)
                self.cliques.append(clique_set)
                return self
            index += 1

        # if set to add is not a subset or superset, add it to cliques list
        self.cliques.append(clique_set)
        return self


    def search_clique(self):
        """ Iterates through all vertices in graph to search for cliques"""
        for key in self.vert_dict:
            self.is_clique(key)


    def bfs(self, vert_key, n):
        if vert_key not in self.vert_dict:
            raise ValueError('Vert not in graph')
        vert_key_list = []
        vert_key_list.append(vert_key)
        counter = 0
        while counter < n:
            neighbors = []
            for vert_key in vert_key_list:
                curr_vert = self.get_vertex(vert_key)
                neighbors.append(curr_vert.get_neighbors())
            counter += 1
        return neighbors

    def bfs2(self, from_vert, to_vert):
        queue = deque()
        shortest_path = []
        visited = {}
        if from_vert == to_vert:
            return("Vertices in shortest path: {}\n Number of edges in shortest path: {} ".format(shortest_path, num_edges))
        else:
            queue.appendleft(from_vert)
            visited[from_vert] = 0

        while queue:
            vert_id = queue.pop()
            curr_vert = self.get_vertex(vert_id)
            visited[from_vert] = curr_vert.id

            for neighbor in curr_vert.get_neighbors():
                if neighbor in visited:
                    continue
                queue.appendleft(neighbor)
                visited[neighbor] = curr_vert.id
                if curr_vert.id not in shortest_path:
                    shortest_path.append(curr_vert.id)

        
        shortest_path.append(to_vert)
        return("Vertices in shortest path: {}\n Number of edges in shortest path: {} ".format(",".join(shortest_path), len(shortest_path) -1 ))

# friend 1, friend 2, friend 3, friend 4, friend 5


    
    # while queue:
    #     source = queue.pop(0)
    #     source.visited = True
g = Graph()

# # Add your friends
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
# g.add_vertex(7)

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.add_edge(3, 4)
# g.add_edge(3, 2)
# g.add_edge(3, 4)
# g.add_edge(1, 5)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
# g.add_edge(6, 7)
# # print(bfs(g, 1, 4))
# curr_vert = g.get_vertex(6)
# print('path')
# print(curr_vert.path)
# print('here')
# for key in g.vert_dict:
#     curr_vert = g.get_vertex(key)
#     print(curr_vert.distance)
# if __name__ == "__main__":
    
#     # Challenge 1: Create the graph

#     g = Graph()

#     # Add your friends
#     g.add_vertex(1)
#     g.add_vertex(2)
#     g.add_vertex(3)
#     g.add_vertex(4)
#     # g.add_vertex("Friend 5")
#     # g.add_vertex("Friend 6")
#     # g.add_vertex("Friend 7")
#     # g.add_vertex("Friend 8")
#     # g.add_vertex("Friend 9")
#     # g.add_vertex("Friend 10")

#     # ...  add all 10 including you ...

#     # Add connections (non weighted edges for now)
#     g.add_edge(1, 2)
#     g.add_edge(2, 3)
#     g.add_edge(3, 4)
#     # g.add_edge("Friend 4", "Friend 5")
#     # g.add_edge("Friend 5", "Friend 6")
#     # g.add_edge("Friend 7", "Friend 8")
#     # g.add_edge("Friend 8", "Friend 9")
#     # g.add_edge("Friend 9", "Friend 10")

#     # Challenge 1: Output the vertices & edges
#     # Print vertices
#     print(bfs(g, 1, 4))
#     print("The vertices are: ", g.get_vertices(), "\n")

#     print("The edges are: ")
#     for v in g:
#         for w in v.get_neighbors():
#             print("( %s , %s )" % (v.get_id(), w.get_id()))

g.search_clique()
print(g.cliques)
print(g.bfs(1, 2))