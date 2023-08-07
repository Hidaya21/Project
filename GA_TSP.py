from  GeneticAlgorithmTSP import *
import Graph2
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances as ED


# read cities with coordinates from a csv file using pandas tool
cities = pd.read_csv('om.csv')
print(cities)
nbr_cities = cities.shape[0]

# get the data in a matrix
cities_mat = cities.values

# create an empty graph
graph = Graph2.Graph(graph_struct = {})


# ------------ Questions --------------
#--------------------------------------

# Questin A: 

# A1: pseudo-code: append the city-pairs to the graph with their respective eudclidean distances
# ------------
# 1. get a pair of cities from the matrix computed above
# 2. compute the distance ed between the two cities using ED of sklearn.

# you should provide an automatic way to append the cities and not manualy as 
# indicated in the demo 

# ----  your code here --------------
des = ED(cities_mat[:,2:])
citiesCode = cities_mat[:,1]
for i in range(len(citiesCode)):
    for j in range (i+1,len(citiesCode)):
        graph.setAdjacent(citiesCode[i], citiesCode[j], des[i,j])
        


# apply GA 
# 1. create the GA object with setting the parameters        
ga_tsp = GA(generations=10, population_size=7, tournamentSize=2, mutationRate=0.2, elitismRate=0.1)
    
# 2. optimize the GA on the graph created above
optimal_path, path_cost = ga_tsp.optimize(graph)

# display the path: a string of cityies codes 
print ('\nPath: {0}, Cost: {1}'.format(optimal_path, path_cost))

# A2: if the path found is for example 'fnhdkbigjclmea', then show 
# the path as follow:  Nizwa->Hamya->AlMazyuna->.....
# f for Nizwa, n for Hamya, h for AlWayzuna, etc.




# Questin B:
  
# B1. display the graph showin g the cities 
cities_coordinates  = cities.iloc[:,2:].values
plt.figure(figsize=(10,8))
plt.scatter(*zip(*cities_coordinates), marker='s', color='red')
plt.grid()

# B2. show the path found by the GA in optimal_path




# B3. Shown the names of the cities on the graph
