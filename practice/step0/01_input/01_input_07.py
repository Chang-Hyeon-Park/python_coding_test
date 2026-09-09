'''## 문제 7. 입력 끝까지 (EOF)

**개수가 주어지지 않는다.** 각 줄에 정수 두 개가 있고, 입력이 끝날 때까지
각 줄의 합을 출력하시오.

**input7.txt**
```
3 5
10 20
7 7
100 1
```

**출력**
```
8
30
14
101
```

> 두 가지 방법으로 각각 풀어볼 것:
> (a) `while True` + `try/except`
> (b) `for line in sys.stdin`

---'''

# import sys
# while True:
#     try:
#         a, b = map(int, sys.stdin.readline().split())
#         print(a + b)
#     except:
#         break
    
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a+b)