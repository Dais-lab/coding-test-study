def solution(arr):
    answer = 0
    cnt = 0
    for i in range(len(arr)):
        cnt += arr[i]
    answer = cnt / len(arr)
    
    return answer