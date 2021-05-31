from TSP import TSP
from leggi_coordinate import leggi_coordinate


if __name__ == "__main__":
    indice_linea_dimensione = 4
    indice_inizio_linee_coordinate = 7
    coordinate, dimensione = leggi_coordinate("a280.txt",indice_linea_dimensione,indice_inizio_linee_coordinate)
    b = 554070.556050  # 19947008.20167722 #239297 #2579 #3323  # best solution istanza benchmark
    L = [i*10 for i in range(1,30)]
    t_in = 10000
    t_fin = 1
    alpha = 0.92
    with open("Test/a280/test_alpha_0.92_only_L_a280v1.txt", 'w') as f:
        f.write('test for a280.txt : \n')
        for i in range(0,29):
            tsp = TSP(coordinate,t_in,t_fin,alpha,L[i])
            eur = tsp.simulatedannealing()
            f.write(str(i+1))
            f.write(') temperatura inziale : ')
            f.write(str(t_in))
            f.write('\n temperatura finale : ')
            f.write(str(t_fin))
            f.write('\n alpha :')
            f.write(str(alpha))
            f.write('\n iterazioni alla stessa temperatura : ')
            f.write(str(L[i]))
            f.write('\n Esito euristica :')
            f.write(str(eur))
            f.write('\n')
    L = [i * 10 for i in range(1, 30)]
    t_in = 10000
    t_fin = 1
    alpha = 0.92
    with open("Test/a280/test_alpha_0.92_only_L_a280v2.txt", 'w') as f:
        f.write('test for a280.txt : \n')
        for i in range(0, 29):
            tsp = TSP(coordinate, t_in, t_fin, alpha, L[i])
            eur = tsp.simulatedannealing()
            f.write(str(i + 1))
            f.write(') temperatura inziale : ')
            f.write(str(t_in))
            f.write('\n temperatura finale : ')
            f.write(str(t_fin))
            f.write('\n alpha :')
            f.write(str(alpha))
            f.write('\n iterazioni alla stessa temperatura : ')
            f.write(str(L[i]))
            f.write('\n Esito euristica :')
            f.write(str(eur))
            f.write('\n')



