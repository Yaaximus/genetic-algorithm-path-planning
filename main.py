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
import numpy as np
import matplotlib.pyplot as plt


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

    x = []
    y = []
    x_best = []
    y_best = []

    plt.figure()
    plt.axis([0.0, 15.0, 0.0, 15.0])

    for element in Config.path_points:
        x.append(element[0])
        y.append(element[1])

    for element in chr_crossover_mutated_population[0]:

        x_best.append(Config.path_points[int(element)][0])
        y_best.append(Config.path_points[int(element)][1])

    plt.plot(x, y, "ko")
    plt.plot(x_best, y_best, "g-")
    plt.draw()
    plt.savefig("./docs/images/best_path.png")
    plt.pause(0.02)


if __name__ == '__main__':

    main()
