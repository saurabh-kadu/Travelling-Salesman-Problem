#!/usr/bin/env python3
import paco
import math
import city
import random
import numpy

class Ant:
    def __init__(self,i,world):
        self.index=i
        self.path_length=0
        self.currCity=world.cities[0]
        self.path=[]
        self.path.append(world.cities[0])
        self.unvisited=[]
        self.unvisited.extend(world.cities[1:])
        self.transition_probs=[]

    def reset_ant(self,world):
        self.path_length=0
        self.currCity=world.cities[0]
        self.path=[]
        self.path.append(world.cities[0])
        self.unvisited=[]
        self.unvisited.extend(world.cities[1:])
        self.transition_probs=[]

    def get_transition_prob(self,world,city_y):
        b = 0
        a = world.routing_table[self.currCity.index][city_y.index]
        for c in self.unvisited:
            b = b + world.routing_table[self.currCity.index][c.index]
        trans_prob = a/float(b)
        return trans_prob

    def calc_path_length(self):
        sum_dist=0.00
        for i in range(0,len(self.path)):
            try:
                distance =  math.sqrt(math.pow((self.path[i].x-self.path[i+1].x),2.0)+math.pow((self.path[i].y-self.path[i+1].y),2.0))            
                sum_dist=sum_dist+distance
                self.path_length = sum_dist
            except:
                return sum_dist