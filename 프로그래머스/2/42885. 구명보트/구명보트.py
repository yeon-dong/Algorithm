def solution(people, limit):
    people = sorted(people)
    start = 0
    end = len(people)-1
    answer = 0
    while start <= end:
        if (people[start] + people[end] <= limit):
            start += 1
            end -= 1
            answer += 1
        else:
            end -= 1
            answer += 1

    return answer