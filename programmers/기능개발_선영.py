from math import ceil

def solution(progresses, speeds):
    max_value = ceil((100-progresses[0]) / speeds[0])
    answer = []
    count = 0
    
    for progresses, speeds in zip(progresses, speeds):
        value = ceil((100-progresses) / speeds)
        if max_value < value:
            answer.append(count)
            count = 0
            max_value = value
        count += 1
    answer.append(count)
    return answer