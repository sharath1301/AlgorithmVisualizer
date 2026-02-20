def binary_search_range(sortedArray, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if sortedArray[mid] == target:
            return mid
        elif sortedArray[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def exponential_search(sortedArray, target):
    n = len(sortedArray)

    if n == 0:
        return -1

    if sortedArray[0] == target:
        return 0

    i = 1
    while i < n and sortedArray[i] <= target:
        i *= 2

    return binary_search_range(sortedArray, target, i // 2, min(i, n - 1))


if __name__ == "__main__":
    input_array = input(
        "Enter all the elements of the sorted array separated by space:"
    )
    input_list = list(map(int, input_array.split()))
    search_input = input("Enter the search value: ")
    search_value = int(search_input)

    result = exponential_search(input_list, search_value)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
