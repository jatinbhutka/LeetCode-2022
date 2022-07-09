## Introduction:

Graph is probably the data structure that has the closest resemblance to our daily life. There are many types of graphs describing the relationships in real life. For instance, our friend circle is a huge “graph”.


![image](https://user-images.githubusercontent.com/35987583/178124925-987a9166-2f77-4f38-8b15-7970626e9102.png)
* Figure 1 *

In Figure 1 above, we can see that person G, B, and E are all direct friends of A, while person C, D, and F are indirect friends of A. This example is a social graph of friendship. So, what is the “graph” data structure?


### Types of “graphs”:
There are many types of “graphs”. In this Explore Card, we will introduce three types of graphs: 

- Undirected graphs
- Directed graphs, and 
- Weighted graphs.


#### A. Undirected graphs
The edges between any two vertices in an “undirected graph” do not have a direction, indicating a two-way relationship.

Figure 1 is an example of an undirected graph.

#### B. Directed graphs
The edges between any two vertices in a “directed graph” graph are directional.

![image](https://user-images.githubusercontent.com/35987583/178124984-d8ff61df-4a4a-4282-bbe4-26a2f19018bd.png)

Figure 2 is an example of a directed graph.

#### C. Weighted graphs

Each edge in a “weighted graph” has an associated weight. The weight can be of any metric, such as time, distance, size, etc. The most commonly seen “weighted map” in our daily life might be a **city map**. In Figure 3, each edge is marked with the distance, which can be regarded as the weight of that edge.

![image](https://user-images.githubusercontent.com/35987583/178124995-66273e84-53f0-41fd-b951-8b4741d247fe.png)


### The Definition of “graph” and Terminologies


“Graph” is a non-linear data structure consisting of vertices and edges. There are a lot of terminologies to describe a graph. If you encounter an unfamiliar term in the following Explore Card, you may look up the definition below.

- **Vertex**: In Figure 1, nodes such as A, B, and C are called vertices of the graph.
- **Edge**:  The connection between two vertices are the edges of the graph. 
- **Path**: The sequence of vertices to go through from one vertex to another. Path from A to C is [A, B, C], or [A, G, B, C], or [A, E, F, D, B, C]. **Note**: There can be multiple paths between two vertices.
- **Path Length:** The number of edges in a path. In Figure 1, the path lengths from person A to C are 2, 3, and 5, respectively.
- **Cycle**: a path where the starting point and endpoint are the same vertex. In Figure 1, [A, B, D, F, E] forms a cycle. Similarly, [A, G, B] forms another cycle.
- **Degree of a Vertex**: the term “degree” applies to unweighted graphs. The degree of a vertex is the number of edges connecting the vertex. In Figure 1, the degree of vertex A is 3 because three edges are connecting it.
- **In-Degree**: “in-degree” is a concept in directed graphs. If the in-degree of a vertex is d, there are d directional edges incident to the vertex. In Figure 2, A’s indegree is 1, i.e., the edge from F to A.
- **Out-Degree**: “out-degree” is a concept in directed graphs. If the out-degree of a vertex is d, there are d edges incident from the vertex. In Figure 2, A’s outdegree is 3, i,e, the edges A to B, A to C, and A to G.


- **Negative Weight Cycle**: In a “weighted graph”, if the sum of the weights of all edges of a cycle is a negative value, it is a negative weight cycle. In Figure 4, the sum of weights is -3.
![image](https://user-images.githubusercontent.com/35987583/178125608-7a5af745-0d16-468b-8813-6df40e0ff96f.png)

- **Connectivity**: if there exists at least one path between two vertices, these two vertices are connected. In Figure 1, A and C are connected because there is at least one path connecting them.
