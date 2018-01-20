import unittest
from model.railroad import Graph 
from exception import graph_exception, railroad_exception


class GraphTestCase(unittest.TestCase):

    def test_build(self):
        # Building graph:
        graph = Graph()
        self.assertRaises(graph_exception.GraphError, graph.build, 3)

        graph = Graph()
        self.assertRaises(graph_exception.NodeError, graph.build, 'AA BB CC DD')

        graph = Graph()
        graph.build('AB5')
        self.assertEqual(graph.graph,{'A': {'B':5}})
    
    def test_get_neighbors(self):
        graph = Graph()
        graph.build('AB3 AC2 BC4')
        self.assertEqual(list(graph.get_neighbors('A')), ['B', 'C'])
    
    def test_clean_string_graph(self):
        graph = Graph()
        self.assertEqual(graph.clean_string_graph('AB4-CD2-JE20'), 'AB4 CD2 JE20')