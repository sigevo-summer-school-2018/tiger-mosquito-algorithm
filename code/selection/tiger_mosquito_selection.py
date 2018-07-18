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
#
#	Author: Shota Saito


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
