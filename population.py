from Dna import *
class Population1:

    def __init__(self, *args):#Target_phrase, Mutation rate, Population Size
        self.population = []
        self.MatingPool = []
        self.generations = 0

        self.finished = False
        self.target = args[0]
        self.MutationRate = args[1]
        self.perfectscore = 1

        self.best = ""
        self.PopSize = args[2]
        self.population = []
        for i in range(self.PopSize):
            temp = DNA1(len(self.target))
            self.population.append(temp)
        self.MatingPool = []
        self.bestOfThis = ""
        self.CalcFitness()

    def CalcFitness(self):
        for i in self.population:
            i.CalcFitness(self.target)

    def NaturalSelection(self):
        self.MatingPool = []
        MaxFitness = 0
        for i in self.population:
            if i.fitness > MaxFitness:
                MaxFitness = i.fitness
                self.bestOfThis = i

        """Adding Parents to the mating Pool According to their fitness"""
        for x in self.population:
            temp = (x.fitness*100)/MaxFitness
            for y in range(int(temp)):
                self.MatingPool.append(x)
        random.shuffle(self.MatingPool)

    def generate(self):
        self.population.clear()
        self.population.append(self.bestOfThis)
        for i in range(self.PopSize-1):
            a = random.choice(self.MatingPool)
            b = random.choice(self.MatingPool)

            child = a.crossover(b)
            child.mutate(self.MutationRate)
            self.population.append(child)
        self.generations += 1

    def GetBest(self):
        return self.best

    def evaluate(self):
        worldrecord = 0.0
        index = 0
        for i,j in enumerate(self.population):
            if j.fitness > worldrecord:
                worldrecord = j.fitness
                index = i
        self.best = self.population[index].getPhrase()
        if worldrecord == self.perfectscore:
            self.finished = True

    def getAverageFitness(self):
        total = 0
        for i in self.population:
            total += i.fitness
        return total / self.PopSize

    def AllPhrases(self):
        for i in self.population:
            print(i)
