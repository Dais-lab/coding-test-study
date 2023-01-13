"""
문제 url : https://school.programmers.co.kr/learn/courses/30/lessons/42746#
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    answer = ""
    numbers_ = []
    for i in range(len(numbers)):
        if numbers[i] == "0":
            numbers_.append(["0", "0"])
        else:
            numbers_.append([(numbers[i] * 4)[:4], numbers[i]])
        

    numbers_index = numbers.copy()
    numbers_.sort(reverse=True)

    
    while numbers_ != []:
        num = numbers_.pop(0)
        index = numbers_index.index(num[1])
        answer += numbers[index]
    if answer[0] == "0":
        return "0"
    return answer
