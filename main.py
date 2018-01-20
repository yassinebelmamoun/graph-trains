from model.railroad import Railroad 


if __name__ == '__main__':
    
    # Create and build the Railroad
    railroad = Railroad()
    railroad.build('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')

    # Visualise the railroad
    railroad.visualise()

    # Measure the distance of the routes:
    routes = ['A-B-C', 'A-D', 'A-D-C', 'A-E-B-C-D']
    print('\n\n*** The distance of:')
    for route in routes:
        print('\t- The route {} is {} units'.format(route, str(railroad.get_route_distance(route))))

    print('\n*** The number of trips starting at C and ending at C with a maximum of 3 stops is: {} routes'.format(railroad.get_count_trips_MaxStop('C', 'C', max_stop=3)))

    print('\n*** The number of trips starting at A and ending at C with exactly 4 stops is: {} routes'.format(railroad.get_count_trips_ExactCountStop('A', 'C', count_stop=4)))

    print('\n*** The length of the shortest route (in terms of distance to travel) from A to C is: {} units'.format(railroad.get_length_shortest_route('A', 'C')))

    print('\n*** The length of the shortest route (in terms of distance to travel) from B to B is: {} units'.format(railroad.get_length_shortest_route('B', 'B')))

    print('\n*** The number of different routes from C to C with a distance of less than 30 is: {} routes'.format(railroad.get_count_routes_MaxDistance('C', 'C', 30)))