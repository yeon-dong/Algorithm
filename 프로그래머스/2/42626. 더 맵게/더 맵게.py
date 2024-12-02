import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    #최소 힙 큐 이용
    while scoville[0] < K:
        new_food = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_food)
        answer += 1
        #한개밖에 안 남았고, 스코빌 지수도 K를 못 채웠다면 -1 리턴
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer