'''
1) 괄호 종류 하나짜리
()만 들어있는 문자열이 올바른지 판정.
"(())" -> True
"())(" -> False
'''

'''
[전략]
1. 시작은 무조건 여는 괄호여야 함
2. 끝이 여는 괄호면 안됨
3. 여는괄호면 append
4. 닫는괄호이면
    4-1. 스택이 비어있는데 닫는 괄호면 False
    4-2. 직전 스택이 여는 괄호이면 True이면서 pop
'''


import sys

def is_valid(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()

    return not stack

def main():
    s = sys.stdin.readline().rstrip()
    print(is_valid(s))

if __name__ == '__main__':
    main()