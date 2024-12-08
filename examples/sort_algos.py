import time
import tracemalloc
from collections import defaultdict

class TimeAndSpaceProfiler:
    def __init__(self):
        self.comparison_count = 0
        self.move_count = 0

    def profile(self, func, arr):
        """
        Profiles the function and tracks time and memory usage.
        """
        # Start memory tracking
        tracemalloc.start()

        # Start time tracking
        start_time = time.time()
        self.comparison_count = 0  # Reset comparison count before profiling
        self.move_count = 0  # Reset move count before profiling

        # Run the sorting function
        func(arr)

        # Stop time tracking
        end_time = time.time()

        # Stop memory tracking and get memory usage
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Calculate the metrics
        time_taken = end_time - start_time
        return {
            'time_taken': time_taken,  # Time in seconds
            'memory_usage': peak / 1024,  # Peak memory usage in KB
            'comparisons': self.comparison_count,
            'moves': self.move_count,
            'memory_current': current / 1024  # Current memory usage in KB
        }

    def increment_comparisons(self):
        """Increments comparison counter."""
        self.comparison_count += 1

    def increment_moves(self):
        """Increments move counter."""
        self.move_count += 1
