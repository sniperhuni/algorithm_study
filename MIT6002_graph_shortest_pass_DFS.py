from MIT6002_graph_classes import *

def buildCityGraph(graphType):

    '''Create graphType object'''
    g = graphType()

    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                    'Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))

    '''This is a study. Create a hard corded graph'''
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))

    return g

def printPath(path):
    result = ''

    for i in range(len(path)):

        result = result + str(path[i])

        if i != len(path) -1:
            result = result + '->'

    return result

'''
Depth First Search
'''
def DFS(graph, start, end, path, shortest, toPrint=False):
    '''
    Assume that a graph is a digraph
    '''

    '''The first node of the path is the start node'''
    path = path + [start]

    if toPrint:
        print('Current DFS path: ', printPath(path))

    '''Get out of the function with a path'''
    if start == end:
        return path

    '''Search recursively in depth'''
    for node in graph.childrenOf(start):
        '''
        To avoid revisiting the same node
        '''
        if node not in path:
            '''We do not have a solution yet or our solution is not optimal'''
            if (shortest == None) or (len(path) < len(shortest)):
                newPath = DFS(graph, node, end, path, shortest, toPrint)

                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already Visited', node)

    return shortest

'''Wrapper Function'''
def shortestPath(graph, start, end, toPrint = False):

    return DFS(graph, start, end, [], None, toPrint)


def testSP(source, destination):

    g = buildCityGraph(Digraph)

    sp = shortestPath(g, g.getNode(source), g.getNode(destination),
                    toPrint = True)

    if sp != None:

        print('Shortest path from ',source, 'to ', destination, 'is ',
                printPath(sp))
    else:
        print('There is not path from ', source, 'to ', destination)

'''
Breadth first search
Search from path with length=1 to the longest path

We do not need shortest parameter in DFS
'''
def BFS(graph, start, end, toPrint=False):

    '''
    input: Digraph object

    return: a shortest path from start to end in graph
    '''

    '''start with a start node'''
    initPath = [start]
    # This queue save lists of path
    # e.g. [[A], [A,B], [A,C], [A,B,D] ...]
    pathQueue = [initPath]

    while len(pathQueue) !=0:

        # Get and remove the oldest element in pathQueue
        if toPrint:
            print('Queue:', len(pathQueue))
            for p in pathQueue:
                print(printPath(p))

        currentPath = pathQueue.pop(0)

        if toPrint:
            print('Current BFS path: ', printPath(currentPath))
            print()

        # the last node of the current path
        lastNode = currentPath[-1]

        # We found the solution
        if lastNode == end:
            return currentPath

        '''
        Before the current node is replaced by the new value,
        add next candidate paths
        '''
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in currentPath:
                newPath = currentPath + [nextNode]
                pathQueue.append(newPath)

    return None

def shortestPath_BFS(graph, start, end, toPrint = False):
    return BFS(graph, start, end, toPrint)

def testSP_BFS(source, destination):

    g = buildCityGraph(Digraph)

    sp = shortestPath_BFS(g, g.getNode(source), g.getNode(destination),
                    toPrint = True)

    if sp != None:

        print('Shortest path from ',source, 'to ', destination, 'is ',
                printPath(sp))
    else:
        print('There is not path from ', source, 'to ', destination)

g = buildCityGraph(Digraph)
print(g)
print('--------------------')

# No path
#testSP('Chicago', 'Boston')
print('A solution of DFS')
testSP('Boston', 'Phoenix')
print('--------------------')

print('A solution of BFS')
testSP_BFS('Boston', 'Phoenix')
