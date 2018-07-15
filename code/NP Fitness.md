# NP problem fitness function structure


This is a function to obtain fitness. This code uses the nextdoor method.
``` python3
def fitness(chromosome,n,k):
    :param chromosome : A chromosome of 0 and 1
    :n, k : nk problem parameter
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

    return fitness_val
```

After import, execute the function with chromosome and n, k as input. The result is fitness.
``` python3
import NP_fitness

fitness_vlaue = NP.fitness.fitness(chromosome, n, k)
```
