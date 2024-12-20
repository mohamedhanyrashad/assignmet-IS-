import random

def fitness_function(x):
    """Define the fitness function: f(x) = x^2"""
    return x**2

def generate_population(size, lower_bound, upper_bound):
    """Generate an initial population of random individuals."""
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def select_parents(population, fitnesses):
    """Select two parents using roulette wheel selection."""
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    parents = random.choices(population, probabilities, k=2)
    return parents

def crossover(parent1, parent2):
    """Perform single-point crossover."""
    crossover_point = random.randint(0, len(bin(max(parent1, parent2))) - 2)
    mask = (1 << crossover_point) - 1
    child1 = (parent1 & mask) | (parent2 & ~mask)
    child2 = (parent2 & mask) | (parent1 & ~mask)
    return child1, child2

def mutate(individual, mutation_rate, lower_bound, upper_bound):
    """Perform mutation with a given mutation rate."""
    if random.random() < mutation_rate:
        return random.randint(lower_bound, upper_bound)
    return individual

def genetic_algorithm(
    population_size, generations, mutation_rate, lower_bound, upper_bound
):
    """Run the genetic algorithm."""
    population = generate_population(population_size, lower_bound, upper_bound)

    for generation in range(generations):
        fitnesses = [fitness_function(ind) for ind in population]
        new_population = []

        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate, lower_bound, upper_bound)
            child2 = mutate(child2, mutation_rate, lower_bound, upper_bound)
            new_population.extend([child1, child2])

        population = new_population
        best_individual = max(population, key=fitness_function)
        print(
            f"Generation {generation + 1}: Best Individual = {best_individual}, Fitness = {fitness_function(best_individual)}"
        )

    return max(population, key=fitness_function)

# Parameters
population_size = 20
generations = 50
mutation_rate = 0.1
lower_bound = 0
upper_bound = 31

# Run the genetic algorithm
best_solution = genetic_algorithm(population_size, generations, mutation_rate, lower_bound, upper_bound)
print(f"Best solution found: {best_solution}, Fitness: {fitness_function(best_solution)}")
