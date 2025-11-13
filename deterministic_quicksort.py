def deterministic_quicksort(arr):
    """Deterministic Quicksort using the last element as pivot."""
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)


if __name__ == "__main__":
    data = [25, 45, 61, 5, 22, 10]
    print("Original array:", data)
    sorted_arr = deterministic_quicksort(data)
    print("Sorted array:", sorted_arr)
