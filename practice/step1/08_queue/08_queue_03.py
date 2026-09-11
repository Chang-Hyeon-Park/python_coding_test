'''
3. 요세푸스 순열

문제 설명

1번부터 N번까지 N명의 사람이 원을 이루어 앉아 있고, 양의 정수 K가 주어집니다.

1번부터 순서대로 세어 나가면서 K번째 사람을 원에서 제거합니다. 제거된 다음 사람부터 다시 1부터 세기 시작해 K번째 사람을 제거하는 과정을, 모든 사람이 제거될 때까지 반복합니다.

제거되는 순서대로 번호를 담은 배열을 return 하도록 solution 함수를 완성해주세요.

제한사항

N은 1 이상 100,000 이하의 정수입니다.
K는 1 이상 50 이하의 정수입니다.

입출력 예

N	K	result
7	3	[3, 6, 2, 7, 5, 1, 4]
5	2	[2, 4, 1, 5, 3]
4	1	[1, 2, 3, 4]

입출력 예 설명

입출력 예 #1

[1,2,3,4,5,6,7]에서 3번째인 3이 제거됩니다. 4부터 다시 세어 6이 제거됩니다. 7부터 세어 7, 1, 2 순으로 세므로 2가 제거됩니다. 이런 식으로 계속하면 [3,6,2,7,5,1,4]가 됩니다.

⏱ N × K가 최대 500만이므로, 한 번 제거할 때마다 K번 정도 움직이는 방식이면 통과합니다.
'''

'''
[전략]
1. K만큼 rotate
2. popleft()한거를 answer에 저장
'''


import sys
from collections import deque

def solution(N, K):
    dq = deque(range(1, N+1))
    answer = []
    while dq:
        dq.rotate(-(K-1))
        answer.append(dq.popleft())
    
    return answer

def main():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    print(" ".join(map(str, solution(N, K))))

if __name__ == "__main__":
    main()