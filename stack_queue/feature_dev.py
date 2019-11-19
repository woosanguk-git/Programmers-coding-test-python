# 문제명 : 기능개발
# 스택 큐


def solution(progresses, speeds):

    # 큐에 넣는 다고 생각하고
    # 큐는 먼저 들어온게 먼저 나간다.
    # 먼저 들어온게 100 이 되었을 때 나가는데 나간 후에 뒤에것도 진도수100이면
    # 내보내고 배포개수 +1
    # 큐가 비워질때 까지 한다.
    answer = []
    while len(progresses) != 0:
        count = 0
        progresses = [progress+speed for progress,
                        speed in zip(progresses, speeds)]
        while len(progresses) != 0:
            if progresses[0] >= 100:
                # print(progresses)
                count += 1
                del progresses[0]
                del speeds[0]
            else:
                break
        if count!=0:
            answer.append(count)

    return answer


li = [93,30,55]
li2 = [1,30,5]

# del li[0]
# print(li[0])

print(solution(li,li2))