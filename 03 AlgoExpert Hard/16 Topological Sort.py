import unittest
'''
Application:
    - Instruction scheduling
    - Ordering of formula cell evaluation when recomputing formula values in spreadsheets
    - Logic synthesis
    - Determining the order of compilation tasks to perform in make files
    - Data serialization
    - Resolving symbol dependencies

Directed Graph Data Structure
Linear ordering of the vertices of the graph, so long as every directed edge we have from X to Y
The node X comes before node Y (happens-before relation)

The idea here is to represent the jobs and their dependenices as a directed graph.
Where nodes are the jobs and the direction is based on the dependencies data structure.

Main Logic:
A:
    We start at a node
    We then, check all it's children nodes for the following condition
    if this child has any unsatisfied dependency and this child has not yet been visited?
        yes: start node = current node, branch to A:
    else:
        no : add this node to the result, and mark it visited
    Once, all the children are checked
    We add this start node to the result

This is the depth-first-search way.

What is the flaw in this approach?
Cycle

If we have a cycle, no valid order exists
So, we have to keep track of processing nodes in order to make sure we don't get stuck in a cycle.

Using the knowledge above, we can solve this question in two ways
'''

# O(j + d) Time and O(j + d) Space: where j is the number of jobs and d is the number of dependencies
def topologicalSort(jobs, deps):
    job_graph = create_job_graph(jobs, deps)
    return get_ordered_jobs(job_graph)

def create_job_graph(jobs, deps):
    # populate the graph
    graph = JobGraph(jobs)
    
    # make the graph directed by added dependencies
    for prerequisite, job in deps:
        # adding edges
        graph.add_prerequisite(job, prerequisite)
    return graph

def get_ordered_jobs(graph):
    ordered_jobs = list()
    
    # get all the nodes
    nodes = graph.nodes
    
    # process all the nodes one by one
    while len(nodes):
        node = nodes.pop()
        contains_cycle = depth_first_traverse(node, ordered_jobs)
        
        # if a cycle is present, no valid order exist, return an empty list
        if contains_cycle is True:
            return list()
    return ordered_jobs

def depth_first_traverse(node, ordered_jobs):
    # we don't have to visit the visited nodes, coz they have been processed before
    if node.visited is True:
        return False
    
    # if we reached a node that was being processed in the recursion stack
    # we found a cycle and we can stop
    if node.state == "In Processing":
        return True

    # mark the current node as being processed in the recursion stack
    node.state = "In Processing"
    
    # now visit all of it's prerequisites
    # and follow the logic discussed already
    for prerequisite_node in node.prerequisites:
        contains_cycle = depth_first_traverse(prerequisite_node, ordered_jobs)
        if contains_cycle is True:
            return True

    # after processing, mark this node visited
    node.visited = True
    # update the state
    node.state   = "Not In Processing"
    # as this node now, doesn't have any unmet dependencies
    # add it to the list of ordered_jobs
    ordered_jobs.append(node.job)
    return False
    
class JobGraph:
    def __init__(self, jobs):
        self.nodes = list()
        self.graph = dict()
        
        # populate the graph
        for job in jobs:
            self.add_node(job)

    def add_node(self, job):
        # this graph hashmap is used for O(1) look up of jobs/nodes
        # and JobNode class stores important information about each job
        self.graph[job] = JobNode(job)
        
        # this nodes list stores all the nodes of this graph as a JobNode object
        self.nodes.append(self.graph[job])
        
    def add_prerequisite(self, job, prerequisite):
        # given a job and it's dependency/prerequisite
        # find the node which corresponds to this job in our graph
        job_node = self.get_node(job)        
        
        # find the node which corresponds to this prerequisite job in our graph
        prerequisite_node = self.get_node(prerequisite)
        
        # add this prerequisite node to the prerequisites list of this job
        job_node.prerequisites.append(prerequisite_node)

    # returns the JobNode object in O(1) time
    def get_node(self, job):
        if job not in self.graph:
            self.add_node(job)
        return self.graph[job]

class JobNode:
    def __init__(self, job):
        self.job = job
        # this list stores all the dependencies/ prerequisites of each job/node
        self.prerequisites = list()
        
        # as we process each job, we will mark it as visited
        self.visited = False
        
        # this is important, we will use the information of job's state to find out
        # if our graph has a a cycle 
        self.state = "Not In Processing"

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        jobs = [1, 2, 3, 4]
        deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
        order = topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)
        print("Test Case: Passed")

# this is a helper function to check if the results produced are correct
# provided to test our algorithm
def isValidTopologicalOrder(order, jobs, deps):
    visited = {}
    for candidate in order:
        for prereq, job in deps:
            if candidate == prereq and job in visited:
                return False
        visited[candidate] = True
    for job in jobs:
        if job not in visited:
            return False
    return len(order) == len(jobs)

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa