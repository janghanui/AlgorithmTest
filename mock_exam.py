def solution(answers):
    answer = []
    
    person1=[1,2,3,4,5]                    #1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    person2=[2,1,2,3,2,4,2,5]              #2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    person3=[3,3,1,1,2,2,4,4,5,5]          #3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
    p1=0                                   #1, 2, 3번 수포자의 점수 산출 변수
    p2=0
    p3=0
    
    for i in range(len(answers)):          #점수 산출
        if answers[i]==person1[i%5]:
            p1+=1
        if answers[i]==person2[i%8]:
            p2+=1
        if answers[i]==person3[i%10]:
            p3+=1
    
    a=max(p1,p2,p3)                        #최고점수
    if p1==a:
        answer.append(1)
    if p2==a:
        answer.append(2)
    if p3==a:
        answer.append(3)
    answer.sort()                          #가장 높은 점수를 받은 사람이 여럿일 경우 → 오름차순 정렬
    
    return answer
