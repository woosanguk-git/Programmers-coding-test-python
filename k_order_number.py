
# 문제명 : k 번째 수 
# 정렬

def solution(array, commands):
    answer = []
    for command in commands:
        answer.append(sorted(array[command[0]-1:command[1]], key = lambda x: x)[command[2]-1])
    return answer