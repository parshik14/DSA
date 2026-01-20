def binarySeach(arr,key):
    low = 0
    high = len(arr)-1

    while low <= high :
        mid = int(low + (high-low)/2)
        if arr[mid] == key :
            return mid
        elif arr[mid]>key:
            high = mid-1
        else:
            low= mid + 1
    
    return -1

def leftMostOccurance(arr,key):
    low = 0 
    high = len(arr)-1
    a = -1


    while low <= high :
        mid = int(low + (high - low)/2)

        if arr[mid] == key : 
            a = mid
            high = mid-1
        elif arr[mid] > key :
            high = mid - 1
        elif arr[mid] < key :
            low = low + 1
    
    return a

def rightMostOccurance(arr,key):
    low = 0
    high = len(arr)-1

    ans = -1

    while low <= high :
        mid = int ( low  + (high - low )/2)
        if arr[mid] == key :
            ans = mid
            low = mid + 1
        elif arr[mid]<key:
            low = low + 1
        else : 
            high = high - 1
    return ans


arr = [1,1,1,2,2,3,4,5,6,7,8,9]
arr1 = [1,1,3,3,3,3,3,3,3,4,5,6,7,8,9]
ans = binarySeach(arr,2)
left = leftMostOccurance(arr1,3)
right = rightMostOccurance(arr1,10)
print(ans)
print(left)
print(right)