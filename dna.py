#!/usr/bin/env python

"""
Script containing functionality related to DNA in Genetics like crossover & mutation.

Contains: 'do crossover' function

Author: Yasim Ahmad(yaaximus)

Email: yasim.ahmed63@yahoo.com
"""

from config import Config

import numpy as np
import random


def dna(chr_pop_fitness, ranked_population, chr_best_fitness_index, init_pop):

    chromo_crossover_pop = _do_crossover(
        ranked_pop=ranked_population, chr_best_fit_indx=chr_best_fitness_index,
         init_pop=init_pop)

    return chromo_crossover_pop


def _do_crossover(ranked_pop, chr_best_fit_indx, init_pop):

    crossover_pop = np.zeros((Config.pop_max, Config.chr_len))

    crossover_pop[0, :] = init_pop[chr_best_fit_indx[0], :]
    crossover_pop[1, :] = init_pop[chr_best_fit_indx[1], :]
    crossover_pop[2, :] = init_pop[chr_best_fit_indx[2], :]

    itr = 3

    while itr < Config.pop_max / 5:

        a = random.randint(0, Config.chr_len - 1)
        b = random.randint(0, Config.chr_len - 1)

        partner_a = ranked_pop[a, :]
        partner_b = ranked_pop[b, :]
        joining_pt = random.randint(0, Config.chr_len - 1)

        crossover_pop[itr, :joining_pt] = partner_a[:joining_pt]
        crossover_pop[itr+1, :joining_pt] = partner_b[:joining_pt]

        crossover_pop[itr, joining_pt:] = partner_b[joining_pt:]
        crossover_pop[itr+1, joining_pt:] = partner_a[joining_pt:]

        itr += 2

    while itr < Config.pop_max:

        crossover_pop[itr] = ranked_pop[itr]
        itr += 1

    return crossover_pop
