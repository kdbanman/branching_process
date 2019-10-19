import numpy as np

def poisson_children_generator(mean_children_per_parent = 1.0):

  def generate_child_counts(number_of_parents):
    return np.random.poisson(lam = mean_children_per_parent, size = number_of_parents)
  
  return generate_child_counts

def coinflip_for_children_generator(probability_of_success = 0.5, number_of_children_on_success = 2.0):

  def generate_child_counts(number_of_parents):
    successes_per_parent = np.random.binomial(1, probability_of_success, number_of_parents)
    return number_of_children_on_success * successes_per_parent
  
  return generate_child_counts


def run_generations(number_of_generations = -1,
                    initial_population = 1,
                    generate_child_counts = poisson_children_generator(1.0),
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


def print_siblings(sibling_counts):
  rendered_siblings = ""
  for sibling_count in sibling_counts:
    rendered_siblings += str(sibling_count) * sibling_count + " | "

  print(rendered_siblings[:-1])

def plot_population(sibling_counts):
  population_size = int(np.sum(sibling_counts))

  if population_size < 100:
    print("{:>8} ".format(population_size) + "*" * population_size)
  else:
    print("{:.2E} ".format(population_size) + "*" * 97 + "...")

def log_plot_population(sibling_counts):
  population_size = int(np.sum(sibling_counts))

  if population_size == 0:
    print("")
  else:
    print("{:.2E} ".format(population_size) + "*" * int(np.floor(np.log2(population_size))))
  

if __name__ == "__main__":
  print("Running default process: Poisson with mean 1.0 children per parent per generation,")
  print("  for 30 generations,")
  print("  starting with a population of 100,")
  print("  plotting the population each time.")
  print("")
  run_generations(
    initial_population = 50,
    number_of_generations = 30,
    sibling_counts_callback = plot_population,
  )
  print("")

  print("Doing the same thing, but for a process with mean 0.96 children per parent.")
  print("")
  run_generations(
    initial_population = 50,
    number_of_generations = 30,
    generate_child_counts = poisson_children_generator(mean_children_per_parent = 0.96),
    sibling_counts_callback = plot_population,
  )
  print("")

  print("Run the default process with an initial population of 5,")
  print("  printing the raw array containing the number of children from each parent.")
  print("  Occasionally this will run for a huge number of generations. Exercise: When and why?")
  print("")
  run_generations(
    initial_population = 5,
    sibling_counts_callback = lambda sibling_counts: print(sibling_counts),
  )
  print("")

  print("Doing the same thing, but using the built in sibling printer,")
  print("  printing the children that come from each parent as '.' characters,")
  print("  where each set of siblings is separated by a '|' character.")
  print("")
  run_generations(
    initial_population = 5,
    sibling_counts_callback = print_siblings,
  )
  print("")

  print("Run a Bernoulli child generating process,")
  print("  with 0.5 probability of generating 2 children per parent,")
  print("  generating 0 children otherwise,")
  print("  plotting the population of each generation.")
  print("  This wil also sometimes runaway in number of generations. Exercise: When and why?")
  print("")
  run_generations(
    initial_population = 5,
    generate_child_counts = coinflip_for_children_generator(),
    sibling_counts_callback = plot_population,
  )
  print("")

  print("Do the same thing, but with a 0.25 probability of generating 5 children,")
  print("  for 50 generations,")
  print("  starting with a population of 15,")
  print("  plotting the population on a logarithmic scale.")
  run_generations(
    initial_population = 10,
    number_of_generations = 30,
    generate_child_counts = coinflip_for_children_generator(probability_of_success = 0.25, number_of_children_on_success = 5),
    sibling_counts_callback = log_plot_population,
  )
  print("")
