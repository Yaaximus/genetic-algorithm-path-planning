#!/usr/bin/env python

"""
Script provide functionality related to initialization of population based
on nodes(path points) and links b/w nodes(path points)

Author: Yasim Ahmad(yaaximus)

Email: yasim.ahmed63@yahoo.com
"""

from config import Config

import numpy as np
import math as ma
import random


def population():
    """
    This function encapsulates the capability to initialize population of chromosomes.
    
    Returns
    -------
    [numpy.ndarray]
        [Population of chromosomes]
    """

    # np.set_printoptions(threshold=np.nan)
    link = Config.define_links()
    link_fit = _link_distance(link)
    link_prob = _link_prob(link_fit)
    link_cum_prob = np.cumsum(link_prob, axis=1)
    initial_pop = _create_pop(link_cum_prob=link_cum_prob)

    return initial_pop


def _link_distance(link):
    """
    This function is responsible for calculating distance b/w links
    
    Parameters
    ----------
    link : [numpy.ndarray]
        [links b/w path points of chromosomes]
    
    Returns
    -------
    [numpy.ndarray]
        [numpy array of distance b/w links]
    """

    link_dist = np.zeros((np.shape(link)[0], np.shape(link)[1]-1))

    for i in range(np.shape(link)[0]):

        for j in range((np.shape(link)[1])-1):

            if link[i][j] > -0.1 and link[i][j+1] > -0.1:

                link_dist[i][j] = calculate_distance(
                    pt_1=Config.path_points[int(link[i][j])], pt_2=Config.path_points[int(link[i][j+1])])

    return link_dist


def _link_prob(link_fit):
    """
    This function calculates the probability of links.
    
    Parameters
    ----------
    link_fit : [numpy.ndarray]
        [numpy array of links connections fitness based on distance]
    
    Returns
    -------
    [numpy.ndarray]
        [numpy array of links probability based on links fitness]
    """

    link_prob = np.zeros((np.shape(link_fit)[0], np.shape(link_fit)[1]))

    for i in range(np.shape(link_fit)[0]):

        for j in range(np.shape(link_fit)[1]):

            link_prob[i][j] = link_fit[i][j]/np.sum(link_fit[i], keepdims=True)

    return link_prob


def _create_pop(link_cum_prob):
    """
    This function is responsible for creating chromosome population based on connection
    b/w links.
    
    Parameters
    ----------
    link_cum_prob : [numpy.ndarray]
        [numpy array of links cumulative probability based on links fitness]
    
    Returns
    -------
    [numpy.ndarray]
        [numpy array of chromosome population based on connection b/w links]
    """

    pop = np.zeros((Config.pop_max, Config.chr_len))
    pop[:, 0] = Config.start_index
    pop[:, Config.chr_len - 1] = Config.end_index

    link = Config.define_links()

    for k in range(Config.pop_max):
        i = Config.start_index
        j = Config.start_index + 1
        while j < Config.chr_len:
            i = int(i)
            if j > 0 and j < (Config.chr_len - 1):
                random_val = random.random()
                if random_val < link_cum_prob[i][0]:
                    pop[k][j] = link[i][1]
                    i = link[i][1]
                    if _both_equ(i, Config.end_index):
                        while j < (Config.chr_len - 1):
                            pop[k][j+1] = Config.end_index
                            j += 1
                elif random_val < link_cum_prob[i][1]:
                    pop[k][j] = link[i][2]
                    i = link[i][2]
                    if _both_equ(i, Config.end_index):
                        while j < (Config.chr_len - 1):
                            pop[k][j+1] = Config.end_index
                            j += 1
                elif random_val < link_cum_prob[i][2]:
                    pop[k][j] = link[i][3]
                    i = link[i][3]
                    if _both_equ(i, Config.end_index):
                        while j < (Config.chr_len - 1):
                            pop[k][j+1] = Config.end_index
                            j += 1
                elif random_val < link_cum_prob[i][3]:
                    pop[k][j] = link[i][4]
                    i = link[i][4]
                    if _both_equ(i, Config.end_index):
                        while j < (Config.chr_len - 1):
                            pop[k][j+1] = Config.end_index
                            j += 1
            j += 1

    return pop


def _both_equ(element_1, element_2):
    """
    This function is responsible for finding if both elements are equal or not.
    
    Parameters
    ----------
    element_1 : [Int]
        [First element for comparison]
    element_2 : [Int]
        [Second element for comparison]
    
    Returns
    -------
    [Bool]
        [True or False based on wether both elements were equal or not]
    """

    return True if int(element_1) == int(element_2) else False


def calculate_distance(pt_1, pt_2):
    """
    This function encapsulates the capability of calculating distance b/w two points.
    
    Parameters
    ----------
    pt_1 : [Float]
        [point 1 for calculating distance]
    pt_2 : [Float]
        [point 2 for calculating distance]
    
    Returns
    -------
    [float]
        [Distance b/w two points]
    """

    return ma.sqrt(ma.pow((pt_1[0]-pt_2[0]), 2)+ma.pow((pt_1[1]-pt_2[1]), 2))
