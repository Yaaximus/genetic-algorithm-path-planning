# Python implmentation of Genetic Algorithm in Path Planning

## Running instruction:
- Run the main.py file from directory. 
- User can defined path points, links b/w path points, population size, mutation rate

## Requirements
- python
- numpy

## Features
- user can define fixed links b/w nodes
- user can initialize population of chromosomes which are initialized randomly but program insures that two consective nodes should be linked to each other.
- user can calculate chromosome fitness based on total distance of chromosomes and connectivity of nodes.
- user can find best fitness indices
- user can rank the initial population of chromosomes using roulets wheels selection method

## Fixed issues:
- bug fixed in create population function
- bug related to chromosome population fitness best indices removed
- Bug in generate mating pool function of ranking file fixed

## Example for usage: 
#### You can initialize population, calculate fitness, find best fitness indices & rank population in main function like:

- initial_chromosome_population = population()
- chromosome_population_fitness, chromosome_best_fitness_index = fitness(new_chromosome_population=initial_chromosome_population)
- chromosome_populationn_ranked = ranking(chromosome_population_fitness=chromosome_population_fitness, new_population=initial_chromosome_population)