# 문제명 : 모의고사
# 완전탐색 


def solution(answers):
    math_students = [ [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5] ]
    answer_check = {'1' :{'point' : 0}, '2' : {'point' : 0}, '3' : {'point' : 0} }
    
    for idx, student in enumerate(math_students):
        for answer_idx, answer in enumerate(answers):
            if student[answer_idx % len(student)] == answer:
                answer_check[str(idx+1)]['point'] +=1
                
    result = list(answer_check.values())
    max_point = max(score['point'] for score in result)
    
    
    return [idx +1 for idx, score in enumerate(result) if score['point'] >= max_point]


def solution2(answers):
    math_students = [ [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5] ]
    answer_check = {'1': 0, '2': 0 , '3': 0} 
    
    for answer_idx, answer in enumerate(answers):
        for st_idx, student in enumerate(math_students):
            if student[answer_idx%len(student)] == answer:
                answer_check[str(st_idx+1)] += 1
    
    result = list(answer_check.items())


    return [ int(point[0]) for point in result if point[1] == max(result, key = lambda k : k[1])[1] ]

    