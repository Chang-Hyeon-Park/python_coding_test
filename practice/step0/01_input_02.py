'''## 문제 2. N개의 수 (`list(map(...))`)

첫 줄에 개수 N, 둘째 줄에 N개의 정수가 공백으로 주어진다.

1번째 줄: 합
2번째 줄: 평균 (소수점 둘째 자리까지)
3번째 줄: 최댓값과 최솟값을 공백으로 구분

**input2.txt**
```
5
10 20 30 40 55
```

**출력**
```
155
31.00
55 10
```

> 힌트: 소수점 자리수는 `f"{값:.2f}"`

---'''

# n = int(input())
# lst = list(map(int, input().split()))
# if len(lst) > n:
#     print("FUCK YOU")
# # print(lst)
# sum, avg, min, max = 0;
# for i in range(n):
#     sum+=lst[n]
# avg = sum/n

# min = min(lst)
# max = max(lst)

# print(sum)
# print(avg)
# print(max, min)


# n = int(input())
# lst = list(map(int, input().split()))

# total = 0
# for i in range(n):
#     total += lst[i]

# avg = total / n

# print(total)
# print(f"{avg:.2f}")
# print(max(lst), min(lst))


n = int(input())
lst = list(map(int, input().split()))

print(sum(lst))
print(f"{sum(lst) / n :.2f}")
print(max(lst), min(lst))

# for x in lst:
#     total += x