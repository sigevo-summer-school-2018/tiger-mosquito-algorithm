#       © Shota Saito, 2018
#
#	This file is part of the Tiger Mosquito Algorithm - TMA
#	It implements the selection scheme
#
#	TMA is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	TMA is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random
import unittest

from deap import creator, base, tools, algorithms
import numpy as np

from selection import tigerMosquitoSelection

fixed_binary = [1,0,0,  # individual 1
                1,1,0,  # individual 2
                1,1,1]  # individual 3

idx = 0

def evalOneMax(individual):
    return sum(individual),


def getPheromon(individual):
    # this code is fake
    return 0,


def fixBinaryGenerated():
    global binary
    global idx
    binary = fixed_binary[idx]
    idx = idx + 1 if idx + 1 <= len(fixed_binary) - 1 else 0
    return binary

class TestTigerMosquitoSelection(unittest.TestCase):
    def setUp(self):
        if not hasattr(creator, "FitnessMax"):
            creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        if not hasattr(creator, "PheromoneMax"):
            creator.create("PheromoneMax", base.Fitness, weights=(1.0,))
        if not hasattr(creator, "Individual"):
            creator.create("Individual", list,
                           fitness=creator.FitnessMax,
                           pheromone=creator.PheromoneMax)
        self.toolbox = base.Toolbox()

        self.toolbox.register("attr_bool", fixBinaryGenerated)

        self.toolbox.register("individual", tools.initRepeat,
                              creator.Individual, self.toolbox.attr_bool, n=3)
        self.toolbox.register("population", tools.initRepeat, list,
                              self.toolbox.individual)
        self.toolbox.register("evaluate", evalOneMax)
        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        self.toolbox.register("pheromone", getPheromon)

    def test_fitness_mode(self):
        toolbox = self.toolbox
        toolbox.register("select", tigerMosquitoSelection,
                         tournsize=3, useFitness=True)
        population = toolbox.population(n=3)
        # population size = 3
        offspring = algorithms.varAnd(population, toolbox, cxpb=0., mutpb=0.)
        # set pheromone each individual
        pheromones = [50, 100, 75]
        # evaluation
        fits = toolbox.map(toolbox.evaluate, offspring)

        for i, fit_ind in enumerate(zip(fits, offspring)):
            fit, ind = fit_ind
            ind.fitness.values = fit
            ind.pheromone.values = (pheromones[i], )

        random.seed(20180719)
        selected_ind = toolbox.select(offspring, k=1)
        self.assertEqual([[1,1,1]], selected_ind)

    def test_pheromone_mode(self):
        toolbox = self.toolbox
        toolbox.register("select", tigerMosquitoSelection,
                         tournsize=3, useFitness=False)
        population = toolbox.population(n=3)
        # population size = 3
        offspring = algorithms.varAnd(population, toolbox, cxpb=0., mutpb=0.)
        # set pheromone each individual
        pheromones = [50, 100, 75]

        # evaluation
        fits = toolbox.map(toolbox.evaluate, offspring)

        max_p = -1
        for i, fit_ind in enumerate(zip(fits, offspring)):
            fit, ind = fit_ind
            ind.fitness.values = fit
            ind.pheromone.values = (pheromones[i],)
            if max_p <= pheromones[i]:
                max_p = pheromones[i]
                max_sample = ind

        random.seed(20180719)
        selected_ind = toolbox.select(offspring, k=1)
        self.assertEqual([[1,1,0]], selected_ind)

if __name__ == '__main__':
    unittest.main()
