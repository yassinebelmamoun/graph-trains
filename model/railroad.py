from model.graph import Graph
from exception.railroad_exception import RailroadError 


class Railroad(Graph):
    """
        Vocabulary:
            1. A route/trip is a string (i.e 'ABC') represention:
                - Departure from station A
                - Stop at station B
                - Arrival (last stop) at station C
            2. We define the number of stops of a trip as the total number of stations visited minus one:
                - For the trip 'ABC', the number of stops is 2 

        Raildroad is a graph improved to reply to the following questions:
            1. Find the number of trips with a maximum number of stops between two stations.
            2. Count the number of trips with a maximum number of stops between two stations.
            3. Count the exact number of trips with an exact number of stops between two stations.
            4. Find the shortest route between two stations.
            5. Find the routes between two stations.

    """


    def get_trips_MaxStop(self, departure, arrival, max_stop):
        # Return a list of all the trips from "departure" to "arrival" with a maximum of stops equal to max_stop
        return [route for route in self.generate_all_routes_from_station(departure, max_depth=max_stop) \
                    if len(route) > 1 and len(route) - 1 <= max_stop and route and route[-1] == arrival]
    

    def get_count_trips_MaxStop(self, departure, arrival, max_stop):
        # Return the count of trips from "departure" to "arrival" with a maximum of stops equal to max_stop 
        return len(self.get_trips_MaxStop(departure, arrival, max_stop))


    def get_trips_ExactCountStop(self, departure, arrival, count_stop):
        # Return a list of all the trips from "departure" to "arrival" with a number of stops equal to coun_stop
        return [route for route in self.generate_all_routes_from_station(departure, max_depth=count_stop) \
                    if len(route) > 1 and len(route) - 1 == count_stop and route and route[-1] == arrival]


    def get_count_trips_ExactCountStop(self, departure, arrival, count_stop):
        # Return the count of trips from "departure" to "arrival" with a number of stops equal to count_stop 
        return len(self.get_trips_ExactCountStop(departure, arrival, count_stop))
    

    def get_length_shortest_route(self, departure, arrival):
        # The shortest distance from departure to arrival in terms of distance.
        # Testing with small values of max_depth is faster. (This is related to the cycles issues)
        max_depth, routes = 3, []
        while max_depth <= self.sum_edges_weight and not(routes):
            routes = self.get_trips_MaxStop(departure, arrival, max_stop = max_depth)
            max_depth = max_depth * 2 if max_depth <= self.sum_edges_weight else self.sum_edges_weight
        return min([self.get_route_distance(route) for route in routes])

    
    def get_count_routes_MaxDistance(self, departure, arrival, max_distance):
       return len([route for route in self.get_trips_MaxStop(departure, arrival, max_stop=max_distance) \
                    if self.get_route_distance(route) < max_distance])
