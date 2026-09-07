# 2026.08.31.
# 문제 1 : 국영수 점수 다중 조건 정렬
'''
    학생들의 [이름, 국어, 영어, 수학] 정보가 담긴 2차원 리스트가 주어진다. 다음 조건으로 정렬하는 코드를 작성하라.
    1. 국어 점수가 높은 순(내림차순)
    2. 국어 점수가 같다면 영어 점수가 낮은 순(오름차순)
    3. 국어와 영어 점수가 모두 같다면 수학 점수가 높은 순(내림차순)
    4. 모든 점수가 같다면 이름의 알파벳 순(오름차순)
    
    입력예시
    students = [
        ["Junkyu", 50, 60, 100],
        ["Sangkeun", 80, 60, 50],
        ["Sunghyun", 80, 70, 100],
        ["Soong", 50, 60, 90],
        ["Haebin", 50, 60, 100]
    ]
    
    출력예시
    [['Sangkeun', 80, 60, 50], ['Sunghyun', 80, 70, 100], ['Haebin', 50, 60, 100], ['Junkyu', 50, 60, 100], ['Soong', 50, 60, 90]]
'''

# def sort_practice1(x):
#     x.sort(key=lambda item: (-item[1], item[2], -item[3], item[0]))
#     return x

# def main():
#     students = [
#         ["Junkyu", 50, 60, 100],
#         ["Sangkeun", 80, 60, 50],
#         ["Sunghyun", 80, 70, 100],
#         ["Soong", 50, 60, 90],
#         ["Haebin", 50, 60, 100]
#     ]
#     result = sort_practice1(students)
#     print(result)

# if __name__ == "__main__":
#     main()

# 문제 2 : 단어 길이 우선 및 문자열 내림차순 정렬(문자열 응용)
'''
    단어가 들어있는 1차원 리스트가 있다. 중복된 단어를 먼저 제거한 뒤, 다음 조건으로 정렬하라.
    1. 단어의 길이가 짧은 순서대로(오름차순)
    2. 길이가 같다면 알파벳 역순으로(내림차순, -ord() 활용)
    
    입력 예시
    words = ["but", "i", "wont", "hesitate", "no", "more", "no", "more", "it", "cannot"]
    
    출력 예시
    ['i', 'no', 'it', 'but', 'more', 'wont', 'cannot', 'hesitate']
'''

# def unique_words(x):
#     unique_set = set(x)
#     res = list(unique_set)
#     return res

# def sort_practice2(x):
#     words = unique_words(x)
#     words.sort(key=lambda item: (len(item), [-ord(c) for c in item]))
#     return words

# def main():
#     words = ["but", "i", "wont", "hesitate", "no", "more", "no", "more", "it", "cannot"]
#     result = sort_practice2(words)
#     print(result)

# if __name__ == "__main__":
#     main()

# 문제 3 : 회의실 배정(Greedy 핵심 정렬)
'''
    각 회의의 [시작시간, 종료시간] 정보가 담긴 2차원 리스트가 주어진다.
    회의실을 최대한 많이 배치하기 위해 종료 시간이 빠른 순, 종료 시간이 같다면 시작 시간이 빠른 순으로 정렬하시오.
    
    입력 예시
    meetings = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
    
    출력 예시
    [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14], [2, 13]]
'''


# 문제 4 : 조건별 우선순위 가중치 정렬(커스텀 정렬)
'''
    정수 리스트가 주어질 때, 다음 특수 조건에 맞춰 정렬하시오.
    1. 3의 배수가 3의 배수가 아닌 수보다 무조건 앞에 와야 한다.
    2. 3의 배수끼리는 큰 수가 앞에 오는 내림차순으로 정렬한다.
    3. 3의 배수가 아닌 수끼리는 작은 수가 앞에 오는 오름차순으로 정렬한다.
    
    힌트 : 튜플 1순위에 x%3 != 0을 넣으면 3의 배수가 0이 되어 앞에 서게 된다.
    
    입력 예시
    numbers = [1, 9, 3, 4, 12, 7, 5, 6]
    
    출력 예시
    [12, 9, 6, 3, 1, 4, 5, 7]
'''


# 문제 5 : 딕셔너리 데이터 종합 정렬(실전 구현)
'''
    게임 유저들의 정보가 딕셔너리 리스트 형태로 주어진다.
    1. 레벨(level)이 높은 유저 순(내림차순)
    2. 레벨이 같다면 점수(score)가 높은 유저 순(내림차순)
    3. 레벨과 점수가 모두 같다면 아이디(id)가 빠른 순(오름차순)
    
    입력 예시
    users = [
        {"id": "userC", "level": 10, "score": 500},
        {"id": "userA", "level": 10, "score": 700},
        {"id": "userB", "level": 20, "score": 300},
        {"id": "userD", "level": 10, "score": 500}
    ]
    
    출력 예시
    [{'id': 'userB', 'level': 20, 'score': 300}, {'id': 'userA', 'level': 10, 'score': 700}, {'id': 'userC', 'level': 10, 'score': 500}, {'id': 'userD', 'level': 10, 'score': 500}]
'''