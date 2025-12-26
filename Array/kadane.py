def basic_kadane(arr):
    if not arr:
        return
    
    current_sum = 0 
    max_sum = float('-inf')

    for num in arr:
        current_sum = max(num,current_sum+num)
        max_sum= max(max_sum,current_sum)
    return max_sum


def kadane_with_indices(arr):
    if not arr:
        return 0,-1,-1
    
    current_sum = 0 
    max_sum = float('-inf')
    start = 0 
    end = 0
    temp_start= 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
        if current_sum < 0 :
            current_sum = 0
            temp_start = i+1
        
    return max_sum,start,end

if __name__ == "__main__":
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {arr1}")
    max_sum = basic_kadane(arr1)
    print(max_sum)

    arr2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {arr2}")
    print(f"Max Sum: {kadane_with_indices(arr2)}")
    print()