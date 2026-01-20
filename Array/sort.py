def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range (0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break

def cycle(arr):
    i = 0
    n = len(arr)-1

    while i < n :
        correct_index = arr[i]-1

        if arr[i] != arr[correct_index]:
            arr[i],arr[correct_index] = arr[correct_index],arr[i]
        else:
            i+=1

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        arr[j+1] = arr[i]

arr = [64, 34, 25, 12, 22, 11, 90]
arr1=[3,2,4,1,5]
insertion(arr)
print(arr)
