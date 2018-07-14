from operator import attrgetter
from deap.tools.selection import selRandom


def tigerMosquitoSelection(individuals, k, tournsize, useFitness):
    """Select the best individual/s according to some method. The list returned contains
    references to the input *individuals*.
    Required
    :param individuals: A list of individuals to select from.
    :param k: The number of individuals to select.
    Defined by the user
    :param tournsize: The number of individuals participating in each tournament.
    :param useFitness: If Fitness or pheromone should be used
    :returns: A list of selected individuals.
    """
    chosen = []
    for i in range(k):
        # Code to do selection here, using parameter `tournsize`
        sel_individuals = selRandom(individuals, tournsize)
        if useFitness:
            # use fitness to decide
            best_individual = max(sel_individuals, key=attrgetter('fitness'))
        else:
            # use pheromone to decide
            best_individual = max(sel_individuals, key=attrgetter('pheromone'))

        chosen.append(best_individual)
    return chosen
