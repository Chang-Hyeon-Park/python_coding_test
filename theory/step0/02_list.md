# 2단계 : 리스트 / 문자열 다루기

1) 인덱싱 & 음수 인덱스

s = "PYTHON"
s[0]    # 'P'
s[5]    # 'N'
s[-1]   # 'N'
s[-2]   # 'O'

lst = [1,2,3]
lst[0] = 99     # OK -> [99,2,3]

s = "abc"
s[0] ='X'   # TypeError! 문자열은 수정 불가(immutable)
s = 'X' + s[1:] # 이렇게 새로 만들어야 함

2) 슬라이싱
형태는 [start : stop : step] stop은 포함 안 됨

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a[2:5]      # [2, 3, 4]      ← 5는 제외
a[:3]       # [0, 1, 2]      ← start 생략 = 처음부터
a[7:]       # [7, 8, 9]      ← stop 생략 = 끝까지
a[:]        # 전체 복사
a[::2]      # [0, 2, 4, 6, 8]   ← 2칸씩
a[1::2]     # [1, 3, 5, 7, 9]   ← 홀수 인덱스만
a[::-1]     # [9, 8, ..., 0]    ← 뒤집기 (자주 씀!)
a[-3:]      # [7, 8, 9]         ← 뒤에서 3개
a[:-3]      # [0, ..., 6]       ← 뒤 3개 빼고

* 슬라이싱은 범위를 넘어가도 절대 에러가 안난다.
a = [1, 2, 3]
a[10]     # IndexError
a[1:10]   # [2, 3]   ← 에러 안 남, 알아서 잘라줌
a[10:20]  # []       ← 빈 리스트


* 슬라이싱은 새 객체를 만든다.
a = [1, 2, 3]
b = a        # 같은 리스트를 가리킴
c = a[:]     # 복사본 (별개)

b[0] = 99    # a도 [99,2,3]으로 바뀜
c[0] = 77    # a는 그대로


* 슬라이스에 대입도 가능(리스트 한정)
a = [1,2,3,4,5]
a[1:3] = [10, 20, 30]

# 3) sort() vs sorted()

lst.sort()
 - 대상 : 리스트만
 - 동작 : 원본을 직접 정렬
 - 반환값 : None

sorted(x)
 - 대상 : 모든 iterable (문자열, 튜플, dict, set, ...)
 - 동작 : 원본 그대로, 새 리스트 반환
 - 반환값 : 정렬된 리스트

a = [3, 1, 2]
b = a.sort()     # b는 None!!  ← 절대 이렇게 쓰지 마
print(b)         # None

a.sort()         # 이게 맞음 → a == [1,2,3]
b = sorted(a)    # 또는 이게 맞음


* reverse=True - 내림차순
sorted([3,1,2], reverse=True)   # [3, 2, 1]

* key= -> 정렬 기준을 함수로 지정. 각 원소를 그 함수에 넣은 결과값으로 비교함.

words = ["banana", "kiwi", "apple"]

sorted(words)                  # ['apple','banana','kiwi']  사전순
sorted(words, key=len)         # ['kiwi','apple','banana']  길이순
sorted(words, key=str.lower)   # 대소문자 무시


* lambda로 커스텀 기준
data = [("철수", 90), ("영희", 85), ("민수", 90)]

sorted(data, key=lambda x: x[1])              # 점수 오름차순
sorted(data, key=lambda x: -x[1])             # 점수 내림차순 (숫자면 -로 뒤집기 가능)
sorted(data, key=lambda x: (-x[1], x[0]))     # 점수 내림차순, 같으면 이름 오름차순

key에 튜플을 주면 앞에서부터 순서대로 비교해. 다중 기준 정렬의 정석이고 코테에서 진짜 자주 나온다.

안정 정렬(stable): 값이 같으면 원래 순서를 유지해. 그래서 기준이 여러 개일 때 "덜 중요한 기준으로 먼저 정렬 → 중요한 기준으로 다시 정렬"도 가능하지만, 그냥 튜플 쓰는 게 낫다.


4) 문자열 메서드
* 문자열 메서드는 전부 새 문자열을 반환함. 원본은 안바뀜

s = "  Hello World  "
s.strip()          # "Hello World"
print(s)           # "  Hello World  "  ← 원본 그대로!
s = s.strip()      # 대입해야 반영됨

"a b c".split()           # ['a','b','c']
"a,b,c".split(",")        # ['a','b','c']
"a,,b".split(",")         # ['a','','b']   ← 빈 문자열도 생김
"a   b\n c".split()       # ['a','b','c']  ← 인자 없으면 공백/개행 알아서 처리
"a:b:c".split(":", 1)     # ['a', 'b:c']   ← 최대 1번만 분리

인자 없는 split()은 연속 공백을 하나로 취급하고 앞뒤 공백도 무시해. 인자를 주면 정확히 그 구분자마다 자른다. 이 차이가 은근 함정.


* join() - split의 반대. 구분자.join(리스트)

" ".join(['a','b','c'])    # "a b c"
"".join(['a','b','c'])     # "abc"
"-".join(['a','b','c'])    # "a-b-c"

nums = [1, 2, 3]
" ".join(nums)              # TypeError! 원소가 전부 문자열이어야 함
" ".join(map(str, nums))    # "1 2 3"  ← 이 패턴 외워두기


* strip()/lstrip()/rstrip()

"  hi  ".strip()      # "hi"
"  hi  ".lstrip()     # "hi  "
"xxhixx".strip("x")   # "hi"
"ab#c#ba".strip("ab") # "#c#"  ← 문자 '집합'이지 문자열 통째가 아님

* replace(old, new, count)

"aXbXc".replace("X", "-")      # "a-b-c"
"aXbXc".replace("X", "-", 1)   # "a-bXc"
"a b c".replace(" ", "")       # "abc"  ← 공백 제거에 자주 씀

* 같이 알아두면 좋은 것들
s.upper() / s.lower()
s.find("x")      # 없으면 -1
s.index("x")     # 없으면 ValueError
s.count("a")
s.startswith("ab") / s.endswith("cd")
s.isdigit() / s.isalpha() / s.isalnum()
"abc" in s       # 포함 여부


