
def leggi_coordinate(path,indice_linea_dimensione,indice_inizio_linee_coordinate):

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