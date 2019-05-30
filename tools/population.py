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

    np.set_printoptions(threshold=np.nan)
    link = Config.define_links()
    link_fit = _link_distance(link, Config.path_points)
    link_prob = _link_prob(link_fit)
    link_cum_prob = np.cumsum(link_prob, axis=1)
    initial_pop = np.zeros((Config.pop_max, Config.chr_len))
    initial_pop[:, 0] = Config.start_index
    initial_pop[:, Config.chr_len - 1] = Config.end_index
    initial_pop = _create_pop(
        pop_max=Config.pop_max, link_cum_prob=link_cum_prob,
        chr_len=Config.chr_len, start_index=Config.start_index,
        end_index=Config.end_index, initial_pop=initial_pop)

    return initial_pop


def _link_distance(link, path_points):

    link_dist = np.zeros((np.shape(link)[0], np.shape(link)[1]-1))

    for i in range(np.shape(link)[0]):

        for j in range((np.shape(link)[1])-1):

            if link[i][j] > -0.1 and link[i][j+1] > -0.1:

                link_dist[i][j] = calculate_distance(
                    pt_1=path_points[int(link[i][j])], pt_2=path_points[int(link[i][j+1])])

    return link_dist


def _link_prob(link_fit):

    link_prob = np.zeros((np.shape(link_fit)[0], np.shape(link_fit)[1]))

    for i in range(np.shape(link_fit)[0]):

        for j in range(np.shape(link_fit)[1]):

            link_prob[i][j] = link_fit[i][j]/np.sum(link_fit[i], keepdims=True)

    return link_prob


def _create_pop(pop_max, link_cum_prob, chr_len, start_index, end_index, initial_pop):

    link = Config.define_links()

    for k in range(pop_max):
        i = start_index
        j = start_index + 1
        while j < chr_len:
            i = int(i)
            if j > 0 and j < (chr_len - 1):
                random_val = random.random()
                if random_val < link_cum_prob[i][0]:
                    initial_pop[k][j] = link[i][1]
                    i = link[i][1]
                    if _both_equ(i, end_index):
                        while j < (chr_len - 1):
                            initial_pop[k][j+1] = end_index
                            j += 1
                elif random_val < link_cum_prob[i][1]:
                    initial_pop[k][j] = link[i][2]
                    i = link[i][2]
                    if _both_equ(i, end_index):
                        while j < (chr_len - 1):
                            initial_pop[k][j+1] = end_index
                            j += 1
                elif random_val < link_cum_prob[i][2]:
                    initial_pop[k][j] = link[i][3]
                    i = link[i][3]
                    if _both_equ(i, end_index):
                        while j < (chr_len - 1):
                            initial_pop[k][j+1] = end_index
                            j += 1
                elif random_val < link_cum_prob[i][3]:
                    initial_pop[k][j] = link[i][4]
                    i = link[i][4]
                    if _both_equ(i, end_index):
                        while j < (chr_len - 1):
                            initial_pop[k][j+1] = end_index
                            j += 1
            j += 1

    return initial_pop


def _both_equ(i, end_index):

    return True if int(i) == int(end_index) else False


def calculate_distance(pt_1, pt_2):

    return ma.sqrt(ma.pow((pt_1[0]-pt_2[0]), 2)+ma.pow((pt_1[1]-pt_2[1]), 2))
