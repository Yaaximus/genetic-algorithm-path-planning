#!/usr/bin/env python

"""
Main script

Contains: main function

Author: Yasim Ahmad(yaaximus)

Email: yasim.ahmed63@yahoo.com
"""

from population import population
from fitness import fitness
from ranking import ranking
from dna import dna

from config import Config


def main():

    initial_chr_population = population()

    chr_pop_fitness, chr_best_fitness_index = fitness(
        new_chr_pop=initial_chr_population)

    chr_ranked_population = ranking(
        chr_pop_fitness=chr_pop_fitness, new_pop=initial_chr_population)

    chr_crossover_mutated_population = dna(chr_pop_fitness=chr_pop_fitness, 
        ranked_population=chr_ranked_population, chr_best_fitness_index=
        chr_best_fitness_index, init_pop=initial_chr_population)

    while not Config.stop_generation:

        prev_best_fit = chr_pop_fitness[chr_best_fitness_index[0],0]

        chr_pop_fitness, chr_best_fitness_index = fitness(
            new_chr_pop=chr_crossover_mutated_population)

        chr_ranked_population = ranking(
            chr_pop_fitness=chr_pop_fitness, new_pop=initial_chr_population)

        chr_crossover_mutated_population = dna(chr_pop_fitness=chr_pop_fitness, 
            ranked_population=chr_ranked_population, chr_best_fitness_index=
            chr_best_fitness_index, init_pop=initial_chr_population)

        if prev_best_fit == chr_pop_fitness[chr_best_fitness_index[0],0]:
            Config.stop_criteria += 1
        else:
            Config.stop_criteria = 0
            
        if Config.stop_criteria >= 3:
            Config.stop_generation = True
        
        Config.generations += 1

        print("Initial chromosome population:", initial_chr_population)

        print("Chromosome population fitness:", chr_pop_fitness)

        for i in chr_best_fitness_index:
            print("Chromosome", i, "fitness:", chr_pop_fitness[i, 0])
            print("Chromosome", i, initial_chr_population[i])

        print("Chromosome ranked population:", chr_ranked_population)

    print chr_crossover_mutated_population
    print("Generations:", Config.generations)

if __name__ == '__main__':

    main()
