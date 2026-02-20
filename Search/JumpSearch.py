import math


def jump_search(sortedArray, target):
    n = len(sortedArray)

    if n == 0:
        return -1

    step = int(math.sqrt(n))
    prev = 0

    while sortedArray[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while sortedArray[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if sortedArray[prev] == target:
        return prev

    return -1


if __name__ == "__main__":
    input_array = input(
        "Enter all the elements of the sorted array separated by space:"
    )
    input_list = list(map(int, input_array.split()))
    search_input = input("Enter the search value: ")
    search_value = int(search_input)

    result = jump_search(input_list, search_value)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
