import genes
import itertools
from timeit import default_timer as timer
from datetime import timedelta
from sys import exit


population: genes.Kromozom = [] 

def main():
  population = genes.createFirstPopulation()
  # population.append(genes.Kromozom([[0,0],[0,1],[2,6],[3,3],[4,4],[5,5],[6,6],[7,5]], 0))
  # population.append(genes.Kromozom([[0,2],[1,4],[2,2],[3,0],[4,3],[5,1],[6,7],[7,7]], 0))
  #population.append(genes.Kromozom([[0,2],[1,4],[2,6],[3,0],[4,3],[5,1],[6,7],[7,5]], 0))

  for k in range(0, len(population)):
    intersectionCount = genes.crossIntersection(population[k].gene)
    intersectionCount += genes.hvIntersection(population[k].gene)
    population[k].rank += intersectionCount


  ## Sort And Check if there is a solution in starting population
  population.sort(key=lambda x: x.rank)
  if population[0].rank == 0:
    print("Solution found: ", population[0].gene)
    exit()

  ## Print Listed Population 
  for k in range(0, len(population)):
    print(population[k].gene, population[k].rank)

  startAll = timer()
  crossQueue = itertools.combinations(population, 2)

  count = 0

  for i in range(1, len(population)):
    for j in range (0 , i):
      print("\nFirst Gene Index: ", j, "Second Gene Index: ", i)
      crossed = genes.cross(population[j], population[i])

      for k in crossed:
        count += 1

        intersectionCount = genes.crossIntersection(k)
        intersectionCount += genes.hvIntersection(k)
        if intersectionCount == 0:
          endAll = timer()
          print("\nIn", count, "Steps,", endAll-startAll, "Seconds\n Solution found: ", k)
          exit()



  
  

  
    
main()





