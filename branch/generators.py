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
