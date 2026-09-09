'''## 문제 8. 테스트케이스 반복 (종합)

첫 줄에 테스트케이스 개수 T.
각 테스트케이스는 두 줄로 이루어진다 — 첫 줄에 N, 둘째 줄에 N개의 정수.

각 테스트케이스마다 `N 합` 형식으로 출력하되,
**결과를 리스트에 모았다가 마지막에 한 번에** 출력하시오.

**input8.txt**
```
2
3
5 3 9
2
100 40
```

**출력**
```
3 17
2 140
```

> 포인트: `sys.stdin.readline`으로 input 갈아끼우기 + 결과 모아서 `"\n".join()`
'''

import sys
input = sys.stdin.readline

t = int(input())
res = []

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    res.append(f"{n} {sum(lst)}")

print("\n".join(res))