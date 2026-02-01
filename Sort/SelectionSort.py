def SelectionSort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
    arr = [64, 12, 35, 25, 17, 90, 22]

    SelectionSort(arr)

    print(arr)
