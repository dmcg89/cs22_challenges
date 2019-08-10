# cs22_challenges
## Challenge 1
- Implement the Graph ADT with an adjacency list
- Implement code to read in a graph from a text file to create an instance of the Graph ADT and use its methods.
- Input: A graph file (can contain a directed or undirected graph with or without weights) python3 challenge_1.py graph_data.txt

G<br/>
1,2,3,4<br/>
(1,2,10)<br/>
(1,4,5)<br/>
(2,3,5)<br/>
(2,4,7)<br/>

## Challenge 2
Create a Challenge_2 folder in your challenge repository. Copy any code you want to re-use from Challenge 1 to that folder before modifying<br/><br/>

Update your Graph ADT code to use Breadth-first search to compute the shortest path between two provided vertices in your graph.<br/><br/>

Input: A graph file (containing an undirected, unweighted graph), a from_vertex and a to_vertex.<br/><br/>

python3 challenge_2.py graph_data.txt 1 5<br/><br/>

G<br/>
1,2,3,4,5<br/>
(1,2)<br/>
(1,4)<br/>
(2,3)<br/>
(2,4)<br/>
(2,5)<br/>
(3,5)<br/><br/>
Output: The vertices in a shortest path from from_vertex to to_vertex and the number of edges in that path.

Vertices in shortest path: 1,2,5
Number of edges in shortest path: 2
## Challenge 3
## Challenge 4
