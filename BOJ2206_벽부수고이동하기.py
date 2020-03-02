import sys, collections, copy
sys.stdin = open('BOJ2206_벽부수고이동하기.txt' ,'r')
'''
N * M 행렬로 표현되는 맵
0: 이동할 수 있는 경로
1: 이동할 수 없는 경로(벽)

(1, 1) 위치에서 (N, M)으로 이동
그러니까 좌상단에서 우하단까지
시작과 끝점을 포함하여 이동하는 칸의 최소개수를 출력

이동하는 도중에 한 개의 벽을 부수고 이동하는 것이
조금 더 경로가 짧아진다면 벽을 한 번 부수는 것까지 허용

(1, 1)에서 (N, M)까지 어떻게 해서도 이동할 수 없을 경우
-1을 출력한다.

최단거리 문제는 bfs?
'''


def bfs():
    global maps
    q = collections.deque([])
    q.append((0, 0, 0))
    visited = [[[0]*M for _ in range(N)] for _ in range(2)]
    visited[0][0][0] = 1
    while q:
        y, x, cut = q.popleft()

        # 이번에 pop한 큐가 끝점에 도달했을 때
        if y == N-1 and x == M-1:
            # 그 때까지 누적된 거리를 리턴한다.
            return visited[cut][y][x]

        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny = y + d[0]
            nx = x + d[1]
            # 배열 범위 안에 있고,
            if (0 <= ny < N) and (0 <= nx < M):
                # 방문하지 않는 칸인데,
                if not visited[cut][ny][nx]:

                    # 그곳은 진입할 수 있는 곳이다.
                    if not maps[ny][nx]:
                        # 방문처리 후 진입. 벽을 부술 필요는 없다.
                        visited[cut][ny][nx] = visited[cut][y][x] + 1
                        q.append((ny, nx, cut))

                    # 그곳은 벽이 있어 진입할 수 없다.
                    # 만약 벽을 부수는 기회를 사용하지 않았다면 (not cut) 벽을 부수고 진입한다.
                    # 벽을 부수는 기회를 사용했다면 아무것도 못하고 그냥 통과
                    elif maps[ny][nx] and not cut:
                        visited[1][ny][nx] = visited[cut][y][x] + 1
                        q.append((ny, nx, 1))
    # 만약 (N, M)에 도달하지 못했다면 -1을 리턴한다.
    return -1


N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
print(bfs())