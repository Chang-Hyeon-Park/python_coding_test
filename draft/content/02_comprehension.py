# 26.08.31.
# list comprehension
'''
표현 방식
    리스트 : 대괄호 [ ]
    사전 : 중괄호 { }
    집합 : 괄호 ( )
'''

squares = [x**2 for x in range(10)]

print("squares = ", squares)

evens = [x for x in range(20) if x % 2 == 0]

print("evens = ", evens)

# dict comprehension
word_len = {w: len(w) for w in ["apple", "banana", "kiwi"]}
print("word_len = ", word_len)

word = "Hello"
word_dict = {w: word.count(w) for w in word}
print("word_dict = ", word_dict)



# 집합 comprehension
numbers = [1,2,3,2,1]
unique_numbers = {n for n in numbers}
print("집합 comprehension : ", unique_numbers)

# 조건 + 변환 동시에
labels = ["짝" if x % 2 == 0 else "홀" for x in range(10)]

print("labels = ", labels)