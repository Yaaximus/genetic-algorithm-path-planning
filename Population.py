import numpy as np

class Population(object):

    def __init__(self, pop_max, chr_len, start_index, end_index, path_points):

        self._pop_max = pop_max
        self._chr_len = chr_len
        self._start_index = start_index
        self._end_index = end_index
        self._path_points = path_points
        self._link = np.zeros((16,5))
        self.__define_links()

    def __define_links(self):

        self._link[0][0] = 1  ; self._link[0][1]  = 2
        self._link[0][2] = 4  ; self._link[0][3]  = 5
        self._link[1][0] = 2  ; self._link[1][1]  = 3
        self._link[1][2] = 1
        self._link[2][0] = 3  ; self._link[2][1]  = 6
        self._link[2][2] = 12 ; self._link[2][3]  = 2
        self._link[3][0] = 4  ; self._link[3][1]  = 7
        self._link[3][2] = 9  ; self._link[3][3]  = 1
        self._link[4][0] = 5  ; self._link[4][1]  = 6
        self._link[4][2] = 7  ; self._link[4][3]  = 1
        self._link[5][0] = 6  ; self._link[5][1]  = 5
        self._link[5][2] = 11 ; self._link[5][3]  = 3
        self._link[6][0] = 7  ; self._link[6][1]  = 8
        self._link[6][2] = 4  ; self._link[6][3]  = 5
        self._link[7][0] = 8  ; self._link[7][1]  = 10
        self._link[7][2] = 14 ; self._link[7][3]  = 7
        self._link[8][0] = 9  ; self._link[8][1]  = 14
        self._link[8][2] = 4
        self._link[9][0] = 10 ; self._link[9][1]  = 11
        self._link[9][2] = 16 ; self._link[9][3]  = 8
        self._link[10][0] = 11; self._link[10][1] = 10
        self._link[10][2] = 12; self._link[10][3] = 6
        self._link[11][0] = 12; self._link[11][1] = 13
        self._link[11][2] = 3; self._link[11][3] = 11
        self._link[12][0] = 13; self._link[12][1] = 16
        self._link[12][2] = 12
        self._link[13][0] = 14; self._link[13][1] = 15
        self._link[13][2] = 16; self._link[13][3] = 8
        self._link[13][4] = 9
        self._link[14][0] = 15; self._link[14][1] = 16
        self._link[14][2] = 14
        self._link[15][0] = 16; self._link[15][1] = 10
        self._link[15][2] = 13; self._link[15][3] = 14
        self._link[15][4] = 15

        print self._link

    def initialize_population(self):

            pass