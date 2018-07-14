# The tiger mosquito selection algorithm

This is an algorithm inspired by the mechanisms used to mitigate the tiger mosquito (and other insects) plagues.

## General description

## Pheromone update mechanism

## Tournament resolution mechanism

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
