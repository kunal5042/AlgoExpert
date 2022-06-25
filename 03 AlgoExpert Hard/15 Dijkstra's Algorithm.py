import unittest
from typing import List
# Given: no loops
# Adjacency List Representation: usually represented as a singly linked list
# But here, we have a list, which contains multiple other lists where each index in our main list
# will have another list that gives us all of the edges for that corresponding vertex

# length of the adjacency list = number of vertices in the graph

# One way to find the shortest path is to consider every single path and then select the shortest one
# And this can be done in a depth first search way
# But, the problem is this is really inefficient

# Building on this, Dijkstra's Algorithm keeps track of what we have already seen
# to reduce this time complexity
'''
O (v^2 + e) time | O(v) space: where v is the number of vertices and e is the number of edges
'''
def dijkstrasAlgorithm(start: int, edges: List[int]):
    number_of_vertices = len(edges)

    min_distances = [float('inf') for _ in range(number_of_vertices)]
    # The node that we are starting at is zero distance away from itself
    # so it's min distance = 0
    min_distances[start] = 0

    # keep track of visited nodes
    visited = set()

    # once we have visited all the nodes we would know for sure that we have found 
    # minimum distance to all nodes
    # and we can stop, hence this condition
    while len(visited) != number_of_vertices:
        # get_vertex_with_min_distance will return two things
        # a vertex and current minimum distance to that vertex
        # this vertex will be the vertex which is closest to the start and yet not have been visited
        # we will explore this vertex
        # and mark it as visited after exploring
        vertex, current_min_distance = get_vertex_with_min_distance(min_distances, visited)

        # this means we have found a node which is not connected to the start
        # and we can safely break the loop
        # as any nodes that have been closer to start than this node would have already been found
        if current_min_distance == float('inf'):
            min_distances[vertex] = -1
            break

        # mark  this node as visited
        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distance_to_destination = edge

            if destination in visited:
                # there is no need to look at it
                # because there is no better path to this node 
                # coz, if there was we would have already found it before when we visited it
                continue

            # not yet visited
            # the bread and butter
            new_path_distance = current_min_distance + distance_to_destination
            current_destination_distance = min_distances[destination]

            if new_path_distance < current_destination_distance:
                min_distances[destination] = new_path_distance

    # replace infinite values with -1
    return list(map(lambda x: -1 if x == float('inf') else x, min_distances))

# helper function to find the unvisited vertex/node with minimum distance from the starting node
def get_vertex_with_min_distance(distances: List[int], visited: set):
    # to find the minimum distance from the distances array
    current_min_distance = float('inf')
    vertex = None

    for vertex_idx, distance in enumerate(distances):
        # if a vertex has been visited, we can safely skip this vertex
        if vertex_idx in visited:
            continue

        # if current vertex has smaller distance the minimum distance
        # update the resultant vertex as the current vertex
        if distance <= current_min_distance:
            vertex = vertex_idx
            current_min_distance = distance

    return vertex, current_min_distance



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        start = 0
        edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
        expected = [0, 7, 13, 27, 10, -1]
        actual = dijkstrasAlgorithm(start, edges)
        self.assertEqual(actual, expected)
        print('Test Case: Passed')
        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa