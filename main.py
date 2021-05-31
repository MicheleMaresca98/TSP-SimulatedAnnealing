from TSP import TSP


def leggi_coordinate(path):
    indice_linea_dimensione = 4
    indice_inizio_linee_coordinate = 7
    coordinate = []
    with open(path, "r") as f:
        linee = f.readlines()
        linee[indice_linea_dimensione - 1].strip('\n')
        data = linee[indice_linea_dimensione - 1].split(':')
        dimensione = int(data[1])
        for i in range(0, dimensione):
            data = linee[indice_inizio_linee_coordinate - 1 + i].split()
            coordinata = [float(data[1]), float(data[2])]
            coordinate.append(coordinata)
    return coordinate, dimensione


if __name__ == "__main__":
    coordinate, dimensione = leggi_coordinate("rl5934.tsp.txt")
    b = 554070.556050  # 19947008.20167722 #239297 #2579 #3323  # best solution istanza benchmark
    tsp = TSP(coordinate)
    eur = tsp.simulatedannealing()
    gap = (abs(float(b) - float(eur)) / abs(float(b))) * 100.0
    # tsp.visualizza_tour()
