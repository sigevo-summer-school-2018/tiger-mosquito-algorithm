# Basic structure of the selection function
To define a selection mechanism in DEAP, a function is needed that takes at least a list of individuals, the number of individuals to be choosen. 
```python
def mySelection(individuals, k, config, useFitness):
    """Select the best individual/s according to some method. The list returned contains
    references to the input *individuals*.
    Required
    :param individuals: A list of individuals to select from.
    :param k: The number of individuals to select.
    Defined by the user
    :param config: A parameter that defines some configuration
    :param useFitness: If Fitness or pheromone should be used
    :returns: A list of selected individuals.
    """
    chosen = []
    for i in xrange(k):
        #Code to do selection here, using parameter config
        
        if useFitness:
            #use fitness to decide
        else:
            #use pheromone to decide
        
        chosen.append(...)
    return chosen
```
After the function is defined, we need to register it, and if neccesary pass any other parameter required by our
method.
```python
toolbox.register("select",mySelection,config=[...])
```
To perform selection in the algorithm we call the function, with a list from where to choose, the quantity and
any other extra parameter required.
```python
selected = toolbox.select(listOfIndividuals, 2, useFitness=False)
```
Here it will return two individuals, and will not use fitness to decide.
