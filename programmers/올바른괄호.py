# 시간복잡도 O(n) n:문자열의 크기

def solution(s):
    answer = True
    count = 0
    right = 0 #'(' 개수 
    left = 0 #')' 개수
    for idx in range(len(s)):
        if s[idx] == '(':
            count += 1 # '('가 나오면 더해줌
            right += 1
        else:
            left += 1
            if count > 0: # '('가 한번이상 나왔을 때
                count -= 1 # ')'가 나오면 빼줌
    
    if (count != 0) | (left != right): # count가 0이 아니거나 '('와 ')' 개수가 다르면 false
        answer = False
    return answer
