def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        picture[i] = picture[i].replace('.','.'*k)
        picture[i] = picture[i].replace('x','x'*k)
        for j in range(k):
            answer.append(picture[i])
    return answer