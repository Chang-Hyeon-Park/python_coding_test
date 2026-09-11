'''
3) 다음 큰 수
문제 설명

정수 배열 numbers가 주어집니다.

배열의 각 원소에 대해, 그 원소보다 뒤쪽(오른쪽)에 위치한 원소들 중에서 가장 왼쪽에 있는, 자기보다 큰 값을 찾아 순서대로 담은 배열을 return 하도록 solution 함수를 완성해주세요.

조건을 만족하는 값이 없으면 -1을 담습니다.

제한사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 각 원소는 1 이상 1,000,000 이하의 정수입니다.
중복된 값이 있을 수 있습니다.
입출력 예
numbers	result
[2, 1, 3]	[3, 3, -1]
[4, 2, 5, 1]	[5, 5, -1, -1]
[9, 1, 5, 3, 6, 2]	[-1, 5, 6, 6, -1, -1]
[7, 7, 7]	[-1, -1, -1]
입출력 예 설명

입출력 예 #1

2의 오른쪽은 [1, 3]입니다. 1은 2보다 작으므로 지나가고, 다음 3이 2보다 크므로 3입니다.
1의 오른쪽은 [3]입니다. 3이 크므로 3입니다.
3의 오른쪽에는 원소가 없으므로 -1입니다.

입출력 예 #3

9의 오른쪽에는 9보다 큰 값이 하나도 없으므로 -1입니다.
3의 오른쪽은 [6, 2]이고 6이 크므로 6입니다. 더 왼쪽에 있는 9는 뒤쪽이 아니므로 후보가 아닙니다.

입출력 예 #4

모든 값이 같습니다. 7은 7보다 크지 않으므로(같은 값은 조건에 맞지 않습니다) 전부 -1입니다.
'''

'''
[전략]
1. key값을 현재 위치로 잡음
2. key+1번째 자리부터 for문을 돌리는데 여기서 나보다 큰 값이 있으면 그 값을 return
3. 없으면 return -1

'''

# 내 풀이

# import sys

# def bigger_than_me(s):
#     res_stack = []
#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             if s[i] < s[j]:
#                 res_stack.append(s[j])
#                 break
#         if len(res_stack) != i+1:
#             res_stack.append(-1)
#     return res_stack

# def main():
#     s = list(map(int, sys.stdin.readline().split()))
#     print(bigger_than_me(s))
    
# if __name__ == "__main__":
#     main()


# Claude 모범 답안
import sys

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(i)
    return answer

def main():
    numbers = list(map(int, sys.stdin.readline().split()))
    print(' '.join(map(str,solution(numbers))))
    
if __name__ == "__main__":
    main()