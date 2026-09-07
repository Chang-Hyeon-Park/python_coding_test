'''
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

입출력 예
s	answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false
입출력 예 설명
입출력 예 #1,2,3,4
문제의 예시와 같습니다.

'''

def gualho(s):
    cnt_f = 0
    cnt_r = 0
    if s[0] == ")":
        return False
    for i in range(len(s)):
        if s[i] == "(":
            cnt_f += 1
        elif s[i] == ")":
            cnt_r += 1
        else:
            return print("똑바로 입력해라 이녀석아")
        
        if cnt_f < cnt_r:
            return False
    if cnt_f == cnt_r:
        return True
    else:
        return False
    

def main():
    input_s = input("괄호만 이루어진 문자열을 입력하시오. : ")
    result = gualho(input_s)
    if result:
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()