'''
    deque - 양쪽 끝이 빠른 큐
    from collections import deque
    
    파이썬 list는 C의 동적 배열(malloc + realloc)이랑 똑같은 구조임
    그래서 맨 앞에서 빼면 뒤에 있는 원소를 전부 한 칸씩 당겨야 함.
    
'''

# lst = [1,2,3,4,5]
# lst.pop(0)
# print(lst)
# lst.insert(0,6)
# print(lst)

'''
    deque는 내부적으로 이중 연결 리스트(정확히는 블록 단위 연결 리스트)라서 양쪽 끝이 O(1)이다.
'''

# from collections import deque

# dq = deque([1,2,3])

# dq.append(4)        # 오른쪽 추가 -> [1,2,3,4]
# dq.appendleft(0)    # 왼쪽 추가   -> [0,1,2,3,4]
# dq.pop()            # 오른쪽 제거 -> 4
# dq.popleft()        # 왼쪽 제거   -> 0
# print(dq)
# dq.extend([5,6])    # 오른쪽에 여러 개
# print(dq)
# dq.extendleft([9,8])    # 왼쪽에 여러 개(역순으로 들어감) deque([8, 9, 1, 2, 3, 5, 6])
# print(dq)

# dq.rotate(1)            # 오른쪽으로 회전
# print("dq.rotate(1) : ", dq)
# dq.rotate(-1)           # 왼쪽으로 회전
# print("dq.rotate(-1) : ", dq)

# dq.rotate(3)
# print("dq.rotate(3) : ", dq)

# res = list(dq) # 리스트로 반환
# print("list(dq) : ", res)

'''
    maxlen - 크기 제한
'''

from collections import deque
dq = deque(maxlen=3)
for i in range(5):
    dq.append(i)
print(dq) # deque([2, 3, 4], maxlen=3)
# 꽉 차면 반대쪽이 자동으로 밀려남. 슬라이딩 윈도우 문제에서 유용함.

# BFS 큐, 슬라이딩 윈도우, 회전 문제에서 사용함

# BFS 기본형 - 암기하기
'''
from collections import deque
q = deque([start])
while q:
    now = q.popleft()
    for nxt in graph[now]:
        q.append(nxt)
'''