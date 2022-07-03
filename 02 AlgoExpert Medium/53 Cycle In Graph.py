# https://www.algoexpert.io/questions/cycle-in-graph
# Graphs

'''Solution - 1'''
'''O(v + e) time | O(v) space - where v is the number of vertices and e is the number of edges in the graph'''

def cycleInGraph(edges):
    num_nodes          = len(edges)
    visited            = [False for _ in range(num_nodes)]
    currently_in_stack = [False for _ in range(num_nodes)]

    for node in range(num_nodes):
        # if this node has already been visited, we can continue
        if visited[node] is True: continue

        # DFS function on node
        contains_cycle = is_node_in_cycle(edges, node, visited, currently_in_stack)

        # if the above function found a cycle, we return True
        if contains_cycle is True: return True

    return False


def is_node_in_cycle(edges, node, visited, currently_in_stack):
    visited[node]            = True
    currently_in_stack[node] = True

    # neighbours of the current node
    neighbours = edges[node]
    for neighbour in neighbours:
        if visited[neighbour] is False:
            contains_cycle = is_node_in_cycle(edges, neighbour, visited, currently_in_stack)
            # if above call returns True, means we did find a cycle
            if contains_cycle is True: return True
                
        # but if that's not the case, and the neighbour has already been visited
        # we check if the neighbour is in the recursion stack
        # if it is, means we found a back edge
        # and we have a cycle
        elif currently_in_stack[neighbour] is True:
                return True

    # take this node out of the recursion stack
    currently_in_stack[node] = False
    return False


'''Solution - 2'''
'''O(v + e) time | O(v) space - where v is the number of vertices and e is the number of edges in the graph'''
# WHITE - not visited
# GREY  - currently in stack
# BLACK - visited and not in stack
WHITE, GREY, BLACK = 0, 1, 2

def cycleInGraph(edges):
    num_nodes          = len(edges)
    colors             = [WHITE for _ in range(num_nodes)]

    for node in range(num_nodes):
        # means we have already visited
        if colors[node] != WHITE: continue

        # check if the current node has a cycle
        contains_cycle = traverse_and_color_nodes(node, edges, colors)
        if contains_cycle is True: return True


    return False

def traverse_and_color_nodes(node, edges, colors):
    colors[node] = GREY

    neighbours = edges[node]

    for neighbour in neighbours:
        neighbour_color = colors[neighbour]

        # if this is true, we found a back edge
        if neighbour_color == GREY: return True

        # has been visited
        if neighbour_color != WHITE: continue

        # means neighbour color is WHITE, and has not been visited
        # so visit
        contains_cycle = traverse_and_color_nodes(neighbour, edges, colors)
        if contains_cycle is True: return True


    colors[node] = BLACK
    return False
        


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
        expected = True
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''