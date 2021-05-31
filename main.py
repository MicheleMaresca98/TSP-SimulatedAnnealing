from TSP import TSP
from leggi_coordinate import leggi_coordinate


if __name__ == "__main__":
    coordinate, dimensione = leggi_coordinate("burma14.txt",4,9)
    b = 554070.556050  # 19947008.20167722 #239297 #2579 #3323  # best solution istanza benchmark
    tsp = TSP(coordinate)
    eur = tsp.simulatedannealing()
    gap = (abs(float(b) - float(eur)) / abs(float(b))) * 100.0
    # tsp.visualizza_tour()
