from Esempi.anneal import SimAnneal


def read_coords(path):
    coords = []
    with open(path, "r") as f:
        for i in range(0, 3):
                line = f.readline()
        line = f.readline()
        line = line.strip('\n')
        data = line.split(':')
        dimension = int(data[1])
        for i in range(0, 4):
            line = f.readline()
        for i in range(0, dimension):
            line = f.readline()
            data = line.split()
            coord = [float(data[1]), float(data[2])]
            coords.append(coord)
    return coords, dimension


if __name__ == "__main__":
    coords, dimension = read_coords("burma14.txt")
    #print(coords)
    sa = SimAnneal(coords, stopping_iter=5000)
    sa.anneal()
    sa.visualize_routes()
    sa.plot_learning()
