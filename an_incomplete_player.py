# 문제명 : 완주하지 못한 선수
# 해쉬 hash

def solution(participant, completion):
    answer = ''
    dictParticipant ={}  #dict자료형
    hashNumber = 0

    for partName in participant:
        dictParticipant[hash(partName)] = partName  #dict 자료형 만들어주기.
        hashNumber += int(hash(partName))

    for comName in completion:
        hashNumber -= int(hash(comName))

    answer = dictParticipant[hashNumber]
    return answer