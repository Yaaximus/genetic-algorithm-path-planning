import numpy as np
from population import define_links, calculate_distance


def fitness(path_points, chr_len, new_pop, pop_max):

    # link = define_links()

    pop_pts_consec_dist = pop_pts_consecutive_dist(
        path_points=path_points, chr_len=chr_len, pop=new_pop, pop_max=pop_max)

    pop_fit_based_dist = pop_fit_based_on_dist(
        pop_max=pop_max, pop_pts_consec_dist=pop_pts_consec_dist)

    return pop_fit_based_dist


def pop_fit_based_on_dist(pop_max, pop_pts_consec_dist):

    pop_fit_based_dist = np.zeros((pop_max, 1))

    for i in range(pop_max):

        pop_fit_based_dist[i][0] = 10.0 * \
            (1.0 / np.sum(pop_pts_consec_dist[i], keepdims=True))

    return pop_fit_based_dist


def pop_pts_consecutive_dist(path_points, chr_len, pop, pop_max):

    pop_dist = np.zeros((pop_max, chr_len-1))

    for i in range(pop_max):

        for j in range(chr_len-1):

            pop_dist[i][j] = calculate_distance(
                pt_1=path_points[int(pop[i][j+1])], pt_2=path_points[int(pop[i][j])])

    return pop_dist
