# 파이썬은 스택 전용 클래스가 따로 없고 그냥 list를 쓰면 됨

'''
1. list = 스택

stack = []

stack.append(1) # push
stack.append(2)
stack.append(3) # stack = [1,2,3]

top = stack[-1] # 3 (peek, 꺼내지 않고 보기만)

x = stack.pop() # 3 (꺼내면서 제거) -> stack = [1, 2]

'''
###################################################
###################################################
'''
2. 빈 스택 처리

빈 리스트에 pop()이나 [-1]을 하면 에러가 발생함

stack = []
stack.pop() # IndexError : pop from empty list
stack[-1]   # IndexError : list index out of range

그래서 항상 비어있는지 확인해야하는데, 파이썬에서는 이렇게 씀
if not stack:
    print("비어있음")

'''
###################################################
###################################################
'''
3. 단락 평가(short-circuit)

and와 or는 왼쪽부터 평가하다가 결과가 확정되면 오른쪽을 아예 실행 안함

A and B -> A가 False면 B를 안 봄(이미 전체가 False)확정

A or B -> A가 True면 B를 안 봄

if stack and stack[-1] == '(':
    stack.pop()
'''
###################################################
###################################################
'''
4. 괄호 짝 맞추기
스택의 대표 문제. 
 - 여는 괄호 -> push
 - 닫는 괄호 -> 스택 top이 짝이 맞으면 pop, 아니면 실패
 - 다 돌고 나서 스택이 비어 있어야 성공
'''
import sys

def is_valid(s):
    pairs = {')' : '(', ']' : '[', '}' : '{'}
    stack = []
    
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    
    return not stack

def main():
    s = sys.stdin.readline().rstrip()
    print(is_valid(s))

if __name__ == "__main__":
    main()