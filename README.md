# Python implementation of Genetic Algorithm in Path Planning

![GA_path_planning](https://user-images.githubusercontent.com/37571161/58662732-51820100-8344-11e9-97fb-a66e6e1cc877.gif)

## Running instruction:
- Run the main.py file from directory. 
- User can defined path points, links b/w path points, population size, mutation rate
in the Config.py file

## Requirements
- python
- numpy

## Features
- user can define fixed links b/w nodes
- user can initialize population of chromosomes which are initialized randomly
but program insures that two consective nodes should be linked to each other.
- user can calculate chromosome fitness based on total distance of chromosomes
and connectivity of nodes.
- user can find best fitness indices
- user can rank the initial population of chromosomes using roulets wheels 
selection method
- user can do crossover on the population
- user can do mutation on the population

## Fixed issues:
- bug fixed in create population function
- bug related to chromosome population fitness best indices removed
- Bug in generate mating pool function of ranking file fixed
- Bug removed in function check fitness based on connection in fitness file

## Example for usage: 
#### You can initialize population in main function like:
- chr_population = population()
#### You can calculate fitness & find best fitness indices in main function like:
- chr_pop_fitness, chr_best_fitness_index = fitness(chr_pop=chr_population)
#### You can obtain ranked population in main function like:
- chr_ranked_population = ranking(chr_pop_fitness=chr_pop_fitness, pop=chr_population)
#### You can do crossover & mutation in main function like:
- chr_crossover_mutated_population = dna(chr_pop_fitness=chr_pop_fitness, 
ranked_population=chr_ranked_population, chr_best_fitness_index=chr_best_fitness_index,
last_pop=chr_population)

## Objective
- Use Genetic Algorithm for finding a best path for mobile robot in a 2D environment.
- To move from starting point to the endpoint while avoiding collisions with
obstacles and minimizing total distance travelled.

## Flow Chart of Genetic Algorithm

![flow_chart_GA](https://user-images.githubusercontent.com/37571161/58673241-f829ca00-8363-11e9-8643-9f508ce0f94c.png)
