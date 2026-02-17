def merge_sort(arr, left, right):
    if left < right:
        mid = (left+right)//2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    leftArray = arr[left:mid+1]
    rightArray = arr[mid+1: right+1]
    i = 0
    j =0
    k = left
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] <=rightArray[j]:
            arr[k] = leftArray[i]
            i+=1
        else:
            arr[k] = rightArray[j]
            j+=1
        k+=1
    while i < len(leftArray):
        arr[k] = leftArray[i]
        i+=1
        k+=1
    while j < len(rightArray):
        arr[k] = rightArray[j]
        j+=1
        k+=1

if __name__ == "__main__":
    arr = [38, 27, 43, 10, 23, 45,67,66,78,95, 95, 12, 1,34, 55]
   
    merge_sort(arr, 0, len(arr) - 1)
    for i in arr:
        print(i, end=" ")
    print()
