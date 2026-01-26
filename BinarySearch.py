def binary_search(sortedArray, searchterm):
    length = len(sortedArray)
    low = 0
    high = length - 1
    
    while low <= high:
        mid = low+(high-low)//2
        if sortedArray[mid] == searchterm:
            return mid
        elif sortedArray[mid] > searchterm:
            high = mid - 1
        else:
            low = mid + 1
    return -1

if __name__ == "__main__":
    input_array = input("Enter all the elements of the sorted array seperated by space:")
    input_list = list(map(int, input_array.split()))
    search_input = input("Enter the search value")
    search_value = int(search_input)
    
    print(binary_search(input_list, search_value))
