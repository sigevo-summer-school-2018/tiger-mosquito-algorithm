# The tiger mosquito selection algorithm

This is an algorithm inspired by the mechanisms used to mitigate the tiger mosquito (and other insects) plagues.

## General description

## Pheromone update mechanism

We will use two different update of the pheromone potential (`PP`) of each individual.

* Based on the whole inheritance:

```python
if x_i selected:
  PP(x_i) += constant_value
  PP(parents[x_i]) += Q^h*PP(x_i)
```

* Based on their children

```python
if x_i selected:
  PP(x_i) += constant_value + k * size(childrens)
```


## Tournament resolution mechanism

We propose the new selection scheme that the individual is given the score stochastically.
The property of our proposed selection scheme is written as below.

---

* Input: The tournament size N_tournament, the set of candidate solutions `X = {x_1, x_2, ... , x_N}`, the objective function `f: X -> R`, the pheromone of candidate solutions `P = {p(x_1), p(x_2), ..., p(x_N)}` and the selection rate function `sr(t)` dependent on the iteration `t` such that `sr(0) = 1.0`.

* Output: the selected solutions `x*`

1.	The random value `r` is sampled from the uniform distribution.
2.	Select the `N_tournament` solutions in `X` at random.
3.	If `r <= sr`, the best candidate solution is set as `x* = max_x ( f(x_1), f(x_2), ..., f(x_N_tournament) )` ,
otherwise, the best candidate solution is set as `x* = max_x ( P(x_1), P(x_2), ..., P(x_N_tournament) )` .
4.	Return the best solution `x*`

---

## Pheromone inheritance mechanism
Three possible mechanisms:
1. Fixed pheromone value: Everyone gets a initial value, so new children don't have any advantage depending on their parents performance.
2. Random pheromone value
3. Based on parents value: Could be a function of the parents pheromone, giving and advantage depending on the parents, with the idea that better parents derives in even better children: `a · parent_1 + (1 - a) · parent_2, 0 <= a <= 1`. a can be a fixed value as `a = 0.5` or random generated
4. Base pheromone value could be some statistics  population, as the average, value.
5. Even better of the current population: `b · pheromone, b > 1 ` and `pheromone` are one of the calculated pheromone by the methods 1 or 2.


## Fitness fucntion
### one-max
We will use one-max as a fitness function. Mosquitoes are attracted to certain genes of pheromones, so we use one-max to approximate them. The optimal solution of one-max is that all data of 0,1 are all 1s.
```
length of the chromosome = N
fitnessVal = 0
for i in range N:
    fitnessVal += chromosome[i]
return fitnessVal
```

### NK problem

The NK problem is that each factor has mutual influence. The next door method was used. The next door method is to evaluate fitness by the values of adjacent parameters. The code is shown below.
``` python3
def fitness(chromosome,n,k):
    :param chromosome : A chromosome of 0 and 1
    :n, k : nk problem parameter
    global NK_landscape
    :NK_landscape is a matrix that stores fitness values.
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
