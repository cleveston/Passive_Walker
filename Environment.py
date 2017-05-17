import random

class Environment(object):
    def __init__(self, kind, population=None, size=100, maxgenerations=100, generation=0, crossover_rate=0.90, mutation_rate=0.02, optimum=None):

        # Start the parameters
        self.kind = kind
        self.size = size
        self.optimum = optimum
        self.population = population or self._makepopulation()
        for individual in self.population:
            individual.evaluate(self.optimum)
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.maxgenerations = maxgenerations
        self.generation = generation

    def _makepopulation(self):
        return [self.kind() for individual in range(self.size)]

    def run(self):
        while not self._goal():
            self._step()

    def _goal(self):
        return self.generation > self.maxgenerations or self.best.score >= self.optimum

    def _step(self):
        self.population.sort(key=lambda a: a.score, reverse=True)
        self._crossover()
        self.generation += 1
        self.report()

    def _crossover(self):
        next_population = [self.best.copy()]
        while len(next_population) < self.size:
            mate1 = self._select()
            if random.random() < self.crossover_rate:
                mate2 = self._select()
                offspring = mate1.crossover(mate2)
            else:
                offspring = [mate1.copy()]
            for individual in offspring:
                self._mutate(individual)
                individual.evaluate(self.optimum)
                next_population.append(individual)
        self.population = next_population[:self.size]

    def _select(self):
        return self._tournament()

    def _mutate(self, individual):
        for gene in range(individual.length):
            if random.random() < self.mutation_rate:
                individual.mutate(gene)

    def _tournament(self, size=8, choosebest=0.90):
        competitors = [random.choice(self.population) for i in range(size)]
        competitors.sort(key=lambda a: a.score, reverse=True)
        if random.random() < choosebest:
            return competitors[0]
        else:
            return random.choice(competitors[1:])

    def best():
        doc = "individual with best fitness score in population."

        def fget(self):
            return self.population[0]
        return locals()
    best = property(**best())

    def report(self):
        print("=" * 70)
        print("generation: ", self.generation)
        print("best:       ", self.best)
