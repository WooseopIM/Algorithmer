import sys
sys.stdin = open('BOJ11047_동전_0.txt', 'r')
'''

'''
N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

accumulation = 0
cnt = 0
for i in range(N-1, -1, -1):
    if arr[i] > K or accumulation + arr[i] > K:
        continue

    while accumulation < K:
        accumulation += arr[i]
        cnt += 1
        if accumulation > K:
            accumulation -= arr[i]
            cnt -= 1
            break
print(cnt)