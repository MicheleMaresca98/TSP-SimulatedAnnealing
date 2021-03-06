from TSP import TSP
from leggi_coordinate import leggi_coordinate
import visualize_tsp

if __name__ == "__main__":
    indice_linea_dimensione = 4
    indice_inizio_linee_coordinate = 9
    coordinate, dimensione = leggi_coordinate("IstanzeBenchmark/burma14.txt", indice_linea_dimensione, indice_inizio_linee_coordinate)
#    coordinate_usa, dimensione_usa = leggi_coordinate("IstanzeBenchmark/usa13509.tsp.txt", 7,10)
#    b = 554070.556050  # 19947008.20167722 #239297 #2579 #3323  # best solution istanza benchmark
    tour = list([0, 9, 8, 10, 7, 12, 6, 11, 5, 4, 3, 2, 13, 1])
    visualize_tsp.plotTSP([tour], coordinate)


'''''''''''''''''''''''''''''
    indice_linea_dimensione = 4
    indice_inizio_linee_coordinate = 7
    coordinate, dimensione = leggi_coordinate("IstanzeBenchmark/burma14.txt", indice_linea_dimensione, indice_inizio_linee_coordinate)
    L = 160
    t_in = 1000
    t_fin = 1
    alpha = 0.95

    with open("Test/nearest_neighbour_a280/test_generali_a280.txt", 'w') as f:
        f.write('test for nearest_neighbour_a280.txt : \n')
        print("primo: \n")
        for i in range(0, 10):
            tsp = TSP(coordinate, t_in, t_fin, alpha, L)
            eur = tsp.simulatedannealing()
            f.write(str(i + 1))
            f.write(') temperatura inziale : ')
            f.write(str(t_in))
            f.write('\n temperatura finale : ')
            f.write(str(t_fin))
            f.write('\n alpha :')
            f.write(str(alpha))
            f.write('\n iterazioni alla stessa temperatura : ')
            f.write(str(L))
            f.write('\n Esito euristica :')
            f.write(str(eur))
            f.write('\n')
            print(i, "\n")
    with open("Test/nearest_neighbour_burma/test_ordini_di_grandezza_burma14_v3.txt", 'w') as f:
        f.write('test for nearest_neighbour_burma14_v3.txt : \n')
        print("terzo: \n")
        for i in range(0, 9):
            tsp = TSP(coordinate, t_in[i], t_fin, alpha, L)
            eur = tsp.simulatedannealing()
            f.write(str(i + 1))
            f.write(') temperatura inziale : ')
            f.write(str(t_in[i]))
            f.write('\n temperatura finale : ')
            f.write(str(t_fin))
            f.write('\n alpha :')
            f.write(str(alpha))
            f.write('\n iterazioni alla stessa temperatura : ')
            f.write(str(L))
            f.write('\n Esito euristica :')
            f.write(str(eur))
            f.write('\n')
            print(i, "\n")
    with open("Test/nearest_neighbour_burma/test_ordini_di_grandezza_burma14_v1.txt", 'w') as f:
        f.write('test for nearest_neighbour_burma14_v1.txt : \n')
        print("primo: \n")
        for i in range(0, 9):
            tsp = TSP(coordinate, t_in[i], t_fin, alpha, L)
            eur = tsp.simulatedannealing()
            f.write(str(i + 1))
            f.write(') temperatura inziale : ')
            f.write(str(t_in[i]))
            f.write('\n temperatura finale : ')
            f.write(str(t_fin))
            f.write('\n alpha :')
            f.write(str(alpha))
            f.write('\n iterazioni alla stessa temperatura : ')
            f.write(str(L))
            f.write('\n Esito euristica :')
            f.write(str(eur))
            f.write('\n')
            print(i, "\n")

    with open("Test/Test_grandi_dimesioni/test_grandi_dimensioni_paametri_ottimali.txt", 'w') as f:
        f.write('test for rl5934.tsp.txt : \n')
        tsp_rl = TSP(coordinate_rl, t_in, t_fin, alpha, L)
        tsp_usa = TSP(coordinate_usa, t_in, t_fin, alpha, L)
        obj_finale_rl = tsp_rl.simulatedannealing()
        print("rl5934")
        obj_finale_usa = tsp_usa.simulatedannealing()
        print("usa13509")
        f.write(1)
        f.write(') temperatura inziale : ')
        f.write(str(t_in))
        f.write('\n temperatura finale : ')
        f.write(str(t_fin))
        f.write('\n alpha :')
        f.write(str(alpha))
        f.write('\n iterazioni alla stessa temperatura : ')
        f.write(str(L))
        f.write('\n Esito euristica :')
        f.write(str(obj_finale_rl))
        f.write('\n')
        f.write('test for usa13509.tsp.txt : \n')
        f.write(1)
        f.write(') temperatura inziale : ')
        f.write(str(t_in))
        f.write('\n temperatura finale : ')
        f.write(str(t_fin))
        f.write('\n alpha :')
        f.write(str(alpha))
        f.write('\n iterazioni alla stessa temperatura : ')
        f.write(str(L))
        f.write('\n Esito euristica :')
        f.write(str(obj_finale_usa))


    with open("Test/nearest_neighbour_vm1084/test_ordini_di_grandezza_vm1084_v3.txt", 'w') as f:
        f.write('test for nearest_neighbour_vm1084_v3.txt : \n')
        print("terzo \n")
        for i in range(0, 10):
            tsp = TSP(coordinate, t_in[i], t_fin, alpha, L)
            eur = tsp.simulatedannealing()
            f.write(str(i + 1))
            f.write(') temperatura inziale : ')
            f.write(str(t_in[i]))
            f.write('\n temperatura finale : ')
            f.write(str(t_fin))
            f.write('\n alpha :')
            f.write(str(alpha))
            f.write('\n iterazioni alla stessa temperatura : ')
            f.write(str(L))
            f.write('\n Esito euristica :')
            f.write(str(eur))
            f.write('\n')
            print(i, "\n")

    indice_linea_dimensione = 4
    indice_inizio_linee_coordinate = 7
    coordinate, dimensione = leggi_coordinate("IstanzeBenchmark/rl5934.tsp.txt", indice_linea_dimensione, indice_inizio_linee_coordinate)
    b = 554070.556050  # 19947008.20167722 #239297 #2579 #3323  # best solution istanza benchmark
    L = 280
    t_in = [10**i for i in range(1,11)]
    t_fin = 1
    alpha = 0.99
    print("rl5934\n")


    with open("Test/nearest_neighbour_rl5934/test_ordini_di_grandezza_vm1084_v1.txt", 'w') as f:
        f.write('test for nearest_neighbour_rl5934_v1.txt : \n')
        print("primo \n")
        for i in range(0,10):
            tsp = TSP(coordinate,t_in[i],t_fin,alpha,L)
            eur = tsp.simulatedannealing()
            f.write(str(i+1))
            f.write(') temperatura inziale : ')
            f.write(str(t_in[i]))
            f.write('\n temperatura finale : ')
            f.write(str(t_fin))
            f.write('\n alpha :')
            f.write(str(alpha))
            f.write('\n iterazioni alla stessa temperatura : ')
            f.write(str(L))
            f.write('\n Esito euristica :')
            f.write(str(eur))
            f.write('\n')
            print(i,"\n")

    with open("Test/nearest_neighbour_rl5934/test_ordini_di_grandezza_rl5934_v2.txt", 'w') as f:
        f.write('test for nearest_neighbour_rl5934_v2.txt : \n')
        print("secondo \n")
        for i in range(0, 10):
            tsp = TSP(coordinate, t_in[i], t_fin, alpha, L)
            eur = tsp.simulatedannealing()
            f.write(str(i + 1))
            f.write(') temperatura inziale : ')
            f.write(str(t_in[i]))
            f.write('\n temperatura finale : ')
            f.write(str(t_fin))
            f.write('\n alpha :')
            f.write(str(alpha))
            f.write('\n iterazioni alla stessa temperatura : ')
            f.write(str(L))
            f.write('\n Esito euristica :')
            f.write(str(eur))
            f.write('\n')
            print(i, "\n")

    with open("Test/nearest_neighbour_rl5934/test_ordini_di_grandezza_rl5934_v3.txt", 'w') as f:
        f.write('test for nearest_neighbour_rl5934_v3.txt : \n')
        print("terzo \n")
        for i in range(0, 10):
            tsp = TSP(coordinate, t_in[i], t_fin, alpha, L)
            eur = tsp.simulatedannealing()
            f.write(str(i + 1))
            f.write(') temperatura inziale : ')
            f.write(str(t_in[i]))
            f.write('\n temperatura finale : ')
            f.write(str(t_fin))
            f.write('\n alpha :')
            f.write(str(alpha))
            f.write('\n iterazioni alla stessa temperatura : ')
            f.write(str(L))
            f.write('\n Esito euristica :')
            f.write(str(eur))
            f.write('\n')
            print(i, "\n")
            
'''''''''''''''''''''''''''''''''
