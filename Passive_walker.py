from Environment import Environment
from Individual import Individual


class Passive_walker:

    def __init__(self):

        # Create the environment
        environment = Environment(kind=Individual, size=100, maxgenerations=300, crossover_rate=0.90, mutation_rate=0.2, optimum=1050)

        # Find the best sample
        environment.run()

        # Get the best sample
        bestSample = environment.best

        # Show the best performance forever
        while True:
            bestSample.show()


# Start the algorithm
Passive_walker()
