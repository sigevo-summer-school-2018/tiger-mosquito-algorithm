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

def evalOneMax(individual):
    return sum(individual),


def getPheromon(individual):
    # this code is fake
    return 0,


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
        self.toolbox.register("attr_bool", random.randint, 0, 1)
        self.toolbox.register("individual", tools.initRepeat,
                              creator.Individual, self.toolbox.attr_bool, n=50)
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
        max_sample = offspring[np.argmax(np.sum(offspring, axis=1))]
        # set pheromone each individual
        pheromones = [50, 100, 75]
        # evaluation
        fits = toolbox.map(toolbox.evaluate, offspring)
        for i, fit_ind in enumerate(zip(fits, offspring)):
            fit, ind = fit_ind
            ind.fitness.values = fit
            ind.pheromone.values = (pheromones[i], )

        selected_ind = toolbox.select(offspring, k=1)
        self.assertEqual([max_sample], selected_ind)

    def test_pheromone_mode(self):
        toolbox = self.toolbox
        toolbox.register("select", tigerMosquitoSelection,
                         tournsize=3, useFitness=False)
        population = toolbox.population(n=3)
        # population size = 3
        offspring = algorithms.varAnd(population, toolbox, cxpb=0., mutpb=0.)
        # set pheromone each individual
        pheromones = [50, 100, 75]
        max_sample = offspring[np.argmax(pheromones)]
        # evaluation
        fits = toolbox.map(toolbox.evaluate, offspring)
        for i, fit_ind in enumerate(zip(fits, offspring)):
            fit, ind = fit_ind
            ind.fitness.values = fit
            ind.pheromone.values = (pheromones[i],)

        selected_ind = toolbox.select(offspring, k=1)
        self.assertEqual([max_sample], selected_ind)

if __name__ == '__main__':
    unittest.main()
