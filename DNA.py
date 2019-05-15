class DNA(object):

    def __init__(self, chr_fitness, pop_max, chr_len, mutation_rate, start_index, ranked_population, best_fitness_index, mutated_population, prev_best_fitness, stop_criteria):

        self._chr_fitness = chr_fitness
        self._pop_max = pop_max
        self._chr_len = chr_len
        self._mutation_rate = mutation_rate
        self._start_index = start_index
        self._ranked_population = ranked_population
        self._best_fitness_index = best_fitness_index
        self._mutated_population = mutated_population
        self._prev_best_fitness = prev_best_fitness
        self._stop_criteria = stop_criteria

    def crossover(self):

        pass