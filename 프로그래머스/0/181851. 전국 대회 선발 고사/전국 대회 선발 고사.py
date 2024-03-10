def solution(rank, attendance):
    a = [j for i,j in enumerate(rank) if attendance[i]]
    a.sort()
    return 10000 * rank.index(a[0]) + 100 * rank.index(a[1]) + rank.index(a[2])