'''
2. 배열 회전

문제 설명

정수 배열 numbers와 정수 k가 주어집니다.

numbers를 오른쪽으로 k칸 회전시킨 배열을 return 하도록 solution 함수를 완성해주세요. 오른쪽 끝을 넘어간 원소는 왼쪽 끝으로 돌아옵니다.

제한사항

numbers의 길이는 1 이상 200,000 이하입니다.
numbers의 각 원소는 1 이상 1,000,000 이하의 정수입니다.
k는 0 이상 1,000,000,000 이하의 정수입니다.

입출력 예

numbers	k	result
[1, 2, 3, 4, 5]	2	[4, 5, 1, 2, 3]
[1, 2, 3, 4, 5]	5	[1, 2, 3, 4, 5]
[1, 2, 3]	7	[3, 1, 2]
[10]	100	[10]

입출력 예 설명

입출력 예 #3

배열 길이가 3이므로 7칸 회전은 1칸 회전과 같습니다.

⏱ k가 10억까지 가능합니다. k번 회전을 그대로 반복하면 시간 초과입니다. O(N)으로 풀어야 합니다.
'''

import sys
from collections import deque

def solution(n, k):
    dq = deque(n)
    dq.rotate(k % len(dq))
    return list(dq)

def main():
    n = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())
    print(solution(n,k))
    
if __name__ == "__main__":
    main()