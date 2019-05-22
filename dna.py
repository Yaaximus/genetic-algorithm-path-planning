from config import Config

def dna(chr_pop_fitness, ranked_population, chr_best_fitness_index, mutated_population):

    pop_max = Config.pop_max
    chr_len = Config.chr_len
    mutation_rate = Config.mutation_rate
    start_index = Config.start_index
    prev_best_fitness = Config.prev_best_fitness
    stop_criteria = Config.stop_criteria

    return ranked_population