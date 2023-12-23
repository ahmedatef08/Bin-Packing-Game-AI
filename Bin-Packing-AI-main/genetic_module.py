import random


def initialize_population(population_size, items, bins, num_bins, bin_capacity):
    population = []
    k = 0
    checkt = 0
    while k < population_size:
        # print(checkt)
        # Initialize an empty configuration of bins
        solution = [[bins[0], []] for _ in range(num_bins)]
        # Randomly assign items to bins, ensuring capacity constraints
        for item in items:
            bin_index = random.randint(0, num_bins - 1)
            if checkt == 100000:
                return []
            # Check if adding the item would exceed the bin capacity
            count = 0
            flag = False
            sumofbin = 0
            for im in solution[bin_index][1]:
                sumofbin += im.width

            while sumofbin + item.width > bin_capacity:
                # If it does, choose another bin
                bin_index = random.randint(0, num_bins - 1)
                count += 1
                if count == 1000:
                    flag = True
                    break
                sumofbin = 0
                for im in solution[bin_index][1]:
                    sumofbin += im.width
            if flag == True:
                continue
            # Add the item to the selected bin
            solution[bin_index][1].append(item)
            solution[bin_index][0] = bins[bin_index]
        total_sum = 0
        for so in solution:
            for s2 in so[1]:
                total_sum += s2.width
        checkt += 1
        sumofitems = 0
        for item in items:
            sumofitems += item.width
        if total_sum != sumofitems:
            continue
        k += 1
        fit = fitness(solution)
        population.append({'solution': solution,
                           'fit': fit})

    return population


def fitness(solution):
    total_bins = len(solution)

    # Count the number of empty bins
    empty_bins = 0
    for so in solution:
        if len(so[1]) == 0:
            empty_bins += 1
    # Apply a penalty for each empty bin
    penalty = empty_bins

    # Calculate the fitness as the total number of used bins minus the penalty
    fitness_value = total_bins - penalty

    return fitness_value


def mutat(solution):
    # Extract the solution details
    bins = solution['solution']
    fit = solution['fit']

    # Choose a random bin and item
    random_bin_index = random.randint(0, len(bins) - 1)
    random_item_index = random.randint(0, len(bins[random_bin_index][1]) - 1)

    # Remove the randomly chosen item from its current bin
    item_to_move = bins[random_bin_index][1].pop(random_item_index)

    # Choose a different random bin for the item
    new_bin_index = random.randint(0, len(bins) - 1)

    # Add the item to the new bin
    bins[new_bin_index][1].append(item_to_move)

    # Update the fitness value (number of used bins)
    new_fit = fit

    return {'solution': bins, 'fit': new_fit}


def crossover(parent1, parent2):
    item_to_bin_mapping1 = {}

    # Iterate through the list representation and populate the dictionary
    for bin_object, item_list in parent1:
        for item_object in item_list:
            item_to_bin_mapping1[item_object] = bin_object
    item_to_bin_mapping2 = {}

    # Iterate through the list representation and populate the dictionary
    for bin_object, item_list in parent2:
        for item_object in item_list:
            item_to_bin_mapping2[item_object] = bin_object
    child = {}

    # Select a random crossover point
    crossover_point = random.choice(list(item_to_bin_mapping1.keys()))

    # Create a child solution by inheriting items up to the crossover point from parent1
    for item, bin_object in item_to_bin_mapping1.items():
        child[item] = bin_object
        if item == crossover_point:
            break

    # Inherit the remaining items from parent2
    for item, bin_object in item_to_bin_mapping2.items():
        if item not in child:
            child[item] = bin_object
    c = remap_to_list(child)
    return {'solution': c, 'fit': fitness(c)}


def remap_to_list(child_solution):
    # Create a dictionary to store items for each bin
    bins_dict = {}

    # Iterate through the child solution and populate the bins_dict
    for item, bin_object in child_solution.items():
        if bin_object not in bins_dict:
            bins_dict[bin_object] = []
        bins_dict[bin_object].append(item)

    # Convert the dictionary to a list of bins
    list_of_bins = [[bin_object, items] for bin_object, items in bins_dict.items()]

    return list_of_bins


def gene(bins, items):
    population = initialize_population(100, items, bins, len(bins), bins[0].height)

    print(population)
    if len(population[0]) == 0:
        print("not solution")
    else:
        sorted_data = sorted(population, key=lambda x: x['fit'])
        print(sorted_data)
        best_popultion = sorted_data[0]
        usedpopulation = sorted_data[:16]
        for i in range(10000):
            for j in range(15):
                fromcross = crossover(usedpopulation[j]['solution'], usedpopulation[j + 1]['solution'])
                if i % 50 == 0 and j % 5 == 0:
                    fromcross = mutat(fromcross)
                sum = 0
                flag = True
                for n in fromcross['solution']:
                    for q in n[1]:
                        sum += q.width
                        if sum > fromcross['solution'][0][0].height:
                            flag = False
                    sum = 0
                if flag == True:
                    sorted_data.append(fromcross)
                # print(sorted_data[-1])
            sorted_data = sorted(usedpopulation, key=lambda x: x['fit'])
            # print(sorted_data[j]['fit'])
            usedpopulation = sorted_data[:16]
            best_popultion = sorted_data[0]

        return population, best_popultion
