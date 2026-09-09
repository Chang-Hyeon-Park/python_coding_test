'''## 문제 4. 2차원 격자 (공백 구분)

첫 줄에 N M, 다음 N줄에 M개씩 정수가 공백으로 주어진다.

1번째 줄: 전체 합
2번째 줄: 각 행의 합을 공백으로 구분
3번째 줄: 대각선 원소들 (board[0][0], board[1][1], ...) 를 공백으로 구분

**input4.txt**
```
3 4
1 2 3 4
5 6 7 8
9 10 11 12
```

**출력**
```
78
10 26 42
1 6 11
```'''

# n, m = map(int, input().split())

# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))
    
# print(sum(board[0]) + sum(board[1]) + sum(board[2]))
# print(sum(board[0]), sum(board[1]), sum(board[2]))
# print(board[0][0], board[1][1], board[2][2])

# n, m = map(int, input().split())

# board = []

# for _ in range(n):
#     board.append(list(map(int, input().split())))

# # 1. 전체 합
# total = 0
# for row in board:
#     total += sum(row)

# print(total)

# # 2. 각 행의 합
# row_sums = []
# for row in board:
#     row_sums.append(sum(row))

# print(" ".join(map(str, row_sums)))

# # 3. 대각선
# diag = []
# for i in range(min(n, m)):
#     diag.append(board[i][i])

# print(" ".join(map(str, diag)))

