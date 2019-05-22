import math as ma

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
