import math as ma
import numpy as np

path_points = [[1, 7], [1, 11], [3, 14], [3, 1], [5, 8], [6, 11], [6, 4], [
    8, 4], [10, 1], [10, 7], [10, 11], [11, 14], [13, 12], [12, 2], [14, 3], [14, 8]]
npts = len(path_points)
pop_max = 50
mutation_rate = 0.001
start_index = int(0)
end_index = npts - 1
generations = 1
prev_best_fitness = 0
nobs = 7
nbits = ma.log10(npts) / ma.log10(2)
chr_len = int(((nobs+2)*nbits)/nbits)
stop_criteria = 0

def define_links():
    
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
