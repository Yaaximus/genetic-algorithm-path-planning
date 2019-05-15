class Population(object):

    def __init__(self, pop_max, chr_len, start_index, end_index, path_points):

        self._pop_max = pop_max
        self._chr_len = chr_len
        self._start_index = start_index
        self._end_index = end_index
        self._path_points = path_points

    def initialize_population(self):

        pass