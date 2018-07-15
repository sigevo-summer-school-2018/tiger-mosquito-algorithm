import numpy as np

NK_landscape = None

def fitness(chromosome,n,k):
    #The inputs are choromosome with 0,1, and n, k.
    #Using nextdoor method
    global NK_landscape
    if NK_landscape is None:
        NK_landscape = np.random.rand(n, 2**k)

    temp_list = []
    for i in range(n):
        temp_str = ""
        for j in range(k):
            temp_str += str(chromosome[(i+j) % n])
        temp_list.append(int(temp_str, 2))
    fitness_val = 0
    for i in range(n):
        fitness_val += NK_landscape[i][temp_list[i]]

    #output is fitness value
    return fitness_val