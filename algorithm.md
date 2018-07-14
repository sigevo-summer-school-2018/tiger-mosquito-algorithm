# The tiger mosquito selection algorithm

This is an algorithm inspired by the mechanisms used to mitigate the tiger mosquito (and other insects) plagues.

## General description

## Pheromone update mechanism

## Tournament resolution mechanism
We propose the new selection scheme that the individual is given the score stochastically.
The property of our proposed selection scheme is written as below.

---

Input: The tournament size N_tournament, the set of candidate solutions `X = {x_1, x_2, ... , x_N}`, the objective function `f: X -> R`, the pheromone of candidate solutions `P = {p(x_1), p(x_2), ..., p(x_N)}` and the selection rate function `sr(t)` dependent on the iteration `t` such that `sr(0) = 1.0`.

Output: the selected solutions `x*`

1.	The random value `r` is sampled from the uniform distribution.
2.	Select the `N_tournament` solutions in `X` at random.
3.	If `r <= sr`, the best candidate solution is set as `x* = max_x ( f(x_1), f(x_2), ..., f(x_N_tournament) )` ,
otherwise, the best candidate solution is set as `x* = max_x ( P(x_1), P(x_2), ..., P(x_N_tournament) )` .
4.	Return the best solution `x*`

---

## Pheromone inheritance mechanism

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
