# TSP-SimulatedAnnealing
Simulated Annealing algorithm to solve Symmetric Travelling Salesman Problem in Python.

Implementazione di un algoritmo Simulated Annealing per la soluzione del problema del commesso viaggiatore TSP Problem.   
Su istanze di piccole dimensioni, confronta i risultati ottenuti con l’euristica con quelli ottenuti mediante un 
approccio esatto.

### Link per istanze benchmark
http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsplib.html

### Cooling schedules
PARAMETRI DI DEFAULT:

	0.  MOSSA: 2-opt.
	1.  Soluzione iniziale: algoritmo greedy nearest neighbour.
	2.  T0: 10*|f0/2| (dove f0 è il valore della soluzione iniziale)
	3.  TF: 10^-4*|f0|
	4.  Lk: Lk = L = costante = n (dove n è la dimensione dell'istanza del problema, cioè il numero di nodi del grafo)
	5.  Quanto decrementare Tk, legge di decremento (successione Tk): Tk+1 = \alpha Tk. Con \alpha < 1. \alpha è elevato (es. 0.99) per Lk basso, mentre \alpha è basso (es. 0.8) per Lk elevato
![TSP_Berlin](https://user-images.githubusercontent.com/58850779/120661639-bff47f00-c488-11eb-9e3e-13b046a16a4e.png)
