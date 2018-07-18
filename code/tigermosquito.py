#       © Hugo Monzon, 2018
#
#	This file is part of the Tiger Mosquito Algorithm - TMA
#	The implementation is based on the onemax.py example provided in
#	the DEAP - Distributed Evolutionary Algorithms in Python.
#
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
#

from problems.NK_fitness import fitness

import argparse

import random
import numpy as np

from deap import base
from deap import creator
from deap import tools



def config(n,k):
	
	"""
	Receives parameters for the problem, and for the genetic operators
	:param n: Defines the size of the bit string for the NK-landscape problem
	:param k: Defines the epistasis bit for the NK-landscape problem
	:returns: A toolbox object (from deap framework) that
			 has information on how to create individuals, which
			 evaluation, selection, crossover and mutation function to use
	"""
	
	#Setup Fitness type and problem to be evaluated
	#Single Objective, considering minimization
	creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
	creator.create("Individual", list, fitness=creator.FitnessMin)


	toolbox = base.Toolbox()

	# Attribute generator
	#                      define 'attr_bool' to be an attribute ('gene')
	#                      which corresponds to integers sampled uniformly
	#                      from the range [0,1] (i.e. 0 or 1 with equal
	#                      probability)
	toolbox.register("attr_bool", np.random.randint, 0, 1)

	# Structure initializers
	#                         define 'individual' to be an individual
	#                         consisting of n 'attr_bool' elements ('genes')
	toolbox.register("individual", tools.initRepeat, creator.Individual,
		toolbox.attr_bool, n)

	# define the population to be a list of individuals
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)

	#----------
	# Operator registration
	#----------
	# register the goal / fitness function
	#Interdependance of variables for NK-landscape problem
	epistasis = np.random.rand(n, pow(2,k))
	toolbox.register("evaluate", fitness,n=n,k=k,epistasis=epistasis)

	# register the crossover operator
	toolbox.register("mate", tools.cxTwoPoint)

	# register a mutation operator with a probability to
	# flip each attribute/gene of 0.05
	toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)

	# operator for selecting individuals for breeding the next
	# generation: each individual of the current generation
	# is replaced by the 'fittest' (best) of three individuals
	# drawn randomly from the current generation.
	toolbox.register("select", tools.selTournament, tournsize=3)

	#----------
	return toolbox

def main(n,k,popsize,crossover_p,mutation_p,genmax):

	toolbox = config(n,k)

	# create an initial population of 300 individuals (where
	# each individual is a list of integers)
	pop = toolbox.population(n=popsize)

	# CXPB  is the probability with which two individuals
	#       are crossed
	#
	# MUTPB is the probability for mutating an individual
	CXPB, MUTPB = crossover_p, mutation_p

	print("Start of evolution")

	# Evaluate the entire population
	fitnesses = list(map(toolbox.evaluate, pop))
	for ind, fit in zip(pop, fitnesses):
		ind.fitness.values = fit

	print("  Evaluated %i individuals" % len(pop))

	# Variable keeping track of the number of generations
	g = 0

	# Begin the evolution
	while g < genmax:
		# A new generation
		g = g + 1
		print("-- Generation %i --" % g)

		# Select the next generation individuals
		offspring = toolbox.select(pop, len(pop))
		# Clone the selected individuals
		offspring = list(map(toolbox.clone, offspring))

		# Apply crossover and mutation on the offspring
		for child1, child2 in zip(offspring[::2], offspring[1::2]):

			# cross two individuals with probability CXPB
			if random.random() < CXPB:
				toolbox.mate(child1, child2)

				# fitness values of the children
				# must be recalculated later
				del child1.fitness.values
				del child2.fitness.values

		for mutant in offspring:

			# mutate an individual with probability MUTPB
			if random.random() < MUTPB:
				toolbox.mutate(mutant)
				del mutant.fitness.values

		# Evaluate the individuals with an invalid fitness
		invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
		fitnesses = map(toolbox.evaluate, invalid_ind)
		for ind, fit in zip(invalid_ind, fitnesses):
			ind.fitness.values = fit

		print("  Evaluated %i individuals" % len(invalid_ind))

		# The population is entirely replaced by the offspring
		pop[:] = offspring

		# Gather all the fitnesses in one list and print the stats
		fits = [ind.fitness.values[0] for ind in pop]

		length = len(pop)
		mean = sum(fits) / length
		sum2 = sum(x*x for x in fits)
		std = abs(sum2 / length - mean**2)**0.5

		print("  Min %s" % min(fits))
		print("  Max %s" % max(fits))
		print("  Avg %s" % mean)
		print("  Std %s" % std)

	print("-- End of (successful) evolution --")

	best_ind = tools.selBest(pop, 1)[0]
	print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Setup some variable to run the Tiger Mosquito Algorithm.')
	parser.add_argument('seed', metavar='seed', type=int,
	help='an integer used as seed for the pseudonumber generator')
	parser.add_argument('n', metavar='n', type=int,
	help='an integer used as the number of bits of the decision variable for the problem NK-landscape')
	parser.add_argument('k', metavar='k', type=int,
	help='an integer used as the epistasis bit for the problem NK-landscape')
	parser.add_argument('popsize', metavar='popsize', type=int,
	help='an integer used as the population size of the TGA')
	parser.add_argument('crossover_p', metavar='crossover_p', type=float,
	help='a float used as the crossover probability of the TGA')
	parser.add_argument('mutation_p', metavar='crossover_p', type=float,
	help='a float used as the mutation probability of the TGA')
	parser.add_argument('genmax', metavar='genmax', type=int,
	help='an integer used as the maximum number of generations of the TGA')

	args = parser.parse_args()
	#define the seed for the random number generator
	np.random.seed(args.seed)
	main(args.n,args.k,args.popsize,args.crossover_p,args.mutation_p,args.genmax)
