# TSP-SimulatedAnnealing
Simulated Annealing algorithm to solve Symmetric Travelling Salesman Problem in Python.
## Traccia
Implementare un algoritmo di Simulating Annealing per la soluzione del problema del commesso viaggiatore TSP Problem.   
Su istanze di piccole dimensioni, confrontare i risultati ottenuti con l’euristica con quelli ottenuti mediante un 
approccio esatto.

### Link per istanze benchmark
http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsplib.html

### TODO
1. Risoluzione ottima del TSP per problemi di piccola dimensione con Gurobi con jupyter notebook. (FATTO)
   1. Fare lettura da file per prelevare le coordinate dei nodi. (FATTO)
2. Rifare algoritmo Greedy per trovare soluzione iniziale (vedere slide corso)
3. Rifare algoritmo SimulatedAnnealing 
4. Cooling schedules

### Cooling schedules
PROPOSTE INIZIALI:

	0.  MOSSA: 2-opt.
	1.  Soluzione iniziale: random, oppure data in uscita da un algoritmo greedy.
	2.  T0: 10*|f0/2| (dove f0 è il valore della soluzione iniziale)
	3.  TF: 10^-4*|f0|
	4.  Lk: Lk = L = costante = n (dove n è la dimensione dell'istanza del problema, cioè il numero di nodi del grafo)
	5.  Quanto decrementare Tk, legge di decremento (successione Tk)

2, 3, 4 sono proposte iniziali, poi in fase di cooling schedules bisogna provare a migliorarli facendo prove su istanze benchmark.
