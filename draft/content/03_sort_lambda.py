# 2026.08.31.
# sort()/sorted() + key/lambda 활용
'''
    파이썬의 sort()와 sorted()는 모두 key 매개변수로 정렬 기준 함수를 전달받음
    보통 짧고 명확한 lambda(익명 함수)를 함께 사용
    
    list.sort() : 원본 리스트를 직접 변경함(반환값 None)
    sorted(iterable) : 원본은 유지하고, 정렬된 새 리스트를 반환함
'''

matrix = [[3, 10], [1,20], [2,5]]

# 0번째 원소(첫 번째 열) 기준 오름차순 정렬
matrix.sort(key=lambda x : x[0])
print(matrix)

# 0번째 원소(첫 번째 열) 기준 내림차순 정렬
matrix.sort(key=lambda x : -x[0])
print(matrix)

# 1번째 원소(두 번째 열) 기준 오름차순 정렬
matrix.sort(key=lambda x : x[1])
print(matrix)

# 마지막 열 기준 오름차순 정렬
matrix.sort(key=lambda x : x[-1])
print(matrix)

# 마지막 열 기준 내림차순 정렬
matrix.sort(key=lambda x : -x[-1])
print(matrix)

# 1번째 원소(두 번째 열) 기준 내림차순 정렬
matrix.sort(key=lambda x : -x[1])
print(matrix)


'''
    튜플() 정렬의 핵심 동작 방식
    파이썬에서 key=lambda x: (-x[0], x[1])처럼 튜플을 반환하면 파이썬에서는 다음과 같이 비교를 진행
    
    data = [[2, 'b'], [1, 'c'], [2, 'a']]
    
    1. 각 요소 변환
        [2, 'b'] -> (-2, 'b')
        [1, 'c'] -> (-1, 'c')
        [2, 'a'] -> (-2, 'a')
    
    2. 1순위 비교(-x[0])
    3. 2순위 비교(x[1])
    최종
        [[2, 'a'], [2, 'b'], [1, 'c']]
'''
data = [[2, 'b'], [1, 'c'], [2, 'a']]

data.sort(key=lambda x : (x[0], x[1]))
print(data)

data.sort(key=lambda x : (x[0], x[1]), reverse=True)
print(data)

'''
    lambda 매개변수 : 반환할_식
'''

# lambda가 자주 쓰이는 3가지 대표 패턴
# 1. sort() / sorted()의 key 매개변수
# -> 리스트에서 원소를 하나씩(x) 꺼내어, "무엇을 기준으로 비교할지" 정할 때 쓰임

words = ["python", "c", "java"]
words.sort(key=lambda x : len(x))
print(words)

# 2. map() 함수와 조합
# 리스트의 모든 원소에 똑같은 연산을 적용할 때 사용
numbers = [1,2,3,4,5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# 3. filter() 함수와 조합
# 조건에 맞는 원소만 골라낼 때 사용
numbers = [1,2,3,4,5,6]
evens = list(filter(lambda x : x%2 == 0, numbers))
print(evens)

'''
    ord(), chr()
    ord(문자) : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환.
    chr(정수) : 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환.
'''
print(ord('A')) # 결과 : 65
print(chr(65)) # 결과 : A

