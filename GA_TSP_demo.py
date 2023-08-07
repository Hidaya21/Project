from  GeneticAlgorithmTSP import GA
import Graph2



# great a graph between cities, a, b,c and d. 
graph = Graph2.Graph()
graph.setAdjacent('a', 'b', 4)
graph.setAdjacent('a', 'c', 4)
graph.setAdjacent('a', 'd', 7)
graph.setAdjacent('a', 'e', 3)
graph.setAdjacent('b', 'c', 2)
graph.setAdjacent('b', 'd', 3)
graph.setAdjacent('b', 'e', 5)
graph.setAdjacent('c', 'd', 2)
graph.setAdjacent('c', 'e', 3)
graph.setAdjacent('d', 'e', 6)


ga_tsp = GA(generations=20, population_size=7, tournamentSize=2, mutationRate=0.2, elitismRate=0.1)

optimal_path, path_cost = ga_tsp.optimize(graph)
print ('\nPath: {0}, Cost: {1}'.format(optimal_path, path_cost))