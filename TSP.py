import math
import random
import visualize_tsp


class TSP(object):
    def __init__(self, coordinate, temperatura_iniziale=-1, temperatura_finale=-1, alpha=-1, L=-1):
        self.coordinate = coordinate
        self.N = len(coordinate)
        self.L = self.N if L == -1 else L
        self.temperatura_iniziale = temperatura_iniziale  # serve il valore della soluzione iniziale
        self.temperatura_finale = temperatura_finale  # serve il valore della soluzione iniziale
        self.T = self.temperatura_iniziale
        self.alpha = ((0.99 if self.L < 10000 else 0.8) if alpha == -1 else alpha)
        self.nodi = [i for i in range(self.N)]
        # self.distanze = {(n1, n2): self.calcolo_distanza(n1, n2) for n1 in self.nodi for n2 in self.nodi if n1 != n2}
        self.best_solution = None
        self.best_objective = float("Inf")
        self.current_solution = None
        self.current_objective = float("Inf")
        self.iterazione = 1  # iterazione con valore di temperatura fisso

    def calcolo_soluzione_iniziale(self):
        current_node = random.choice(self.nodi)
        solution = [current_node]
        free_nodes = set(self.nodi)
        free_nodes.remove(current_node)
        while free_nodes:
            next_node = min(free_nodes, key=lambda x: self.calcolo_distanza(current_node, x))
            free_nodes.remove(next_node)
            solution.append(next_node)
            current_node = next_node
        current_obj = self.funzione_obiettivo(solution)
        self.best_objective = current_obj
        self.best_solution = solution
        self.current_objective = current_obj
        self.current_solution = solution

        if self.temperatura_iniziale == -1:
            self.temperatura_iniziale = 10 * abs(self.best_objective / 2.0)
            self.T = self.temperatura_iniziale
        if self.temperatura_finale == -1:
            self.temperatura_finale = 10 ** (-4) * abs(self.best_objective)

    def funzione_obiettivo(self, solution):
        current_obj = 0
        for i in range(self.N):
            current_obj += self.calcolo_distanza(solution[i % self.N], solution[(i + 1) % self.N])
        return current_obj

    def calcolo_distanza(self, nodo1, nodo2):
        n1, n2 = self.coordinate[nodo1], self.coordinate[nodo2]
        return math.sqrt(((n1[0] - n2[0]) ** 2) + ((n1[1] - n2[1]) ** 2))

    def calcolo_probabilita_accettazione(self, candidate):
        candidate_objective = self.funzione_obiettivo(candidate)
        if candidate_objective <= self.current_objective:
            self.current_solution, self.current_objective = candidate, candidate_objective
            if candidate_objective <= self.best_objective:
                self.best_solution, self.best_objective = candidate, candidate_objective
        else:
            if random.random() < math.exp(-(candidate_objective - self.current_objective) / self.T):
                self.current_solution, self.current_objective = candidate, candidate_objective

    def avanza_T(self):
        if self.iterazione == self.L:
            self.iterazione = 1
            self.T *= self.alpha
        else:
            self.iterazione += 1

    def mossa2_opt(self, candidate):
        i = random.randint(0, self.N - 1)
        free_nodes = list(candidate)
        free_nodes.remove(candidate[i])
        free_nodes.remove(candidate[i - 1] if i > 0 else candidate[self.N - 1])
        free_nodes.remove(candidate[i + 1] if i < (self.N - 1) else candidate[0])
        j = random.choice(free_nodes)
        if i < j:
            candidate[i:j] = reversed(candidate[i:j])
        else:
            candidate[j:i] = reversed(candidate[j:i])

    def simulatedannealing(self):
        self.calcolo_soluzione_iniziale()
        while self.T >= self.temperatura_finale:  # si potrebbe
            # aggiungere anche un contatore assoluto di iterazioni
            # per non farne troppe
            candidate = list(self.current_solution)
            # mossa 2-opt
            self.mossa2_opt(candidate)
            self.calcolo_probabilita_accettazione(candidate)
            self.avanza_T()
        print("Miglior risultato ottenuto: ", self.best_objective)
        print("Tour: ", self.best_solution)
        return self.best_objective

    def visualizza_tour(self):
        tour = list(self.best_solution)
        visualize_tsp.plotTSP([tour], self.coordinate)
