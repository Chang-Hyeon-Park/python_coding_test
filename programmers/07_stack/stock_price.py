'''
Lv 2.
문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.
'''

'''
[전략]
1. key값과 그 뒤에 있는 값들을 비교하여 뒤에 값이 더 크면 count += 1
2. 뒤에 값이 더 작으면 continue
-> 브루트포스임

[전략2]
1. 뒤부터 봐서 나보다 큰 숫자가 나오면 +1
2. [0, 0, 0, 1, 0]
3. 0인것들은 전부 len -1 - index
4. 0이 아닌것의 바로 앞 인덱스에 있는 녀석을 stack에 있는 값만큼 뺌

[전략3]
1. 나보다 싼 값이 나온것까지 숫자를 세는것임
2. 
'''

import sys

def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
    return answer


# def solution(prices):
#     answer = [0] * len(prices)
#     stack = []
#     for i, price in enumerate(prices):
#         while stack and prices[stack[-1]] < price:
#             answer[stack.pop()]
#         stack.append(i)
#     return answer

def main():
    prices = list(map(int, sys.stdin.readline().split()))
    print(solution(prices))

if __name__ == "__main__":
    main()
