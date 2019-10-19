import numpy as np


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

