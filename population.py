import numpy as np
import math as ma
import random


def population(pop_max, chr_len, start_index, end_index, path_points):

    np.set_printoptions(threshold=np.nan)
    link = _define_links()
    link_fit = _link_fit(link, path_points)
    link_prob = _link_prob(link_fit)
    link_cum_prob = np.cumsum(link_prob, axis=1)
    print("link_cum_prob:", link_cum_prob)
    initial_pop = np.zeros((pop_max, chr_len))
    initial_pop[:, 0] = start_index
    initial_pop[:, chr_len - 1] = end_index
    initial_pop = _create_pop(
        pop_max, link_cum_prob, chr_len, start_index, end_index, link, initial_pop)

    return initial_pop


def _define_links():

    link = -1 * np.ones((16, 5))

    link[0][0] = 0
    link[0][1] = 1
    link[0][2] = 3
    link[0][3] = 4
    link[1][0] = 1
    link[1][1] = 2
    link[1][2] = 0
    link[2][0] = 2
    link[2][1] = 5
    link[2][2] = 11
    link[2][3] = 1
    link[3][0] = 3
    link[3][1] = 6
    link[3][2] = 8
    link[3][3] = 0
    link[4][0] = 4
    link[4][1] = 5
    link[4][2] = 6
    link[4][3] = 0
    link[5][0] = 5
    link[5][1] = 4
    link[5][2] = 10
    link[5][3] = 2
    link[6][0] = 6
    link[6][1] = 7
    link[6][2] = 3
    link[6][3] = 4
    link[7][0] = 7
    link[7][1] = 9
    link[7][2] = 13
    link[7][3] = 6
    link[8][0] = 8
    link[8][1] = 13
    link[8][2] = 3
    link[9][0] = 9
    link[9][1] = 10
    link[9][2] = 15
    link[9][3] = 7
    link[10][0] = 10
    link[10][1] = 9
    link[10][2] = 11
    link[10][3] = 5
    link[11][0] = 11
    link[11][1] = 12
    link[11][2] = 2
    link[11][3] = 10
    link[12][0] = 12
    link[12][1] = 15
    link[12][2] = 11
    link[13][0] = 13
    link[13][1] = 14
    link[13][2] = 15
    link[13][3] = 7
    link[13][4] = 8
    link[14][0] = 14
    link[14][1] = 15
    link[14][2] = 13
    link[15][0] = 15
    link[15][1] = 9
    link[15][2] = 12
    link[15][3] = 13
    link[15][4] = 14

    return link


def _link_fit(link, path_points):

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


def _create_pop(pop_max, link_cum_prob, chr_len, start_index, end_index, link, initial_pop):

    for k in range(pop_max):

        i = start_index

        for j in range(chr_len):

            if j > 0 and j < (chr_len):

                random_val = random.random()

                if random_val < link_cum_prob[i][0]:

                    initial_pop[k][j] = link[i][1]
                    i = link[i][1]

                    if _is_end_point(i, end_index):

                        while j < (chr_len):

                            initial_pop[k][j] = end_index
                            j += 1

                        print("k:", k, initial_pop[k])

                elif random_val < link_cum_prob[i][1]:

                    initial_pop[k][j] = link[i][2]
                    i = link[i][2]

                    if _is_end_point(i, end_index):

                        while j < (chr_len):
                            initial_pop[k][j] = end_index
                            j += 1

                        print("k:", k, initial_pop[k])

                elif random_val < link_cum_prob[i][2]:

                    initial_pop[k][j] = link[i][3]
                    i = link[i][3]

                    if _is_end_point(i, end_index):

                        while j < (chr_len):

                            initial_pop[k][j] = end_index
                            j += 1

                        print("k:", k, initial_pop[k])

                elif random_val < link_cum_prob[i][3]:

                    initial_pop[k][j] = link[i][4]
                    i = link[i][4]

                    if _is_end_point(i, end_index):

                        while j < (chr_len):

                            initial_pop[k][j] = end_index
                            j += 1

                        print("k:", k, initial_pop[k])
                        
    return initial_pop


def _is_end_point(i, end_index):

    return True if int(i) == int(end_index) else False


def calculate_distance(pt_1, pt_2):

    return ma.sqrt(ma.pow((pt_1[0]-pt_2[0]), 2)+ma.pow((pt_1[1]-pt_2[1]), 2))
