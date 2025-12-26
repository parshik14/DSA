def basic_kadane(arr):
    if not arr:
        return
    
    current_sum = 0 
    max_sum = float('-inf')

    for num in arr:
        current_sum = max(num,current_sum+num)
        max_sum= max(max_sum,current_sum)
    return max_sum


if __name__ == "__main__":
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {arr1}")
    max_sum = basic_kadane(arr1)
    print(max_sum)