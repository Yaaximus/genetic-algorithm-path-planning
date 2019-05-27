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
from draw_plot import draw_plot

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

        prev_best_fit = chr_pop_fitness[chr_best_fitness_index[0], 0]

        chr_pop_fitness, chr_best_fitness_index = fitness(
            new_chr_pop=chr_crossover_mutated_population)

        chr_ranked_population = ranking(
            chr_pop_fitness=chr_pop_fitness, new_pop=chr_crossover_mutated_population)

        chr_crossover_mutated_population = dna(chr_pop_fitness=chr_pop_fitness,
            ranked_population=chr_ranked_population, chr_best_fitness_index=
            chr_best_fitness_index, init_pop=chr_crossover_mutated_population)

        if prev_best_fit == chr_pop_fitness[chr_best_fitness_index[0], 0]:
            Config.stop_criteria += 1
        else:
            Config.stop_criteria = 0

        if Config.stop_criteria >= 3:
            Config.stop_generation = True

        Config.generations += 1

    for i in range(3):

        print("Best chromosome number", i, "is:",
              chr_crossover_mutated_population[chr_best_fitness_index[i]])

    draw_plot(best_chromosome=chr_crossover_mutated_population[0])

if __name__ == '__main__':

    main()
