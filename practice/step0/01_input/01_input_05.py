'''## 문제 5. 미로 격자 (붙어있는 숫자)

첫 줄에 N M, 다음 N줄에 0과 1이 **공백 없이 붙어서** 주어진다.

1번째 줄: 1의 총 개수
2번째 줄: 각 열의 1의 개수를 공백으로 구분

**input5.txt**
```
4 5
11000
01110
00011
10101
```

**출력**
```
10
2 2 2 2 2
```

> 포인트: `split()`을 쓰면 안 된다. `map(int, input())`이 왜 되는지 생각해볼 것.

---'''

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input())))

count = 0

for row in board:
    for x in row:
        if x == 1:
            count += 1

print(count)

row_count_num = 0
row_count = []

for row in board:
    for x in row:
        if x == 1:
            row_count_num += 1
    row_count.append(row_count_num)
    row_count_num = 0

print(" ".join(map(str, row_count)))

col_count = []
for j in range(m):
    col_sum = 0
    for i in range(n):
        col_sum += board[i][j]
    col_count.append(col_sum)

print(" ".join(map(str, col_count)))