def solution(people, limit):
    answer = 0
    people.sort()
    frontidx = 0
    backidx = len(people)-1
    while frontidx <= backidx:
        if frontidx == backidx:
            answer += 1
            break

        if (people[frontidx] + people[backidx] <= limit):
            frontidx += 1
            backidx -= 1
        else:
            backidx -= 1
        answer += 1

    return answer