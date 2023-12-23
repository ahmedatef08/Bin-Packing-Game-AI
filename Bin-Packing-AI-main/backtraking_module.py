def bin_packing_backtracking(items, bins):
    all_solutions = []

    def backtracking_util(current_bin, remaining_items, bin_assignment, all_solutions):
        nonlocal best_solution, best_num_bins

        if not remaining_items:
            # All items have been packed
            if current_bin < best_num_bins:
                best_num_bins = current_bin
                best_solution = bin_assignment.copy()
            return

        for a_bin in bins:
            if a_bin.height >= remaining_items[0].width:  # Check item size instead of item value
                a_bin.height -= remaining_items[0].width
                bin_assignment[remaining_items[0].index] = (a_bin, remaining_items[0])
                all_solutions.append(bin_assignment.copy())  # Append a copy to avoid modifying the same dictionary
                backtracking_util(current_bin, remaining_items[1:], bin_assignment, all_solutions)

                # Backtrack
                a_bin.height += remaining_items[0].width
                bin_assignment.pop(remaining_items[0].index, None)  # Use pop to avoid KeyError

    # Initialization
    best_solution = {}
    best_num_bins = float('inf')
    bin_assignment = {}

    backtracking_util(0, items, bin_assignment, all_solutions)

    # Return the actual number of bins used, the items in each bin, and all solutions
    return best_solution, len(set(location for location, size in best_solution.values())), all_solutions
