#!/usr/bin/env python

"""
Script provide functionality related to ranking of the population. Ranking is 
obtained using roulets wheel selection method.

Author: Yasim Ahmad(yaaximus)

Email: yasim.ahmed63@yahoo.com
"""

from config import Config

import numpy as np


def ranking(chr_pop_fitness, pop):
    """
    This function encapsulates the capability of generate ranking of chromosome
    population based on roulet wheel selection method.
    
    Parameters
    ----------
    chr_pop_fitness : [numpy.ndarray]
        [fitness of chromosome population]
    pop : [numpy.ndarray]
        [Population of chromosomes which will undergo ranking process]
    
    Returns
    -------
    [numpy.ndarray]
        [Population of ranked chromosomes]
    """

    chromo_prob = cal_prob(chr_pop_fitness=chr_pop_fitness)

    chromo_cum_prob = np.cumsum(chromo_prob, axis=0)

    chromo_rank = _ranking_based_on_roulet_wheel_selection(chr_cum_prob=chromo_cum_prob)

    chromo_pop_ranked = _generate_mating_pool(chr_rank=chromo_rank, pop=pop)

    return chromo_pop_ranked


def _generate_mating_pool(chr_rank, pop):
    """
    This function is responsible for generating mating pool which will undergo
    crossover and mutation in the next stage.
    
    Parameters
    ----------
    chr_rank : [numpy.ndarray]
        [ranks of chromosomes based on roulets wheeel selection method]
    pop : [numpy.ndarray]
        [Population of chromosomes from which mating pool will be generated]
    
    Returns
    -------
    [numpy.ndarray]
        [numpy arrayy of mating pool]
    """

    ranked_pop = np.zeros((1, np.shape(pop)[1]))

    for i in range(Config.pop_max):
        for j in range(int(chr_rank[i, 0])):
            if np.shape(ranked_pop)[0] == 1:
                ranked_pop = pop[i, :]
            else:
                ranked_pop = np.vstack((ranked_pop, pop[i, :]))
    return ranked_pop


def _ranking_based_on_roulet_wheel_selection(chr_cum_prob):
    """
    This function encapsulates the capability of doing ranking of chromosomes
    population based on roulets wheel selection method
    
    Parameters
    ----------
    chr_cum_prob : [numpy.ndarray]
        [Chromosome cumulative probabilty based on chromosome fitness]
    
    Returns
    -------
    [numpy.ndarray]
        [ranks of chromosomes based on roulets wheeel selection method]
    """

    rand_array = np.random.rand(Config.pop_max)
    no_of_times_chr_got_choosen = np.zeros((Config.pop_max, 1))
    chr_rank = np.zeros((Config.pop_max, 1))

    for i in range(Config.pop_max):
        k = 0
        while chr_cum_prob[k, 0] < rand_array[i]:
            k += 1
        no_of_times_chr_got_choosen[i, 0] = k

    for i in range(Config.pop_max):
        for j in range(Config.pop_max):
            if no_of_times_chr_got_choosen[j, 0] == i:
                chr_rank[i, 0] += 1

    return chr_rank


def cal_prob(chr_pop_fitness):
    """
    
    
    Parameters
    ----------
    chr_pop_fitness : [numpy.ndarray]
        [fitness of chromosome population]
    
    Returns
    -------
    [numpy.ndarray]
        [Chromosome probabilty based on chromosome fitness]
    """

    chr_prob = np.zeros((Config.pop_max, 1))

    for i in range(Config.pop_max):

        chr_prob[i, 0] = chr_pop_fitness[i, 0] / \
            np.sum(chr_pop_fitness, keepdims=True)

    return chr_prob
