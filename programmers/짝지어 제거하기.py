def solution(s):
    리스트 = []
    
    for i in s:
        if len(리스트) == 0:
            리스트.append(i)
        elif i == 리스트[-1]:
            리스트.pop()
        else:
            리스트.append(i)
        
    return int(리스트 == [])