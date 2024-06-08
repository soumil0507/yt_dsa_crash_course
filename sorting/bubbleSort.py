def bubbleSort(arr):
    
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    

    

if __name__ == '__main__':
    arr = [9, 8, 7, 4, 1, 10]
    print("Array before sorting - ", arr)
    bubbleSort(arr)
    print("Array after sorting - ", arr)