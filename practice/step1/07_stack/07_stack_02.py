'''
2) 중복 문자 제거
문자열에서 연속된 같은 문자 2개를 계속 지웠을 때 최종 결과를 반환

"abbaca" -> "ca" (bb제거 -> "aaca" -> aa제거 -> "ca")
'''

'''
[전략]
1. 직전문자와 비교하여 같으면 pop
2. 직전문자와 비교하여 다르면 append
3. 첫문자는 무조건 append
'''


import sys

def duplicate_string(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif ch == stack[-1]:
            stack.pop()
        elif ch != stack[-1]:
            stack.append(ch)
    return stack

def main():
    s = sys.stdin.readline().strip()
    # print("".join(map(str,duplicate_string(s))))
    print(duplicate_string(s))
    print("".join(duplicate_string(s)))

if __name__ == "__main__":
    main()