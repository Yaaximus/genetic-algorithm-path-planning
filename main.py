#!/usr/bin/env python
from population import population
from fitness import fitness
from ranking import ranking
from DNA import DNA

import math as ma


def main():

    path_points = [[1, 7], [1, 11], [3, 14], [3, 1], [5, 8], [6, 11], [6, 4], [
        8, 4], [10, 1], [10, 7], [10, 11], [11, 14], [13, 12], [12, 2], [14, 3], [14, 8]]
    npts = len(path_points)
    pop_max = 500
    mutation_rate = 0.001
    start_index = int(0)
    end_index = npts - 1
    generations = 1
    prev_best_fitness = 0
    nobs = 7
    nbits = ma.log10(npts) / ma.log10(2)
    chr_len = int(((nobs+2)*nbits)/nbits)
    stop_criteria = 0

    initial_chr_population = population(
        pop_max=pop_max, chr_len=chr_len, start_index=start_index,
        end_index=end_index, path_points=path_points)

    chr_pop_fitness, chr_best_fitness_index = fitness(
        path_points=path_points, chr_len=chr_len,
        new_chr_pop=initial_chr_population, pop_max=pop_max)

    chr_pop_ranked = ranking(chr_pop_fitness=chr_pop_fitness,
                             new_pop=initial_chr_population, pop_max=pop_max)

    print("Initial chromosome population:", initial_chr_population)
    print("Chromosome population fitness:", chr_pop_fitness)

    for i in chr_best_fitness_index:
        print("Chromosome", i, "fitness:", chr_pop_fitness[i, 0])
        print("Chromosome", i, initial_chr_population[i])

    print("Chromosome population ranked:", chr_pop_ranked)

    # crossover_population = DNA(chr_fitness=chr_fitness, pop_max=pop_max, chr_len=chr_len, mutation_rate=mutation_rate, start_index=start_index, ranked_population=ranked_population, best_fitness_index=best_fitness_index, mutated_population=initial_population, prev_best_fitness=prev_best_fitness, stop_criteria=stop_criteria)


if __name__ == '__main__':

    main()
