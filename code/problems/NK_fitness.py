#	© Hyeon-Chang Lee, Hugo Monzon, 2018
#
#	This file is part of the Tiger Mosquito Algorithm - TMA
#	It implements the NK-Landscape problem
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


def fitness(chromosome,n,k,epistasis):
    """
	Implements the problem NK-landscape where N is the number of bits
	of the bit string or number of decision variables (binary), and K 
	determines the epistasis or the effect of each variable on others.
    
    The calculation is done in a nextdoor fashion, taking groups of 2^k,
    and considering the list as cyclical.
    
    Required
    :param chromosome: A list of int composed by 0s or 1s.
    :param n: The number of decision variables.
    :param k: The epistasis bit.
    :param epistasis: a matrix that defines the effect of each variable
    to others.
    
    :returns: A single float that represents the fitness of the individual.
    
    """

    temp_list=[]
    for i in range(n):
        temp_str = ""
        for j in range(k):
            temp_str += str(chromosome[(i+j) % n])
        temp_list.append(int(temp_str, 2))
    fitness_val = 0
    for i in range(n):
        fitness_val += epistasis[i][temp_list[i]]

    return (fitness_val,)
