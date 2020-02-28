import sys

sys.stdin = open('BOJ2573_빙산.txt', 'r')

import collections

N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# 빙산의 덩어리가 몇 개인지 세주는 bfs 알고리즘. 함수 실행이 끝나면 num을 증가시킴
def bfs(visited, queue):
    while q:
        first_q = queue.popleft()
        for ii in range(4):
            ny = first_q[0] + delta[ii][0]
            nx = first_q[1] + delta[ii][1]
            if (0 <= ny < N) and (0 <= nx < M):
                if iceberg[ny][nx] and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True


year = 0
while True:
    visited = [[0] * M for _ in range(N)]

    # Step1. 빙산 녹이기
    for i in range(N):
        for j in range(M):
            water = 0
            if iceberg[i][j] > 0:
                for k in range(4):
                    dy = i + delta[k][0]
                    dx = j + delta[k][1]
                    if (0 <= dy < N) and (0 <= dx < M):
                        if iceberg[dy][dx] == 0:
                            water += 1
                if iceberg[i][j] <= water:
                    iceberg[i][j] = -1
                else:
                    iceberg[i][j] -= water

    # Step2. 1년 지나서 빙산이 녹았으면 -1로 된 부분을 0으로 바꿔준다.
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] == -1:
                iceberg[i][j] = 0

    year += 1

    # Step3. 빙산이 남아 있는지 확인(1년만에 다 녹았는지 아닌지)
    start_counting = False
    for i in range(N):
        for j in range(M):
            # 빙산이 1년만에 다 녹지 않았다면(빙산이 있는 칸이 하나 이상 있으면 빙산 덩어리가 몇 개인지 카운팅 시작)
            if iceberg[i][j]:
                start_counting = True
                break
        if start_counting:
            break

    # 만약 빙산이 1년만에 다 녹았다면 while문 종료
    if not start_counting:
        ice = 0
        break

    # Stpe3. bfs로 iceberg 배열과 visited 배열을 순회하면서 빙산 덩어리 카운트
    q = collections.deque([])
    ice = 0
    flag = False
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] and not visited[i][j]:
                ice += 1

                if ice < 2:
                    visited[i][j] = True
                    q.append((i, j))
                    bfs(visited, q)
                # j 반복문 종료
                else:
                    flag = True
                    break
        # i 반복문 종료
        if flag:
            break
    # while 반복문 종료
    if flag:
        break


if ice == 0:
    print(0)
else:
    print(year)
