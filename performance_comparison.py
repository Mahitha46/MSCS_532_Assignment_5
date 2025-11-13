import random
import time
import matplotlib.pyplot as plt
import sys
from deterministic_quicksort import deterministic_quicksort
from randomized_quicksort import randomized_quicksort

# === SAFETY SETTINGS ===
sys.setrecursionlimit(1500)   # Safe recursion depth for large arrays

# Reduced input sizes for faster execution
sizes = [500, 1000, 2000, 5000, 8000]  
data_types = ["random", "sorted", "reversed"]

def generate_data(size, data_type="random"):
    """Generate input arrays of different types."""
    if data_type == "random":
        return [random.randint(0, size) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reversed":
        return list(range(size, 0, -1))
    else:
        raise ValueError("Invalid data_type. Choose from: random, sorted, reversed.")

def measure_time(sort_func, arr):
    """Measure execution time of a sorting function with safety checks."""
    start = time.time()
    try:
        sort_func(arr.copy())
    except RecursionError:
        return float("inf")  # too deep recursion → mark as infinite time
    return time.time() - start

def run_experiment():
    for dtype in data_types:
        det_times = []
        rand_times = []

        print(f"\n=== Testing on {dtype.upper()} Data ===")
        for n in sizes:
            arr = generate_data(n, dtype)

            # Skip deterministic Quicksort on sorted/reversed large arrays
            if dtype != "random" and n > 2000:
                det_time = float("inf")
            else:
                det_time = measure_time(deterministic_quicksort, arr)

            rand_time = measure_time(randomized_quicksort, arr)

            det_times.append(det_time)
            rand_times.append(rand_time)

            print(f"Size={n:5d} | Deterministic={det_time:.5f}s | Randomized={rand_time:.5f}s")

        # Plot results
        plt.figure(figsize=(8, 5))
        plt.plot(sizes, det_times, marker='o', label='Deterministic Quicksort', linewidth=2)
        plt.plot(sizes, rand_times, marker='s', label='Randomized Quicksort', linewidth=2)
        plt.title(f"Quicksort Performance on {dtype.capitalize()} Data")
        plt.xlabel("Input Size (n)")
        plt.ylabel("Time (seconds)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"quicksort_{dtype}_safe_performance.png", dpi=300)
        plt.close()  # closes figure to save memory

if __name__ == "__main__":
    print("=== Safe Quicksort Performance Experiment ===")
    print(f"Recursion limit: {sys.getrecursionlimit()}")
    run_experiment()
    print("\nExperiment complete. Plots saved as PNG files.")
