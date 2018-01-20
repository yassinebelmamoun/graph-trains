from exception.graph_exception import GraphError, NodeError

class Graph:
    """
        The representation of a graph with a string is:
            string_graph = 'AB5, AC2, BC3, BD1, CD3, DA5'

        We represent a graph with a dictionary:
        > railroad = Graph()
        > railroad.build(string_graph)
        > railroad.graph

        [OUTPUT] >> {
                        'A': {'B': 5, 'C': 2}
                        'B': {'C': 3, 'D': 1}
                        'C': {'D': 3}
                        'D': {'A': 5}
                    }

        1 - Node:
            A node is represented by ONE letter (A, B, ..., Z) and is called "station"

        2 - Distance between two Nodes:
            The distance between two nodes A and B is an integer.
            > graph.get_distance(departure='A', arrival='B')

        3 - Neighbors:
            The neighbors of the node A are represented by a list of nodes.
            > graph.get_neighbors('A')

        4 - Route distance:
            The distance of a route is the sum of the distance between the nodes
            > graph.get_route_distance('ABC') = graph.get_distance('A', 'B') + graph.get_distance('B', 'C')

        5 - Build of a graph:
            The following method are used to build a graph: 
                - build
                - add_node
                - clean_string_graph
                - parse_node
                - check_node_station
                - check_node_distance
            A graph will be represented by a description. Each key is a node and its value is a dictionary:
            > 'A': {'B': 5, 'C': 2}
            The node/key A is connected to B and C with a weight of 5 and 2 respectivily.

        6 - Graph exploration:
            We explore the graph depth by depth starting from a departure station.
            We limit the max_depth in case we find a cycle (i.e. ABCDA) which will lead to infinite number of routes ABCDABCDABCD
            The following methods are used:
                - generate_all_routes_from_station(departure, max_depth):
                    "departure" is the departure station.
                    "max_depth" is the maximum depth for the exploration
                - create_deeper_routes(routes, max_depth): Recursive function
                - create_deeper_route(route)

        7 - Graph sum of edges' weight:
                Due to the possibility of the existence of cycles, we can proove mathematically than the distance of a cycle is less than the sum of the edges.
            
    """
    
    def __init__(self):
        self.graph = {}
        self.sum_edges_weight = 0
        

    def __repr__(self):
        return str(self.graph)


    def visualise(self):
        for departure, arrival_duration_dict in self.graph.items():
            print('\n*** The distance between the station {} and:'.format(departure))
            for arrival, duration in arrival_duration_dict.items(): 
                print('\t - the station {} is: {} units'.format(arrival, duration))


    def build(self, string_graph):
        for node in self.clean_string_graph(string_graph).split(): self.add_node(node)
    

    def get_neighbors(self, departure):
        return self.graph[departure].keys() if departure in self.graph else []


    def get_distance(self, departure, arrival):
        if departure in self.graph and arrival in self.graph[departure]:
            return self.graph[departure][arrival]
        raise GraphError('The connexion from {} to {} does not exist'.format(departure, arrival))


    def get_route_distance(self, route):
        route = ''.join([c.upper() if c.isalnum() else "" for c in route])
        return sum([self.get_distance(departure=route[i],arrival=route[i+1]) for i in range(len(route)-1)])
    
    
    def create_deeper_route(self, route):
        """
            Starting from a route, i.e. 'ABC'
            We explore all the possible routes starting from the last station 'C'
            If 'B', 'F' and 'L' are neighbors of 'A'.
            The output will be ['ABCF', 'ABCL', 'ABCA'].
        """
        last_station = route[-1]
        neighbors = [neighbor for neighbor in self.get_neighbors(last_station)]
    
        if neighbors:
            return [route + neighbor for neighbor in neighbors]
        else:
            return []


    def create_deeper_routes(self, routes, max_depth):
        """
            Recursive function for exploring deeper routes
            For each route in routes: We create deeper routes
            We concatenate all the new (deeper) routes with the initial routes and we continue.
        """

        new_routes = []
        for route in routes:
            new_routes += self.create_deeper_route(route)

        if new_routes and max_depth > 0:
            return routes + self.create_deeper_routes(new_routes, max_depth=max_depth-1)
        else:
            return routes 


    def generate_all_routes_from_station(self, departure, max_depth):
        """
            Explore all the routes starting from departure station with a maximum depth of 'max_depth'
        """
        return self.create_deeper_routes([departure], max_depth)


    def add_node(self, string_graph):
        """
        Parse node into departure, arrival and distance
        """

        departure, arrival, distance = self.parse_node(string_graph)
        if not(departure in self.graph): self.graph[departure] = {}
        self.graph[departure][arrival] = distance
        self.sum_edges_weight += distance


    @classmethod
    def parse_node(cls, string_node):
        """
            Check the length of the node (at least 3 characters):
                - First character(Departure): ONE alpha
                - Second character(Arrival): ONE alpha
                - The rest of the string are numeric characters
        """
        
        if not(len(string_node) >= 3):
            raise NodeError('The following node  {} contains {} characters.\n \
                The Node should contain exactly 3 characters.'.format(string_node, len(string_node)))

        departure = cls.check_node_station(station_type = 'Departure',\
                                            station = string_node[0],\
                                            string_node = string_node)
        arrival = cls.check_node_station(station_type = 'Arrival',\
                                            station = string_node[1],\
                                            string_node = string_node)
        if departure == arrival: raise NodeError('The arrival and departure stations must be different in the node {}'.format(string_node))
        distance = cls.check_node_distance(string_node[2:], string_node)

        return (departure, arrival, distance)


    @staticmethod
    def check_node_station(station_type, station, string_node):
        if not(station.isalpha()):
            raise NodeError('The {} value {} is not in the right format in the following node "{}" '.format(station_type, station, string_node))
        return station


    @staticmethod
    def check_node_distance(distance, string_node):
        try:
            distance = int(distance)
        except ValueError:
            raise NodeError('The Distance value {} is not in the right format in the following node {}.'.format(str(distance), string_node))
        else:
            return distance


    @staticmethod
    def clean_string_graph(string_graph):
        """
            Clean the string:
                - Remove not(alphanumeric) character and replace by whitespace
                - Replace lowercase character by uppercase character
        """
        if not(isinstance(string_graph, str)): raise GraphError('The graph must be a string.\n i.e. "AB5, AC2, BC3, BD1, CD3, DA5"')    
        return ''.join([c.upper() if c.isalnum() else " " for c in string_graph])

