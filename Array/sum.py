def prefix(arr,n):
    prefixSum = 0
    for i in range(n):
        prefixSum += arr[i]
        prefixArr.append(prefixSum)
    return prefixSum

def postfix(arr,n):
    postfixSum = [0 for _ in range(n)]

    postfixSum[n-1] = arr[n-1] 

    for i in range(n-2,-1,-1):
        postfixSum[i] = postfixSum[i+1] + arr[i]
    
    return postfixSum


if __name__ == "__main__":
    arr = [10,14,16,20]
    n=len(arr)
    prefixArr = []
    prefix(arr,n)
    postfix = postfix(arr,n)
    print(prefixArr)
    print(postfix)