# Overview of Depth-First Search Algorithm:

Previously, we learned how to check the connectivity between two vertices with the “disjoint set” data structure. Now, let's switch gears and consider: Given a graph, how can we find all of its vertices, and how can we find all paths between two vertices?

The depth-first search algorithm is ideal in solving these kinds of problems because it can explore all paths from the start vertex to all other vertices. Let's start by considering an example. In Figure 7, there are five vertices [A, C, D, B, E]. Given two vertices A and B, there are two paths between them. One path is [A, C, D, B], and the other is [A, E, B].

![image](https://user-images.githubusercontent.com/35987583/178164958-95397d66-6f72-473f-a7c7-a8c4ffcb4d87.png)


In Graph theory, the depth-first search algorithm (abbreviated as DFS) is mainly used to:

1. Traverse all vertices in a “graph”;
2. Traverse all paths between any two vertices in a “graph”.




# DFS:

- We will use Stack to Implement and travel to all the vertices

<img width="880" alt="image" src="https://user-images.githubusercontent.com/35987583/178165280-b58330e9-f345-4399-91cf-3dd6c0049340.png">



# Traversing all paths between two vertices (A to E) Using DFS:
<img width="846" alt="image" src="https://user-images.githubusercontent.com/35987583/178165426-8b88c6d1-b053-4fe6-b1ea-53935345646c.png">

<img width="841" alt="image" src="https://user-images.githubusercontent.com/35987583/178165466-3f49adef-ec8a-4655-927a-dc79c298dccd.png">
<img width="835" alt="image" src="https://user-images.githubusercontent.com/35987583/178165474-ebb18187-8aab-4151-8d0b-085c0a0b46ed.png">
