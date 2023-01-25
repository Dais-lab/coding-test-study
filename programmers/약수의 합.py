def solution(n):
    answer = 0
    리스트 = []
    
    for i in range(1, n+1):
        if n % i == 0:
            리스트.append(i)
            
    for i in range(len(리스트)):
        answer += 리스트[i]
    return answer