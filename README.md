# Algorithmer 인증용 Repo

|    날짜    |                      문제번호_이름                      |    알고리즘     |
| :--------: | :-----------------------------------------------------: | :-------------: |
| 2020.02.19 | [BOJ2798_블랙잭](https://www.acmicpc.net/problem/2798)  |   BruteForce    |
| 2020.02.27 | [BOJ11047_동전0](https://www.acmicpc.net/problem/11047) | GreedyAlgorithm |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |
|            |                                                         |                 |



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

