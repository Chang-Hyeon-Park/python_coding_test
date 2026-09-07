# 해답 1
# def is_pair(s):
#     st = list()
#     for c in s:
#         if c == '(':
#             st.append(c)
        
#         if c == ')':
#             try:
#                 st.pop()
#             except IndexError:
#                 return False
#     return len(st) == 0

# print(is_pair("(hello)()"))
# print(is_pair("()()()"))
# print(is_pair(")()"))

# 해답 2
def is_pair(s):
    pair = 0
    for x in s:
        if pair < 0:
            break        
        if x == "(":
            pair += 1
        elif x == ")":
            pair -= 1
        else:
            pair
        
    return pair == 0