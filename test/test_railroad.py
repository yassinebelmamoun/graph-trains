import unittest
from model.railroad import Railroad
from exception import graph_exception, railroad_exception


class RailroadTestCase(unittest.TestCase):
    
    def setUp(self):
        self.railroad = Railroad()
        self.railroad.build('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')

    def test_get_route_distance(self):
        # test 1:
        self.assertEqual(self.railroad.get_route_distance('A-B-C'), 9)
        # test 2:
        self.assertEqual(self.railroad.get_route_distance('A-D'), 5)
        # test 3:
        self.assertEqual(self.railroad.get_route_distance('A-D-C'), 13)
        # test 4:
        self.assertEqual(self.railroad.get_route_distance('A-E-B-C-D'), 22)
        # test 5: (Route does not exist)
        self.assertRaises(graph_exception.GraphError, self.railroad.get_route_distance, 'A-E-D')

    def test_get_count_trips_MaxStop(self):
        # test 6:
            # The number of trips starting at C and ending at C with a maximum of 3 stops.
            # In the sample data below, there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops).
        self.assertEqual(self.railroad.get_count_trips_MaxStop('C', 'C', max_stop=3), 2)

    def test_get_trips_ExactCountStop(self):
        # test 7:
            # The number of trips starting at A and ending at C with exactly 4 stops.
            # In the sample data below, there are three such trips:
            # A to C (via B,C,D); A to C (via D,C,D); and A to C (via D,E,B).
        self.assertEqual(self.railroad.get_count_trips_ExactCountStop('A', 'C', count_stop=4), 3)

    def test_get_length_shortest_route(self):
        # test 8:
            # The length of the shortest route (in terms of distance to travel) from A to C.
        self.assertEqual(self.railroad.get_length_shortest_route('A', 'C'), 9)

        # test 9:
            # The length of the shortest route (in terms of distance to travel) from B to B.
        self.assertEqual(self.railroad.get_length_shortest_route('B', 'B'), 9)

    def test_get_count_routes_MaxDistance(self):
        # test 10:
            # The number of different routes from C to C with a distance of less than 30.  In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.
        self.assertEqual(self.railroad.get_count_routes_MaxDistance('C', 'C', 30), 7)
        

