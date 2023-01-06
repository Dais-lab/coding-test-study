
import math

def solution(progresses, speeds):
    answer = []
    items = []
    for i in range(len(progresses)):
        item = (100 - progresses[i]) / speeds[i]
        items.append(math.ceil(item))
    std = items.pop(0)
    count = 1
    while items:
        item = items.pop(0)
        if std < item:
            std = item
            answer.append(count)
            count = 1
        else:
            count += 1
    answer.append(count)
    return answer