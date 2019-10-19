import numpy as np

from branch import generators

def run_generations(number_of_generations = -1,
                    initial_population = 1,
                    generate_child_counts = generators.poisson_children_generator(1.0),
                    sibling_counts_callback = lambda _: None):
  sibling_counts = np.array([1] * initial_population)
  generation = 0
  while number_of_generations == -1 or generation < number_of_generations:
    sibling_counts_callback(sibling_counts)

    generation_size = int(np.sum(sibling_counts))
    if generation_size == 0:
      break

    sibling_counts = generate_child_counts(generation_size)
    generation += 1
