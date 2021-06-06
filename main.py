from TSP import TSP
from leggi_coordinate import leggi_coordinate


if __name__ == "__main__":
    indice_linea_dimensione = 4
    indice_inizio_linee_coordinate = 7
    coordinate, dimensione = leggi_coordinate("IstanzeBenchmark/vm1084.tsp.txt", indice_linea_dimensione,
                                              indice_inizio_linee_coordinate)
    b = 239297 # 554070.556050 # 30.87 # 33.23 # 554070.556050  # 19947008.20167722 #239297 #2579  # best solution
    # istanza benchmark
    tsp = TSP(coordinate)
    eur = tsp.simulatedannealing()
    gap = (abs(float(b) - float(eur)) / abs(float(b))) * 100.0
    print("gap : ", gap)
    tsp.visualizza_tour()
