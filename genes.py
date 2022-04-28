import random
import itertools

class Kromozom():
  def __init__(self, gene:list, rank:int):
    self.gene = gene
    self.rank = rank


def createFirstPopulation():
  population: Kromozom = []
  for i in range(0,32):
    firstParent = [0,1,2,3,4,5,6,7]
    secondParent = [0,1,2,3,4,5,6,7]
    gens = []
    for i in range(0,len(firstParent)):
      firstRandom = random.choice(firstParent)
      secondRandom = random.choice(secondParent)

      gen = [firstRandom, secondRandom]
      gens.append(gen)

      firstParent.remove(firstRandom)
      secondParent.remove(secondRandom)
    population.append(Kromozom(gens, 0))
  return population


def hvIntersection(gene):
  rank = 0
  for i in range(0, len(gene)):
    for j in range(i+1, len(gene)):
      if gene[i][0]==gene[j][0]:
        rank += 1
      if gene[i][1]==gene[j][1]:
        rank += 1
  return rank



def crossIntersection(gene):
  rank = 0
  for i in range(0, len(gene)):
    crossGenes:list = []
    for j in range(1, len(gene)+1):
      crossGenes.append([gene[i][0]+j, gene[i][1]+j])
      crossGenes.append([gene[i][0]+j, gene[i][1]-j])
      crossGenes.append([gene[i][0]-j, gene[i][1]+j])
      crossGenes.append([gene[i][0]-j, gene[i][1]-j])
    for crossGene in crossGenes:
      if crossGene in gene:
        rank += 1
  return rank

def cross(kromozom1:Kromozom, kromozom2:Kromozom):
  gen1 = kromozom1.gene
  gen2 = kromozom2.gene
  print("\nGen 1: ", gen1, "\nGen 2: ", gen2)
  
  combinedList = gen1+gen2 

  combinations = itertools.combinations(combinedList, len(gen1))
  return combinations



    

