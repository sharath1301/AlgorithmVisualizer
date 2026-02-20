def interpolation_search(sortedArray, target):
    low = 0
    high = len(sortedArray) - 1

    while low <= high and target >= sortedArray[low] and target <= sortedArray[high]:
        if low == high:
            if sortedArray[low] == target:
                return low
            return -1

        pos = low + ((target - sortedArray[low]) * (high - low)) // (
            sortedArray[high] - sortedArray[low]
        )

        if sortedArray[pos] == target:
            return pos

        if sortedArray[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


if __name__ == "__main__":
    input_array = input(
        "Enter all the elements of the sorted array separated by space:"
    )
    input_list = list(map(int, input_array.split()))
    search_input = input("Enter the search value: ")
    search_value = int(search_input)

    result = interpolation_search(input_list, search_value)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
