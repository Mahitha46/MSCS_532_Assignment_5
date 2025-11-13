import random

def randomized_quicksort(arr):
    """Randomized Quicksort using a randomly chosen pivot."""
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)


if __name__ == "__main__":
    data = [25, 45, 61, 5, 22, 10]
    print("Original array:", data)
    sorted_arr = randomized_quicksort(data)
    print("Sorted array:", sorted_arr)
