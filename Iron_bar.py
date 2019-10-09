# 문제명 : 쇠막대기
# 스택 큐

 def solution(arrangement):
        answer = 0
    arrangement = arrangement.replace('()', 'l')
    stack = []
    for iron in arrangement:
        if iron == '(':
            stack.append(1)
        elif iron ==')':
            stack.pop()
            answer += 1
        else :
            answer += len(stack)
    return answer