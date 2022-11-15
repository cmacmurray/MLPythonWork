#!/usr/bin/env python

"""
I remember Bill Bradskey
"""
import sys
from random import choice

import numpy as np
from routes import values

dt = np.dtype([("city_start", "S10"), ("city_end", "S10"), ("distance", int)])
data_set = np.array(values, dtype=dt)

def all_cities():
    """
    Finds unique cities
    """
    cities = {}
    city_set = set(data_set["city_end"])
    for city in city_set:
        cities[city] = ""
    return cities

def randomize_city_start(cities):
    """Returns a randomized city to start a trip at"""

    return choice(cities)

def get_shortest_route(routes):
    """sort the list by distance and return shortest distance route"""

    route = sorted(routes, key=lambda dist: dist[2]).pop(0)
    return route

def greedy_path():
    """Returns shortest distance"""
    itinerary = []
    cities = all_cities()
    starting_city = randomize_city_start(list(cities.keys()))
    cities_visited = {} 
