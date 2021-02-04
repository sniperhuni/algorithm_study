'''
This is a code from the lecture
'''

# Node class of graph
class Node:
    def __init__(self, name):
        '''
        Assumes that a name is string
        '''
        self.name = name

    def getName(self):
        return self.name

    # This will decide the way to print a node name
    def __str__(self):
        return self.name

# Edge of graph
class Edge:
    def __init__(self, src, dest):
        '''
        src: source Node, Node class
        dest: destination Node, Node class
        '''
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() +' -> ' + self.dest.getName()

class Digraph:
    '''
    Edges are a dict mapping each node to a list its children
    '''

    def __init__(self):
        '''
        key : a source
        value : a list of destinations
        '''
        self.edges = {}

    def addNode(self, node):

        if node in self.edges:
            raise ValueError('Existing Node')

        else:
            # Create a node not having children & edges
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()

        ''' There should exist nodes of edges that we want to add to '''
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')

        self.edges[src].append(dest)

    def childrenOf(self, node):
        '''return a list of children'''
        return self.edges[node]

    '''Check if the graph has the node'''
    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for node in self.edges:

            if node.getName() == name:
                return node
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:

            for dest in self.edges[src]:

                result = result + src.getName() + '->' \
                            + dest.getName() + '\n'

        return result[:-1] # remove tha final newline

'''Bidirectional Graph'''
def Graph(Digraph):

    '''Method Overriding'''
    def addEdge(self, edge):

        Digraph.addEdge(self, edge)

        reverse_edge = Edge(edge.getDestination(), edge.getSource())

        Digraph.addEdge(self, reverse_edge)

'''
Test classes

toronto = Node('Toronto')
montreal = Node('Montreal')
vancouver = Node('Vancouver')

edge1 = Edge(vancouver, toronto)
edge2 = Edge(toronto, montreal)

print(toronto)
print(montreal)

print(edge1)

digraph = Digraph()

digraph.addNode(toronto)
digraph.addNode(montreal)
digraph.addNode(vancouver)
digraph.addEdge(edge1)
digraph.addEdge(edge2)

#print(digraph.edges)
print(digraph.childrenOf(toronto))
print(digraph.hasNode(toronto))
#print(digraph.getNode('vancouver'))
print(digraph)
'''
