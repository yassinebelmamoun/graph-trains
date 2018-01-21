# Railroad System - Graph Theory

I implemented a data structure based on the graph theory for managing a railroad.

A railroad is represented in this problem as a directed & weighted graph of stations/towns (i.e. "nodes") separated by a distance (i.e. "edge"). All the tracks are considered one-way in this problem.

This representation offer the railroad with a system to provide informations such as the distance along a certain route, the number of different routes between two towns, and the distance of the shortest route between two towns.


## Getting started:


#### Prerequisite:

You need to install python 3 to run this code.
No library is required.


#### Installation:

You can clone my repository:
```
git clone https://github.com/yassinebelmamoun/graph-trains
```


#### Running the tests:

The directory /test/ contains the 2 test files used for the Test Driven Development. In order to run the test, you can launch the following commands from your Terminal.
```
python3 -m unittest test.test_graph.GraphTestCase
python3 -m unittest test.test_railroad.RailroadTestCase
```


## Example of usage:

Launch Python3 in your terminal.

```
▶ python3
```

Start by importing the Railroad model:

```python
>>> from model.railroad import Railroad
```

Create and build the Railroad object:
```python
>>> railroad = Railroad()
>>> railroad.build('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')
```

Let's play with our Railroad object:
```
>>> print(railroad)
{'A': {'B': 5, 'D': 5, 'E': 7}, 'B': {'C': 4}, 'C': {'D': 8, 'E': 2}, 'D': {'C': 8, 'E': 6}, 'E': {'B': 3}}
>>> railroad.get_length_shortest_route('A', 'C')
9
>>> railroad.get_count_trips_MaxStop('C', 'C', 3)
2
```





## Structure of the code:



### Models:

The directory model/ contains the two models for the oriented graph (adjajency list) and for the raildroad.


#### Graph model:

The "Graph" model is a class representing an oriented & weighted graph.
Each node is an uppercase letter (A-Z) and each edge is a positive integer.



__1. Representation:__
  
We build a graph from a string representation of the graph.

```python
string_representation_of_graph = 'AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'
```

The graph will be represented by a dictionary (Adjacency dictionary). Each key represents a node and the value of each key is a dictionary representing the neighbors of the node (keys) and the distance to these nodes (value)
  
  Example:
  
```python
graph = Graph()
graph.build(string_representation_of_graph)
```
  
  The graph will be represented by a dictionary. Each key represents a node and the value of each key is a dictionary representing the neighbors of the node (keys) and the distance to these nodes (value).
  
  We can visualise the graph by calling the method .visualise() or by printing the dictionary of the graph.
  
```python
> graph.visualise()
```


```
*** The distance between the station A and:
     - the station B is: 5 units
     - the station D is: 5 units
     - the station E is: 7 units

*** The distance between the station B and:
     - the station C is: 4 units

*** The distance between the station C and:
     - the station D is: 8 units
     - the station E is: 2 units

(...)
```
        
  Or simply, using:

```python
print(graph)
```

returns:

```python
{
  'A': {'B': 5, 'D': 5, 'E': 7},
  'B': {'C': 4},
  'C': {'D': 8, 'E': 2},
  'D': {'C': 8, 'E': 6},
  'E': {'B': 3}
}
```


__2. The methods:__


* add_node, parse_node, check_node_station, check_node_duration, clean_string_graph are the method used by ** the "build" method" ** in order to create the graph representation.


* get_neighbors(node): Return the neighbors of a node.

```python
>>> graph.get_neighbors('A')
['B', 'D', 'E']
```

* get_distance(node1, node2): Return the distance between two nodes

```python
>>> graph.get_distance('A', 'B')
5
```
  _If there is no edge from A to B, the program raise the ** GraphError ** exception._


* get_route_distance(route): Return the distance of a route (sum of distance between nodes)

```python
>>> graph.get_route_distance('ABC')
9
```
  _If there is no route 'ABC', the program raise the ** GraphError ** exception._


* generate_all_routes_from_station(departure, max_depth): Return list of routes starting from departure with max_depth stops.

```python
>>> graph.generate_all_routes_from_station('A', 3)
['A', 'AB', 'AD', 'AE', 'ABC', 'ADC', 'ADE', 'AEB', 'ABCD', 'ABCE', 'ADCD', 'ADCE', 'ADEB', 'AEBC']
```



#### Railroad model:

The Railroad Class represents a railroad as an oriented & weighted graph and offers helpful method to provide informations such as the distance along a certain route, the number of different routes between two towns, and the shortest route between two towns.


__1. Representation:__

The Railroad Class inherits from the ** Graph Class **.


__2. Methods:__

* get_trips_MaxStop(departure, arrival, max_stop): return all the routes starting from "departure" and ending in "arrival" with a maximum of stops equal to max_stop

```python
>>> railroad.get_trips_MaxStop('A', 'C', 4)
['ABC', 'ADC', 'AEBC', 'ABCDC', 'ADCDC', 'ADEBC']
```
_Note that the number of stops in the number of stations visited (including departure and arrival) minus one.

* get_count_trips_MaxStop(self, departure, arrival, max_stop): return the length of get_trips_MaxStop(departure, arrival, max_stop)

```python
>>> railroad.get_count_trips_MaxStop('A', 'C', 4)
6
```

* get_trips_ExactCountStop(departure, arrival, count_stop): return all the routes starting from "departure" and ending in "arrival" with a number of stops equal count_stop

```python
>>> railroad.get_trips_ExactCountStop('A', 'C', 4)
['ABCDC', 'ADCDC', 'ADEBC']
```

* get_count_trips_ExactCountStop(departure, arrival, count_stop): return the length of get_trips_ExactCountStop(departure, arrival, count_stop)

```python
>>> railroad.get_count_trips_ExactCountStop('A', 'C', 4)
3
```

* get_length_shortest_route(departure, arrival): return the distance of the shortest route from departure to arrival (if it exists).

```python
>>> railroad.get_length_shortest_route('A', 'E')
7
```

* get_count_routes_MaxDistance(departure, arrival, max_distance): Return the number of routes from "departure" to "arrival" with a maximum route's distance less than "max_distance"

```python
>>> railroad.get_count_routes_MaxDistance('C', 'C', 30)
7
```


  
 ## Author:
 
Yassine Belmamoun
*  [Linkedin Profile](https://www.linkedin.com/in/yassine-belmamoun/)
*  [Github Profile](https://github.com/yassinebelmamoun)
*  belmamoun.yassine [at] gmail [dot] com
