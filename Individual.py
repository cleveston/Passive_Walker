#!/usr/bin/env python2.7

import random
from math import *
from simulation import simulation

'''Creates a passive dynamic walker. The parameters
are as follow:
pos -- the initial position
ul -- the length of the upper leg
ll -- the length of the lower leg
w -- the width of the robot
lua -- the angle of the left hip
lla -- the angle of the left ankle
rua -- the angle of the right hip
rla -- the angle of the right angle'''

class Individual(object):
    alleles = [[600, 600], [250, 250], [20, 80], [10, 60], [10, 60], [
        0, pi/2], [0, pi/2], [0, pi/2], [0, pi/2]]
    length = 9
    seperator = ''

    def __init__(self, chromosome=None):
        self.chromosome = chromosome or self._makechromosome()
        self.score = 1
        self.s = simulation(show=False)

    def _makechromosome(self):
        return [random.uniform(self.alleles[gene][0], self.alleles[gene][1]) for gene in range(self.length)]

    def evaluate(self, optimum=None):

        #Start the simulation
        self.score = self.s.start(self.chromosome)

    def show(self):
        finalSimulation = simulation()
        finalSimulation.start(self.chromosome)

    def crossover(self, other):
        return self._twopoint(other)

    def mutate(self, gene):
        self._pick(gene)

    # sample mutation method
    def _pick(self, gene):
        self.chromosome[gene] = random.uniform(
            self.alleles[gene][0], self.alleles[gene][1])

    # sample crossover method
    def _twopoint(self, other):
        left, right = self._pickpivots()

        def mate(p0, p1):
            chromosome = p0.chromosome[:]
            chromosome[left:right] = p1.chromosome[left:right]
            child = p0.__class__(chromosome)
            child._repair(p0, p1)
            return child
        return mate(self, other), mate(other, self)

    # some crossover helpers ...
    def _repair(self, parent1, parent2):
        pass

    def _pickpivots(self):
        left = random.randrange(1, self.length - 2)
        right = random.randrange(left, self.length - 1)
        return left, right

    def __repr__(self):
        "returns string representation of self"
        chromosome_str = ''
        for gene in range (len(self.chromosome)):
            chromosome_str += ' ' + str(self.chromosome[gene])

        return '<%s chromosome="%s" \nscore=%s>' % \
               (self.__class__.__name__,
                chromosome_str, self.score)

    def copy(self):
        twin = self.__class__(self.chromosome[:])
        twin.score = self.score
        return twin
