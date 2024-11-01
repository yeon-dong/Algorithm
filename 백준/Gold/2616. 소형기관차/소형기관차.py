# def solution(genres, plays):
#     from collections import defaultdict
#     genre_play_count = defaultdict(int)
#     genre_songs = defaultdict(list)
#
#     for i in range(len(genres)):
#         genre_play_count[genres[i]] += plays[i]
#         genre_songs[genres[i]].append((i,plays[i]))
#     print(genre_songs)
#
#
#     return 0
#
#
# print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))
#
# import random
#
# 왓더버거 = 0
# 한솥 =  0
#
# for _ in range(10000):
#     i = random.randint(0,1)
#     if i == 0:
#         왓더버거 += 1
#     else:
#         한솥 += 1
# print("숫자가 더 높은 쪽으로 고릅니다 : ", 왓더버거 ,",", 한솥)

giguancha = int(input())
giguancha_list = input().split()
giguancha_list = [ int(i) for i in giguancha_list ]
small_giguancha_num = int(input())
dp = [[0 for _ in range(giguancha+1)] for _ in range(4)]
giguancha_list_sum = [0 for _ in range(giguancha+1)]
giguancha_list_sum[1] = giguancha_list[0]
for i in range(1,giguancha+1):
    giguancha_list_sum[i] = giguancha_list_sum[i-1] + giguancha_list[i-1]
for i in range(1, 4):
    for j in range(small_giguancha_num, giguancha+1):
        dp[i][j] = max(dp[i][j - 1],
                       dp[i - 1][j - small_giguancha_num] + giguancha_list_sum[j] - giguancha_list_sum[j - small_giguancha_num])
print(dp[3][giguancha])