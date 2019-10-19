import branch 

if __name__ == "__main__":
  print("Running default process: Poisson with mean 1.0 children per parent per generation,")
  print("  for 30 generations,")
  print("  starting with a population of 100,")
  print("  plotting the population each time.")
  print("")
  branch.run_generations(
    initial_population = 50,
    number_of_generations = 30,
    sibling_counts_callback = branch.plot_population,
  )
  print("")

  print("Doing the same thing, but for a process with mean 0.96 children per parent.")
  print("")
  generator = branch.poisson_children_generator(mean_children_per_parent = 0.96)
  branch.run_generations(
    initial_population = 50,
    number_of_generations = 30,
    generate_child_counts = generator,
    sibling_counts_callback = branch.plot_population,
  )
  print("")

  print("Run the default process with an initial population of 5,")
  print("  printing the raw array containing the number of children from each parent.")
  print("  Occasionally this will run for a huge number of generations. Exercise: When and why?")
  print("")
  branch.run_generations(
    initial_population = 5,
    sibling_counts_callback = lambda sibling_counts: print(sibling_counts),
  )
  print("")

  print("Doing the same thing, but using the built in sibling printer,")
  print("  printing the children that come from each parent as '.' characters,")
  print("  where each set of siblings is separated by a '|' character.")
  print("")
  branch.run_generations(
    initial_population = 5,
    sibling_counts_callback = branch.print_siblings,
  )
  print("")

  print("Run a Bernoulli child generating process,")
  print("  with 0.5 probability of generating 2 children per parent,")
  print("  generating 0 children otherwise,")
  print("  plotting the population of each generation.")
  print("  This wil also sometimes runaway in number of generations. Exercise: When and why?")
  print("")
  generator = branch.coinflip_for_children_generator()
  branch.run_generations(
    initial_population = 5,
    generate_child_counts = generator,
    sibling_counts_callback = branch.plot_population,
  )
  print("")

  print("Do the same thing, but with a 0.25 probability of generating 5 children,")
  print("  for 50 generations,")
  print("  starting with a population of 15,")
  print("  plotting the population on a logarithmic scale.")
  generator = branch.coinflip_for_children_generator(
    probability_of_success = 0.25,
    number_of_children_on_success = 5,
  )
  branch.run_generations(
    initial_population = 10,
    number_of_generations = 30,
    generate_child_counts = generator,
    sibling_counts_callback = branch.log_plot_population,
  )
  print("")
