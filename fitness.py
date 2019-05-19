import numpy as np
from population import define_links, calculate_distance


def fitness(path_points, chr_len, new_chr_pop, pop_max):

    chromo_pts_consec_dist = chr_pts_consecutive_dist(
        path_points=path_points, chr_len=chr_len, chr_pop=new_chr_pop, pop_max=pop_max)

    chromo_fit_based_dist = chr_fit_based_dist(
        pop_max=pop_max, chr_pts_consec_dist=chromo_pts_consec_dist)

    chromo_conn = chr_conn(
        pop_max=pop_max, chr_len=chr_len, chr_pop=new_chr_pop)

    chromo_fit_based_conn = chr_fit_based_conn(
        pop_max=pop_max, chr_len=chr_len, chr_conn=chromo_conn)

    chromo_fit = chr_fit(pop_max=pop_max, chr_fit_based_dist=chromo_fit_based_dist,
                         chr_fit_based_conn=chromo_fit_based_conn)

    chromo_best_fit_index = chr_best_fit_ind(chr_fit=chromo_fit)

    return chromo_fit, chromo_best_fit_index


def chr_best_fit_ind(chr_fit):

    y1 = np.where(chr_fit == np.amax(chr_fit))[0]

    chr_fit_temp = chr_fit

    for i in y1:
        chr_fit_temp[i][0] = 0

    y2 = np.append(y1, values=np.where(
        chr_fit_temp == np.amax(chr_fit_temp))[0])

    chr_fit_temp_2 = chr_fit_temp

    for i in y2:
        chr_fit_temp_2[i][0] = 0

    chr_best_fit_index = np.append(y2, values=np.where(
        chr_fit_temp_2 == np.amax(chr_fit_temp_2))[0])

    return chr_best_fit_index


def chr_fit(pop_max, chr_fit_based_dist, chr_fit_based_conn):

    chr_fit = np.zeros((pop_max, 1))

    for i in range(pop_max):

        chr_fit[i][0] = chr_fit_based_dist[i][0] + chr_fit_based_conn[i][0]

    return chr_fit


def chr_fit_based_conn(pop_max, chr_len, chr_conn):

    chr_conn_fit = np.zeros((pop_max, 1))

    for i in range(pop_max):

        chr_conn_fit[i][0] = chr_conn[i][0] / \
            np.sum(chr_conn[i], keepdims=True)

    return chr_conn_fit


def chr_conn(pop_max, chr_len, chr_pop):

    link = define_links()
    chr_conn = np.zeros((pop_max, 1))

    for i in range(pop_max):
        for j in range(chr_len-1):
            a = int(chr_pop[i][j])
            b = int(chr_pop[i][j+1])
            for k in range(np.shape(link)[1]):
                if link[a, k] == b:
                    chr_conn[i][0] += 1

    return chr_conn


def chr_fit_based_dist(pop_max, chr_pts_consec_dist):

    chr_pop_fit_based_dist = np.zeros((pop_max, 1))

    for i in range(pop_max):

        chr_pop_fit_based_dist[i][0] = 10.0 * \
            (1.0 / np.sum(chr_pts_consec_dist[i], keepdims=True))

    return chr_pop_fit_based_dist


def chr_pts_consecutive_dist(path_points, chr_len, chr_pop, pop_max):

    chr_pop_dist = np.zeros((pop_max, chr_len-1))

    for i in range(pop_max):

        for j in range(chr_len-1):

            chr_pop_dist[i][j] = calculate_distance(
                pt_1=path_points[int(chr_pop[i][j+1])], pt_2=path_points[int(chr_pop[i][j])])

    return chr_pop_dist
