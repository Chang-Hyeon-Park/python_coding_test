'''
1. input() - 기본 입력
s = input()
print(s)

특징
- 항상 문자열로 받는다
n = input()         # "5" 입력
print(n + 1)        # TypeError! 문자열 + 정수
print(int(n) + 1)   # 6
- 숫자로 쓰려면 무조건 int()로 감싸야 한다.
- 엔터 친 건 안들어옴

- 인자는 하나만
input("이름: ")     # OK
input("이름", "나이") # TypeError

2. sys.stdin.readline() - 빠른 입력
import sys
s = sys.stdin.readline()
- input()은 내부적으로 프롬프트 처리 같은 부가 작업을 해서 느림
- 입력이 10만 줄쯤되면 이것만으로 시간 초과가 남
- 개행문자가 안잘림

s = sys.stdin.readline()    # "hello"입력
print(len(s))               # 6 -> \n포함
'''

# import sys
# s = sys.stdin.readline()
# print(len(s))

'''
그래서 문자열로 쓸 땐 .strip() 또는 .rstrip() 필수
'''
# import sys
# s = sys.stdin.readline().strip()
# print(len(s))
'''
숫자로 받을 땐 strip 안 해도 됨
'''
# n = int(sys.stdin.readline())   # int()가 공백/개행 알아서 무시

# import sys
# input = sys.stdin.readline

# n = int(input())
# s = input().strip()

# print(n)
# print(s)

'''
3. map(int, input().split()) - 숫자 여러 개 받기
입력이 3 5 7 이라고 할 때

s = input()         # "3 5 7" -> 문자열 하나
lst = s.split()     # ['3', '5', '7']   문자열 리스트

split()은 공백 기준으로 쪼갬. 근데 아직 전부 문자열임

lst = list(map(int, lst))   # [3,5,7] 정수 리스트

map(함수, 반복가능한것) - 모든 원소에 함수를 적용해줌. 여기선 각 문자열에 int()를 씌운것임

한 줄로는
a, b, c = map(int, input().split())     # 개수가 정해져 있을 때
lst = list(map(int, input().split()))   # 개수가 유동적일 때

※ map은 리스트가 아님
m = map(int, input().split())
print(m)        # <map object at 0x...>
print(len(m))   # TypeError!

map은 한 번만 순회 가능한 객체.
인덱스 접근도 안 되고 len()도 안됨. 그래서 리스트로 쓰려면 list()로 감싸야함

그리고 한 번 다 쓰면 비어버림
m = map(int, "1 2 3".split())
print(list(m))      # [1, 2, 3]
print(list(m))      # [] 두 번째는 비어있음!

split()옵션

"3 5 7".split()         # ['3','5','7']     공백 기준(연속 공백도 처리)
"3,5,7".split(",")      # ['3','5','7']     쉼표 기준
"3     5  7".split()    # ['3','5','7']     연속 공백 OK
"3     5  7".split(" ") # ['3','','','','5','','7']     빈 문자열 생김


4. 여러 줄 입력
패턴A : 첫 줄에 개수, 다음 줄부터 데이터

3
10
20
30

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
    
컴프리헨션으로
n = int(input())
lst = [int(input()) for _ in range(n)]

패턴 B : 여러 줄, 각 줄에 여러 값

3
1 2
3 4
5 6

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

패턴 C : 첫 줄에 여러 값

5 3

n, m = map(int, input().split())


5. 2차원 입력 받기
숫자가 공백으로 구분된 경우

3 3
1 2 3
4 5 6
7 8 9

n, m = map(int(input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

숫자가 붙어있는 경우(미로 문제에 자주 나옴)
3 3
110
011
101

n, m = map(int, input().split())
board = [list(map(int, intput())) for _ in range(n)]

문자 그대로 받을 경우
##.
.#.

board = [list(input()) for _ in range(n)]

6. print() 옵션
print(1,2,3) # 1 2 3 -> 자동으로 공백 삽입, 끝에 개행문자

sep - 값 사이 구분자
print(1, 2, 3, sep=", ")    # 1, 2, 3
print(1, 2, 3, sep="")      # 123
print(1, 2, 3, sep="\n")    # 각 줄에 하나씩

end - 마지막에 붙일 것(기본은 \n)
print("a", end="")      # 개행 없이
print("b")              # ab

for i in range(3):
    print(i, end=" ")   # 0 1 2
    
''.join() - 리스트를 한 줄로
lst = [1,2,3]
for x in lst:
    print(x, end=" ")
    
# 빠른 방법
print(" ".join(map(str, lst))) # 1 2 3


# join은 문자열만 받음
" ".join([1,2,3])       # TypeError!
" ".join(map(str, [1, 2, 3]))   # "1 2 3"

숫자 리스트면 무조건 map(Str, ...)로 변환

출력이 많으면 sys.stdout.write

import sys
sys.stdout.write("\n".join(map(str, results)) + "\n")



7. 입력 끝까지 받기
입력 줄 수가 안 알려진 문제에 쓰는 패턴. EOF까지 계속 읽음

import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break

입력이 끝나면 readline()이 빈 문자열을 반환하고, map에서 언팩할 게 없어 에러가 남. 그걸 잡아서 break하는 것.

import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)

sys.stdin은 그 자체로 반복 가능해서 try없이 EOF까지 읽음

전부 한 번에 읽기
import sys
data = sys.stdin.read().split()

'''



# 최종 정리 - 상황별 템플릿

'''
백준 기본형
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

2차원 격자
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

출력 모아서 한 번에
result = []
for ...:
    result.append(answer)
print("\n".join(map(str, result)))
'''

