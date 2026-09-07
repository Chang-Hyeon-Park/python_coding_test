# 26.08.31.
# [컴프리헨션 1]
# 1부터 n까지 숫자 중 제곱수(1,4,9,16,...)만 리스트로 만드세요.
# 입력 : n=50
# 출력 : [1,4,9,16,25,36,49]
# n = int(input("[컴프리헨션 1] n을 입력하시오. : "))
n = 50
result1 = [i for i in range(1,n+1) if (i**0.5) == int(i**0.5)]
print(result1)


# [컴프리헨션 2]
# 단어 리스트를 받아서, 각 단어를 key로하고 길이를 value로 하는 딕셔너리를 만드세요.(dict comprehension 사용)
# 입력 : ["apple", "kiwi", "banana", "fig"]
# 출력 : {'apple' : 5, 'kiwi' : 4, 'banana' : 6, 'fig' : 3}
# word_input = input("[컴프리헨션 2] 단어 리스트를 입력하시오 (콤마로 구분) : ")
# word_list = [w.strip() for w in word_input.split(",")]

# result2 = {w: len(w) for w in word_list}
# print(result2)

# [컴프리헨션 3]
# 숫자 리스트를 받아서, 3의 배수면 "Fizz", 아니면 그대로 숫자를 담은 리스트를 만드세요.(list comprehension + 삼항연산자 사용)
# 입력 : [1,2,3,4,5,6]
# 출력 : [1,2,'Fizz',4,5,'Fizz']
# num_input3 = input("숫자를 입력하시오 (콤마로 구분) : ")
# num_list3 = [int(i) for i in num_input3.split(",")]
# result3 = ["Fizz" if i%3 == 0 else i for i in num_list3]
# print(result3)


# [슬라이싱 + 컴프리헨션 혼합]
# 2차원 리스트(행렬)를 받아서, 각 행을 뒤집은 새로운 2차원 리스트를 반환하세요.
# 입력 : [[1,2,3],[4,5,6],[7,8,9]]
# 출력 : [[3,2,1],[6,5,4],[9,8,7]]

n = int(input("행의 개수를 입력하시오: "))
matrix = []

for row_num in range(n):
    row_input = input(f"{row_num + 1}번째 행의 숫자를 입력하시오 (콤마로 구분) : ")
    row = [int(i) for i in row_input.split(",")]
    matrix.append(row)

print(matrix)

result_final = [row[::-1] for row in matrix]

print(result_final)