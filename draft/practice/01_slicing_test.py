# 2026.08.31.

# [슬라이싱 1]
# 주어진 리스트를 뒤집어서 반환하세요.(슬라이싱만 사용, revcerse() 금지)
# 입력 : [1,2,3,4,5]
# 출력 : [5,4,3,2,1]

lst1 = [1,2,3,4,5]
print("[슬라이싱 1] : ", lst1[::-1])

# [슬라이싱 2]
# 리스트에서 앞2개, 뒤2개를 제거한 나머지를 반환하세요.
# 입력 : [1,2,3,4,5,6,7,8]
# 출력 : [3,4,5,6]

lst2 = [1,2,3,4,5,6,7,8]
print("[슬라이싱 2] : ", lst2[2:6])

# [슬라이싱3] 
# 인덱스가 짝수인 원소만 뽑아 리스트로 반환하세요.
# 입력 : [10,20,30,40,50,60]
# 출력 : [10,30,50]

lst3 = [10,20,30,40,50,60]
print("[슬라이싱 3] : ", lst3[::2])

# [슬라이싱 4]
# 문자열이 앞뒤로 똑같이 읽히는지(팰린드롬) 슬라이싱으로 검사하세요.
# 팰린드롬(palindrome) : 앞으로 읽으나 뒤로 읽으나 똑같이 읽히는 단어 (회문)
# 입력 : "level"
# 출력 : True
# 입력 : "hello"
# 출력 : False

# def palindrome(string x)
# {
#     string_compare = x[::-1]
#     cnt = 0
#     for i in range(sizeof(x))
#     {
#         if(x[i] == string_compare[i])
#         {
#             continue
#         }
#         else
#         {
#             cnt++
#         }
#     }
#     if cnt > 0
#         return False
#     else
#         return True
# }

# string1 = "level"

# result = palindrome(string1)
# if (result == 1)
# {
#     print("True")
# }
# else
# {
#     print("False")
# }

# 해답 01
# def palindrome(x):
#     string_compare = x[::-1]
#     cnt = 0
#     for i in range(len(x)):
#         if x[i] == string_compare[i]:
#             continue
#         else:
#             cnt += 1;
#     if cnt > 0:
#         return False;
#     else:
#         return True;

# def main():
#     string1 = input("[슬라이싱 4] 문자열을 입력하세요: ")
#     result = palindrome(string1)
#     if result == 1:
#         print("True")
#     else:
#         print("False")
        
# if __name__ == "__main__":
#     main()

# 해답 02
# def palindrome(x) -> bool:
#     for i in range(len(x) // 2):
#         if x[i] != x[len(x) - 1 - i]:
#             return False
#     return True

# def main():
#     string1 = input("[슬라이싱 4] 문자열을 입력하세요: ")
#     print(palindrome(string1))

# if __name__ == "__main__":
#     main()
    
# [슬라이싱 5]
# 문자열에서 처음 3글자와 마지막 3글자를 제외한 가운데 부분만 반환하세요.
# 입력 : "programming"
# 출력 : "gramm"
# def slicing5(x):
#     return x[3:-3]

# def main():
#     input = "programming"
#     print("[슬라이싱 5] : ",slicing5(input))

# if __name__ == "__main__":
#     main()

# [슬라이싱 6]
# 리스트를 왼쪽으로 k칸 회전시킨 결과를 반환하세요.(슬라이싱 조합 사용)
# 입력 : [1,2,3,4,5], k=2
# 출력 : [3,4,5,1,2]

k = 2
lst6 = [1,2,3,4,5]
print("[슬라이싱 6] : ", lst6[k:] + lst6[:k])
