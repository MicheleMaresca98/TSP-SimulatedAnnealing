# TSP-SimulatedAnnealing
Simulated Annealing algorithm to solve Symmetric Travelling Salesman Problem in Python.
## Traccia
Implementare un algoritmo di Simulating Annealing per la soluzione del problema del commesso viaggiatore TSP Problem.   
Su istanze di piccole dimensioni, confrontare i risultati ottenuti con l’euristica con quelli ottenuti mediante un 
approccio esatto.

### Link per istanze benchmark
http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsplib.html

### TODO
1. Cooling schedules

### Cooling schedules
PROPOSTE INIZIALI:

	0.  MOSSA: 2-opt.
	1.  Soluzione iniziale: random, oppure data in uscita da un algoritmo greedy.
	2.  T0: 10*|f0/2| (dove f0 è il valore della soluzione iniziale)
	3.  TF: 10^-4*|f0|
	4.  Lk: Lk = L = costante = n (dove n è la dimensione dell'istanza del problema, cioè il numero di nodi del grafo)
	5.  Quanto decrementare Tk, legge di decremento (successione Tk): Tk+1 = \alpha Tk. Con \alpha < 1. \alpha è elevato (es. 0.99) per Lk basso, mentre \alpha è basso (es. 0.8) per Lk elevato
2, 3, 4 sono proposte iniziali, poi in fase di cooling schedules bisogna provare a migliorarli facendo prove su istanze benchmark.
![TSP](https://user-images.githubusercontent.com/58850779/120634123-2e2a4900-c46b-11eb-8d82-a6389f0eef19.png)
