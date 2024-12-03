## TODO: Complete the code

# Add a profiling step using TimeAndSpaceProfiler
def profile_with_metrics(func, arr):
    """
    Profiles the function using TimeAndSpaceProfiler and returns the metrics.
    """
    profiler = TimeAndSpaceProfiler()
    # Create a copy of the array to avoid modifying the original during profiling
    arr_copy = arr.copy()
    profile_result = profiler.profile(func, arr_copy)  # Profile the sorting function
    metrics = func(arr_copy)  # Get metrics from the sorting function
    profile_result.update({
        "comparison_count": metrics.comparison_count,
        "move_count": metrics.move_count
    })
    return profile_result

# Benchmarking
profiler = TimeAndSpaceProfiler()
results = []

# Create a tqdm progress bar for tracking the experiments
total_iterations = len(funcs) * len(lengths) * nbr_experiments * 3  # 3 for random, sorted, inverse_sorted
with tqdm(total=total_iterations, desc="Benchmarking", unit="experiment") as pbar:

    for func in funcs:
        for size, random_experiments, sorted_experiments, inverse_sorted_experiments in zip(
            lengths, random_arrays, sorted_arrays, inverse_sorted_arrays
        ):
            for experiment_idx in range(nbr_experiments):
                for data, label in [
                    (random_experiments[experiment_idx], "random"),
                    (sorted_experiments[experiment_idx], "sorted"),
                    (inverse_sorted_experiments[experiment_idx], "inverse_sorted"),
                ]:
                    # Run and profile
                    logs = profile_with_metrics(func, data)
                    logs.update({
                        "algorithm": func.__name__,
                        "data_type": label,
                        "size": size,
                        "experiment": experiment_idx + 1,
                    })
                    results.append(logs)

                    # Update tqdm progress bar with custom message
                    pbar.set_postfix({
                        'algorithm': func.__name__,
                        'data_type': label,
                        'size': size,
                        'experiment': experiment_idx + 1,
                    })
                    pbar.update(1)
