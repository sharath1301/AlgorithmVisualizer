def linear_search(inputArray, value):
    for i in range(len(inputArray)):
        if value == inputArray[i]:
            return i 
    return -1

if __name__ == "__main__":
    input_array = input("Enter all the elements of the array seperated by space:")
    input_list = list(map(int, input_array.split()))
    search_input = input("Enter the search value")
    search_value = int(search_input)
    
    print(linear_search(input_list, search_value))
