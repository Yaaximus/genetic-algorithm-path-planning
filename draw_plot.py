from config import Config
import matplotlib.pyplot as plt

def draw_plot(best_chromosome):

    node_x = []
    node_y = []
    best_path_x = []
    best_path_y = []

    plt.figure()
    plt.axis([0.0, 15.0, 0.0, 15.0])

    for element in Config.path_points:
        node_x.append(element[0])
        node_y.append(element[1])

    for element in best_chromosome:

        best_path_x.append(Config.path_points[int(element)][0])
        best_path_y.append(Config.path_points[int(element)][1])

    plt.plot(node_x, node_y, "ko")
    plt.plot(best_path_x, best_path_y, "g-")
    plt.draw()
    plt.savefig("./docs/images/best_path.png")
    plt.pause(0.02)
