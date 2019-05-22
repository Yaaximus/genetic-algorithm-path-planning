import numpy as np


def ranking(chr_pop_fitness, new_pop, pop_max):

    chromo_prob = cal_prob(pop_max=pop_max, chr_pop_fitness=chr_pop_fitness)

    chromo_cum_prob = np.cumsum(chromo_prob, axis=0)

    chromo_rank = _ranking_based_on_roulet_wheel_selection(
        pop_max=pop_max, chr_cum_prob=chromo_cum_prob)

    chromo_pop_ranked = _generate_mating_pool(
        pop_max=pop_max, chr_rank=chromo_rank, pop=new_pop)

    return chromo_pop_ranked


def _generate_mating_pool(pop_max, chr_rank, pop):

    ranked_pop = np.zeros((1, np.shape(pop)[1]))

    for i in range(pop_max):
        for j in range(int(chr_rank[i, 0])):
            if np.shape(ranked_pop)[0] == 1:
                ranked_pop = pop[i, :]
            else:
                ranked_pop = np.vstack((ranked_pop, pop[i, :]))
    return ranked_pop


def _ranking_based_on_roulet_wheel_selection(pop_max, chr_cum_prob):

    rand_array = np.random.rand(pop_max)
    no_of_times_chr_got_choosen = np.zeros((pop_max, 1))
    chr_rank = np.zeros((pop_max, 1))

    for i in range(pop_max):
        k = 0
        while chr_cum_prob[k, 0] < rand_array[i]:
            k += 1
        no_of_times_chr_got_choosen[i, 0] = k

    for i in range(pop_max):
        for j in range(pop_max):
            if no_of_times_chr_got_choosen[j, 0] == i:
                chr_rank[i, 0] += 1

    return chr_rank


def cal_prob(pop_max, chr_pop_fitness):

    chr_prob = np.zeros((pop_max, 1))

    for i in range(pop_max):

        chr_prob[i, 0] = chr_pop_fitness[i, 0] / \
            np.sum(chr_pop_fitness, keepdims=True)

    return chr_prob
