'''
큐(Queue) & deque

1. what is queue?
 - 한쪽 끝으로 들어가서 반대쪽 끝으로 나오는 자료구조
 - FIFO(First In First Out)
 - 먼저 들어온게 먼저 나온다.
 - enqueue : 뒤에 넣기
 - dequeue : 앞에서 빼기
 
2. 파이썬 list의 실제 모습
 - 파이썬 list는 내부적으로 메모리에 원소들이 쭉 붙어서 저장돼 있음
 - 칸이 일렬로 늘어선 사물함이라 생각하면 됨
 - 근데 앞에서 빠지면 파이썬은 뒤에 있는 것들을 앞으로 옮겨서 채워야함.
 - 이때 쓰잘떼기 없는 작업이 오래 걸려서 느림.
 
3. deque
 - collections 모듈의 deque(덱, double-ended queue)를 쓴다.

from collections import deque

queue = deque()
queue.append(1)     # 뒤에 넣기 O(1)
queue.append(2)     
front = queue.popleft() # 앞에서 빼기 O(1)

 - deque는 내부 구조가 다름
 - 원소들을 작은 블록 단위로 쪼개서 사슬처럼 연결해 놓은 형태
 - 앞쪽 블록만 건드리면 되고 나머지를 옮길 필요가 없음
 - 그래서 양쪽 끝 연산이 전부 O(1)

4. 주요 메서드

from collections import deque

dq = deque([1,2,3])     # 리스트로 초기화 가능

dq.append(4)            # 오른쪽 추가       [1,2,3,4]
dq.appendleft(0)        # 왼쪽 추가         [0,1,2,3,4]
dq.pop()                # 오른쪽 제거 + 반환    -> 4
dq.popleft()            # 왼쪾 제거 + 반환  -> 0

dq.extend([5,6])        # 오른쪽에 여러 개
dq.extendleft([9, 8])   # 왼쪾에 여러 개 (역순으로 붙음! [8,9,1,2,3,5,6])

len(dq)                 # 길이
dq[0]                   # 맨 앞 (제거 안 함)
dq[-1]                  # 맨 뒤 (제거 안 함)
list(dq)                # 리스트로 변환 (return할 때 자주 씀)

5. rotate - 회전
 - rotate(k)는 오른쪽으로 k칸 민다.
 - 음수면 왼쪾으로 민다.
 
dq = deque([1,2,3,4,5])
dq.rotate(2)    # [4,5,1,2,3]
dq.rotate(-1)   # [5,1,2,3,4]

rotate(-1)은 dq.append(dq.popleft())랑 똑같은 동작임.
요세푸스류 문제에서 엄청 유용

6. maxlen - 크기 제한
dq = deque(maxlen=3)
dq.append(1); dq.append(2); dq.append(3)       # [1,2,3]
dq.append(4)                # [2,3,4] -> 1이 자동으로 밀려남

최근 K깨만 유지할 때 편함

7. dqeue의 약점
 - 중간 인덱스 접근이 느림

dq[5000]    # O(n)  - 블록을 하나씩 타고 가야 함
lst[5000]   # O(1)  - 주소 계산 한 번

8. 기준
dqeue - 앞에서 빼거나 앞에 넣는다
list  - 인덱스로 마구 접근한다
list  - 뒤에서만 넣고 뺀다(스택)

9. 복잡도 정리
연산            list        deque
뒤에 추가        O(1)        O(1)
뒤에서 제거      O(1)        O(1)
앞에 추가        O(n)        O(1)
앞에서 제거      O(n)        O(1)
인덱스 접근      O(1)        O(n)


10. 기본 패턴
from collections import deque

queue = deque(초기값들)

while queue:                    # 큐가 빌 때까지
    current = queue.popleft()   # 맨 앞 꺼내서
    # ... 처리 ....             
    queue.append(뭔가)          # 필요하면 다시 뒤에 넣기

while queue: - 빈 deque는 False라서 이렇게 쓰면 됨. len(queue) > 0 안 써도 됨
주의 : 빈 deque에 popleft()하면 IndexError 터짐
    : 스택이랑 똑같이 항상 비어있는지 확인해야함
    : 이 패턴이 나중에 BFS의 뼈대가 그대로 되니깐 손에 익혀둘 것.
'''
