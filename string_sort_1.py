# 문제명 : 문자열 내 마음대로 정렬하기
# 연습문제

def solution(strings, n):
    answer = []
    temp =[]
    
    return sorted(strings, key = lambda x:(x[n],x))