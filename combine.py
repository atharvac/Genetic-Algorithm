from Dna import *
from population import *
import os

def main():
    Mutation_Rate = 0.01
    Target = "To be or not to be that is the question."
    Pop_size = 200
    p = Population1(Target, Mutation_Rate, Pop_size)
    pause = False
    while not pause:
        pause = loop(p)

def loop(p):
    p.NaturalSelection()
    p.generate()
    p.CalcFitness()
    p.evaluate()

    os.system("clear")

    p.AllPhrases()
    print("\nCurrent Best:",p.GetBest())
    print("Generation:",p.generations)

    if p.finished == True:
        return True
    return False

if __name__ == '__main__':
    main()
