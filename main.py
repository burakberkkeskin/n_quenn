import random
import genes
import itertools
from timeit import default_timer as timer
from datetime import timedelta


population: genes.Kromozom = [] 

def main():
  population = genes.createFirstPopulation()
  #population.append(genes.Kromozom([[0,0],[0,1],[2,6],[3,3],[4,4],[5,5],[6,6],[7,5]], 0))
  #population.append(genes.Kromozom([[0,2],[1,4],[2,2],[3,0],[4,3],[5,1],[6,7],[7,7]], 0))
  #population.append(genes.Kromozom([[0,2],[1,4],[2,6],[3,0],[4,3],[5,1],[6,7],[7,5]], 0))

  for i in range(0, len(population)):
    #intersectionCount = genes.crossIntersection(population[i].gene)
    intersectionCount = genes.hvIntersection(population[i].gene)
    population[i].rank += intersectionCount


  ## Sort And Check if there is a solution in starting population
  population.sort(key=lambda x: x.rank)
  if population[0].rank == 0:
    print("Solution found in starting population: ", population[0].gene)
    exit()

  ## Print Listed Population 
  for i in range(0, len(population)):
    print(population[i].gene, population[i].rank)

  startAll = timer()
  crossQueue = itertools.combinations(population, 2)


  for kromozoms in crossQueue:
    count = 0

    # crossStartTime = timer()
    crossed = genes.cross(kromozoms[0], kromozoms[1])
    # crossEndTime = timer()
    # print("Combine took: ", timedelta(seconds=crossEndTime-crossStartTime))

    for i in crossed:
      count += 1

      # checkCrossStartTime = timer()
      #intersectionCount = genes.crossIntersection(i)
      intersectionCount = genes.hvIntersection(i)
      # checkCrossEndTime = timer()
      # print("Check took: ", timedelta(seconds=checkCrossEndTime-checkCrossStartTime))
      if intersectionCount == 0:
        endAll = timer()
        print("\nIn", endAll-startAll, "Seconds\n Solution found: ", i)
        exit()



  
  

  
    
main()





