'''
N장의 카드가 주어지고, 각 카드에는 양의 정수가 쓰여있다.
딜러가 M을 외칠 때, 플레이어는 N장의 카드 중에서 3장을 뽑아 M이거나, M에 가장 가까운 수를 만들어야 한다.
N장의 카드 중에서 순서에 상관 없이 3장을 뽑는 조합(Combination) 문제.
'''

import sys, time
sys.setrecursionlimit(1000000)
sys.stdin = open('BOJ2798_블랙잭.txt', 'r')


# 1. 조합 함수 구현
def combination(index, next, mx):
    global N, M
    if index == 3:
        if mx > M:
            return
        else:
            empty.append(mx)
    else:
        for i in range(next, N):
            if not visited[i]:
                visited[i] = True
                mx += numlist[i]
                combination(index + 1, i + 1, mx)
                visited[i] = False
                mx -= numlist[i]


# 2. 입력 받기
s = time.time()
N, M = map(int, input().split())
numlist = list(map(int, input().split()))
visited = [False] * N
blackjack = 0
empty = []
combination(0, 0, blackjack)
print(max(empty))
e = time.time()
print(e-s)

# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             mx = numlist[i] + numlist[j] + numlist[k]
#             if blackjack <= mx <= M:
#                 blackjack = mx
# print(blackjack)