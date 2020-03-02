# Algorithmer 인증용 Repo

|    날짜    |                      문제번호_이름                      |       알고리즘       |
| :--------: | :-----------------------------------------------------: | :------------------: |
| 2020.02.19 | [BOJ2798_블랙잭](https://www.acmicpc.net/problem/2798)  |      BruteForce      |
| 2020.02.27 | [BOJ11047_동전0](https://www.acmicpc.net/problem/11047) |   GreedyAlgorithm    |
| 2020.02.28 |  [BOJ2573_빙산](https://www.acmicpc.net/problem/2573)   |         BFS          |
| 2020.03.03 |  [BOJ2206_빙산](https://www.acmicpc.net/problem/2206)   | BFS (*3차원 visited) |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |
|            |                                                         |                      |



#### TIL 01: 이미 push한 commit message 수정하기

```bash
$ git rebase -i HEAD~3 (숫자는 원하는 만큼)
- 편집창 뜨면 i(끼워넣기) 눌러서, 수정하고 싶은 커밋의 pick을 reword로 바꿈
- Esc + :wq 누르고 엔터
- 다시 새로운 편집창이 reword로 바꾼 만큼 뜰텐데, 맨 위에 수정하고 싶은 메시지를 입력해주면 됨 (입력할 땐 i(끼워넣기) 누르고 입력)
- 그럼 다음과 같이 뜬다.
- Successfully rebased and updated refs/heads/master.
- 커밋 메시지 수정이 완료 되었으므로 push 하자

$ git push --force
- 끝!
```



#### TIL 02: 3차원 visited 배열 사용하기.

- `BOJ2206-벽부수고이동하기` 문제에서, visited를 체크할 때 벽을 부수는 기회를 사용했는지 하지 않았는지 여부를 확인하기 위해 3차원 visited 배열을 사용했다.
- SWEA에서 풀었던 모의고사 `등산로 조성` 문제와 비슷한 느낌을 받았음.
- 벽을 부쉈을 때와 부수지 않았을 때의 visited 체크가 다르다는 것을 인지하긴 했다.
- 하지만 처음에는 copy 모듈을 통해 벽을 부쉈을 때 visited배열과 벽을 부수지 않았을 때의 visited 배열을 따로 복사해서 queue에 함께 넣어줬더니 코드를 잘못 짰는지 queue에 계속 append 되어서 메모리 초과가 났다.
- 처음 짰던 방식이 비효율적이긴 하더라도 그 코드를 살릴 방법이 없을 지 고민해봐야겠다. 
- visited 체크 방식이 나뉘는 문제를 만났을 때 해결할 수 있는 좋은 경험이 될 듯