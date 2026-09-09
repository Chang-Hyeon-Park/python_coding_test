'''## 문제 3. 성적 처리 (문자열 + 숫자 혼합)

첫 줄에 학생 수 N, 다음 N줄에 `이름 점수` 형식으로 주어진다.

1번째 줄: 최고점 학생의 `이름 점수`
2번째 줄: 전체 점수 합

**input3.txt**
```
4
alice 90
bob 75
charlie 88
dave 61
```

**출력**
```
alice 90
314
```'''

n = int(input())
total = 0
best_name = ""
best_score = 0
for _ in range(n):
    name, score = list(input().split())
    score = int(score)

    total += score
    
    if score > best_score:
        best_score = score
        best_name = name
print(best_name, best_score)
print(total)
    