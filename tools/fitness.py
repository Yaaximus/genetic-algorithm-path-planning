#!/usr/bin/env python

"""
Script provides functionality related to fitness of chromosomes based
on total distance and connection b.w two consecutive nodes of a chromosome

Author: Yasim Ahmad(yaaximus)

Email: yasim.ahmed63@yahoo.com
"""

from config import Config
from tools.population import calculate_distance

import numpy as np


def fitness(chr_pop):
    """
    This function is responsible for calculating fitness of chromosomes.
    
    Parameters
    ----------
    chr_pop : [numpy.ndarray]
        [Population of chromosomes whose fitness is to be calculated]
    
    Returns
    -------
    [numpy.ndarray]
        [(1)Population of chromosomes whose fitness is calculated, 
         (2)List of indices of best fitness chromosomes]
    """

    chromo_pts_consec_dist = chr_pts_consecutive_dist(pop=chr_pop)

    chromo_fit_based_dist = chr_fit_based_dist(chr_pts_consec_dist=chromo_pts_consec_dist)

    chromo_conn = chr_conn(chr_pop=chr_pop)

    chromo_fit_based_conn = chr_fit_based_conn(chr_conn=chromo_conn)

    chromo_fit = chr_fit(chr_fit_based_dist=chromo_fit_based_dist,
        chr_fit_based_conn=chromo_fit_based_conn)

    chromo_best_fit_index = chr_best_fit_ind(chr_fit=chromo_fit)

    return chromo_fit, chromo_best_fit_index


def chr_best_fit_ind(chr_fit):
    """
    This function is responsible for finding best fitness chromosome indices.
    
    Parameters
    ----------
    chr_fit : [numpy.ndarray]
        [numpy array of chromosome population fitness]
    
    Returns
    -------
    [list]
        [list of best fitness chromosome indices]
    """

    temp_chr_fit = np.array(chr_fit, copy=True)

    chr_best_fit_index = []

    while len(chr_best_fit_index) < 3:

        y = np.where(temp_chr_fit == np.amax(temp_chr_fit))[0]

        for i in range(len(y)):
            chr_best_fit_index.append(int(y[i]))

        for i in chr_best_fit_index:
            temp_chr_fit[i][0] = 0

    return chr_best_fit_index


def chr_fit(chr_fit_based_dist, chr_fit_based_conn):
    """
    This function is responsible for calculating fitness of chromosome population
    based on total distance of individual chromosome, and links b/w path points
    of individual chromosome.
    
    Parameters
    ----------
    chr_fit_based_dist : [numpy.ndarray]
        [numpy array of chromosome fitness based on total distance]
    chr_fit_based_conn : [numpy.ndarray]
        [numpy array of chromosome fitness based on links b/w path 
        points of individual chromosome]
    
    Returns
    -------
    [numpy.ndarray]
        [final fitness of chromosome population]
    """

    chr_fit = np.zeros((Config.pop_max, 1))

    for i in range(Config.pop_max):

        chr_fit[i][0] = chr_fit_based_dist[i][0] + chr_fit_based_conn[i][0]

    return chr_fit


def chr_fit_based_conn(chr_conn):
    """
    This function is responsible for calculating fitness of chromosome population
    based on number of connections b/w path points of an individual chromosome
    
    Parameters
    ----------
    chr_conn : [numpy.ndarray]
        [numpy array of number of connection b/w path points of an individual chromosome]
    
    Returns
    -------
    [numpy.ndarray]
        [numpy array of chromosome population fitness based on connections]
    """

    chr_conn_fit = np.zeros((Config.pop_max, 1))

    for i in range(Config.pop_max):

        chr_conn_fit[i][0] = chr_conn[i][0] / ( Config.chr_len - 1 )

    return chr_conn_fit


def chr_conn(chr_pop):
    """
    This function is responsible for finding number of connections b/w path points of
    a individual chromosome.
    
    Parameters
    ----------
    chr_pop : [numpy.ndarray]
        [Population of chromosomes whose number of connections are to be calculated]
    
    Returns
    -------
    [numpy.ndarray]
        [numpy array of number of connection b/w path points of an individual chromosome]
    """

    link = Config.define_links()
    chr_conn = np.zeros((Config.pop_max, 1))

    for i in range(Config.pop_max):
        for j in range(Config.chr_len-1):
            a = int(chr_pop[i][j])
            b = int(chr_pop[i][j+1])
            for k in range(np.shape(link)[1]):
                if link[a, k] == b:
                    chr_conn[i][0] += 1

    return chr_conn


def chr_fit_based_dist(chr_pts_consec_dist):
    """
    This function is responsible for calculating chromosome fitness based on total
    distance of individual chromosome.
    
    Parameters
    ----------
    chr_pts_consec_dist : [numpy.ndarray]
        [numpy array of individual chromosome total distance]
    
    Returns
    -------
    [numpy.ndarray]
        [numpy array of individual chromosome fitness based on total distance]
    """

    chr_pop_fit_based_dist = np.zeros((Config.pop_max, 1))

    for i in range(Config.pop_max):

        chr_pop_fit_based_dist[i][0] = 10.0 * \
            (1.0 / np.sum(chr_pts_consec_dist[i], keepdims=True))

    return chr_pop_fit_based_dist


def chr_pts_consecutive_dist(pop):
    """
    This function is responsible for calculating total distance of individual
    chromosome in population of chromosomes.
    
    Parameters
    ----------
    pop : [numpy.ndarray]
        [Population of chromosomes whose total distance is to be calculated]
    
    Returns
    -------
    [umpy.ndarray]
        [numpy array of individual chromosome total distance]
    """

    chr_pop_dist = np.zeros((Config.pop_max, Config.chr_len-1))

    for i in range(Config.pop_max):

        for j in range(Config.chr_len-1):

            chr_pop_dist[i][j] = calculate_distance(
                pt_1=Config.path_points[int(pop[i][j+1])],
                pt_2=Config.path_points[int(pop[i][j])])

    return chr_pop_dist
