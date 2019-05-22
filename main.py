#!/usr/bin/env python
from population import population
from fitness import fitness
from ranking import ranking
from dna import dna


def main():

    initial_chr_population = population()

    chr_pop_fitness, chr_best_fitness_index = fitness(
        new_chr_pop=initial_chr_population)

    chr_pop_ranked = ranking(
        chr_pop_fitness=chr_pop_fitness, new_pop=initial_chr_population)

    crossover_population = dna(chr_pop_fitness=chr_pop_fitness, ranked_population=chr_pop_ranked,
                               chr_best_fitness_index=chr_best_fitness_index, 
                               mutated_population=initial_chr_population)

    print("Initial chromosome population:", initial_chr_population)
    print("Chromosome population fitness:", chr_pop_fitness)

    for i in chr_best_fitness_index:
        print("Chromosome", i, "fitness:", chr_pop_fitness[i, 0])
        print("Chromosome", i, initial_chr_population[i])

    print("Chromosome population ranked:", chr_pop_ranked)
    print crossover_population


if __name__ == '__main__':

    main()
