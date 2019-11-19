# 문제명  : 프린터
# 스택 큐 
def solution(priorities, location):
    answer = 0
    max_p = max(priorities)
    while True:
        paper = priorities.pop(0)
        if max_p == paper:
            answer += 1 
            # 첫 번째 라는 뜻.
            if location == 0:
                break;
            else:
                location -= 1
                max_p = max(priorities)
        else:
            # 종이를 다시 맨 뒤로
            priorities.append(paper) 
            
            if location == 0:
                # 내가 원한 종이가 다시 맨 뒤로 간것임.
                location = len(priorities) -1
            else:
                location -= 1
    return answer