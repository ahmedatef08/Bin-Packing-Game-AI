def bin_packing_backtracking(item_sizes, bin_capacity, num_bins):
    def backtracking_util(current_bin, remaining_items):
        nonlocal best_solution, best_num_bins

        if not remaining_items:
            # All items have been packed
            if current_bin < best_num_bins:
                best_num_bins = current_bin
                best_solution = bin_assignment.copy()
            return

        for bin_index in range(num_bins):
            if bin_capacity[bin_index] >= remaining_items[0][1]:  # Check item size instead of item value
                # Try placing the item in the current bin
                bin_capacity[bin_index] -= remaining_items[0][1]
                bin_assignment[remaining_items[0][0]] = (bin_index, remaining_items[0][1])

                backtracking_util(current_bin, remaining_items[1:])

                # Backtrack
                bin_capacity[bin_index] += remaining_items[0][1]
                bin_assignment.pop(remaining_items[0][0], None)  # Use pop to avoid KeyError

    # Initialization
    best_solution = {}
    best_num_bins = float('inf')
    bin_assignment = {}

    items_with_sizes = list(enumerate(item_sizes, 1))  # Enumerate items with their sizes

    backtracking_util(0, items_with_sizes)

    # Return the actual number of bins used and the items in each bin
    return best_solution, len(set(location for location, size in best_solution.values()))