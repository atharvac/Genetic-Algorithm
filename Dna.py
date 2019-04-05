import random
import string

class DNA1:
    def __init__(self,*args):#Length of phrase
        temp = []
        self.txtlen = args[0]
        for x in range(self.txtlen):
            temp.append(self.NewRandomChar())
        self.genes = ''.join(temp)
        self.fitness = 0

    def __repr__(self):
        return self.genes

    def crossover(self,parent2):
        child = DNA1(self.txtlen)
        i = random.randrange(self.txtlen+1)
        child.genes = self.genes[:i] + self.genes[i:]
        return child

    def mutate(self,MutationRate):
        MutationRate_ = MutationRate * 100
        for i in range(self.txtlen):
            k = random.randrange(0,100)
            if k < MutationRate_:
                temp_str = self.genes[:i] + self.NewRandomChar() + self.genes[i+1:]
                self.genes = temp_str

    def CalcFitness(self,target):
        score = 0
        for i in range(self.txtlen):
            if self.genes[i] == target[i]:
                score += 1
        self.fitness = score / len(target)

    def NewRandomChar(self):
        temp = string.ascii_letters
        temp = list(temp)
        temp.append(" ")
        temp.append(".")
        return random.choice(temp)

    def getPhrase(self):
        return "".join(self.genes)
