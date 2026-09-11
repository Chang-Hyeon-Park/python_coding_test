'''
1. 카드 버리기

문제 설명

N장의 카드가 위에서부터 1, 2, 3, ..., N 순서로 쌓여 있습니다.

다음 동작을 카드가 한 장 남을 때까지 반복합니다.

맨 위의 카드를 버립니다.
그 다음 맨 위의 카드를 맨 아래로 옮깁니다.

마지막에 남는 카드의 번호를 return 하도록 solution 함수를 완성해주세요.

제한사항

N은 1 이상 500,000 이하의 정수입니다.

입출력 예

N	result
4	4
6	4
7	6
1	1

입출력 예 설명

입출력 예 #1

[1,2,3,4] → 1을 버리고 2를 아래로 → [3,4,2] → 3을 버리고 4를 아래로 → [2,4] → 2를 버리고 4를 아래로 → [4]. 남는 카드는 4입니다.

⏱ N이 500,000이므로 O(N)으로 풀어야 합니다.
'''

# import sys
# from collections import deque

# def solution(N):
#     dq = deque()
#     for i in range(1, N+1):
#         dq.append(i)
    
#     while dq and len(dq) != 1:
#         dq.popleft()
#         num = dq.popleft()
#         dq.append(num)
#     return dq

# def main():
#     N = int(sys.stdin.readline())
#     print("".join(map(str,solution(N))))
    
# if __name__ == "__main__":
#     main()



# Claude 모범 답안
import sys
from collections import deque

def solution(N):
    dq = deque(range(1, N+1))
    
    while len(dq) > 1:
        dq.popleft()
        dq.append(dq.popleft())
    return dq[0]

def main():
    N = int(sys.stdin.readline())
    print(solution(N))
    
if __name__ == "__main__":
    main()