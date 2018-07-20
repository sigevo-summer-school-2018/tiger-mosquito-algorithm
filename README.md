# The tiger mosquito algorithm

This is the project of one of the teams in the [SIGEvo summer school 2018](https://sigevo-summer-school-2018.github.io).

This site can be accessed also through the short url https://git.io/wasabitigers

The final presentation at the summer school is [available from GDrive](https://docs.google.com/presentation/d/174OBwUA8NW9neNcATf0R-6bgGZ3t2arhKnh08l732vc/present?token=AC4w5Vh6H0th2myNK_sdvN6A3a5RIfh9iQ%3A1532046223893&includes_info_params=1#slide=id.p)

## Description of the algorithm

A new evolutionary algorithm inspired from the tiger mosquito plague fighting techniques. The only things that change is the selection mechanism, which uses a *pheromone* to represent the direction in which search should go.

An algorithm that removes mosquitoes that carry dengue virus, zykova virus, yellow fever virus. You will choose a pheromone to eliminate mosquitoes, a good pheromone and a bad pheromone to make a pheromone that attracts tiger mosquitoes.

1. Initialize the pheromone.
   * The way to initialize the pheromone fitness is to use the NK_landscape method.
   * A detailed code of nk_landscape is shown on [this page](code/tiger_mosquito_algorithm/problems/NK_fitness.py).
2. Measure the fitness of pheromones.
   * After initialization, the fitness function uses PP (Pheromone-Potential).
   * We will use two different update methods for the pheromone value (P) of each individual.
     * Based on the whole inheritance:
      ```python
      if x_i selected:
        P(x_i) += constant_value
        P(parents[x_i]) += Q^h*P(x_i)
      ```
     * Based on their children
      ```python
      if x_i selected:
        P(x_i) += constant_value + k * size(childrens)
      ```
   * The contents of the PP are shown in [This page](https://github.com/sigevo-summer-school-2018/tiger-mosquito-algorithm/issues/9).
3. Use the tormant selection to get the results.
   * We use the new selection scheme that the individual is given the score stochastically.
     1.	The random value `r` is sampled from the uniform distribution.
     2.	Select the `N_tournament` solutions in `X` at random.
     3.	If `r <= sr`, the best candidate solution is set as `x* = max_x ( f(x_1), f(x_2), ..., f(x_N_tournament) )` otherwise, the best candidate solution is set as `x* = max_x ( P(x_1), P(x_2), ..., P(x_N_tournament) )` .
     4.	Return the best solution `x*`
   * A detailed code of selection is shown on [this page](code/tiger_mosquito_algorithm/selection/tiger_mosquito_selection.py)
4. Cross over each result to get a new generation and perform mutation.
5. repeat

A more extended description will be shown in [this page](algorithm.md)

## The team

[5 students from all over the world, and a tutor](team.md).

## Other teams

The [*tigers* team](https://sigevo-summer-school-2018.github.io/tigers/) tries to model the spread of mosquitos.
