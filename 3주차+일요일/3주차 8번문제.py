'''
100 미만의 양의 정수들이 주어진다.
입력받다가 0 이 입력되면 마지막에 입력된 0 을 제외하고
그 때까지 입력된 정수의 십의 자리 숫자가 각각 몇 개인지 작은 수부터
출력하는 프로그램을 작성하시오. (0개인 숫자는 출력하지 않는다.)
'''
#사전형/리스트 변수 초기화 {0:0 1:0 2:0 ... 9:0} [0,0,0,0,0,0,0,0,0,0]
사전 = {0:0 ,1:0 ,2:0 ,3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
리스트 = [0,0,0,0,0,0,0,0,0,0]
#반복문 -무한루프
while True:
    #사용자의 정수값 입력
    입력 = int(input())
    #사용자 입력이 0과 같은 경우 반복문 빠져나가기
    if 입력 == 0:
        break
    #10자리의 값 추출 (10으로 나눴을때의 몫으로 연산 가능)
    인덱스 = 입력 // 10 #15 -> 1 85 -> 8 
    #10자리 값을 인덱스로 사용해서 누적 (+1)
    사전[인덱스] += 1

#반복문에 사용할 횟수변수 초기화
횟수 = 0
#반복문 0~9 반복
while 횟수 < 10: #횟수 <= 9
    #사전형 변수에 '횟수'인덱스의 값이 0보다 큰 경우,
    if 사전[횟수] > 0:
        #횟수 : 저장된 값 출력
        print("%s : %s" % (횟수, 사전[횟수]) )
    #횟수 + 1  
    횟수 += 1 
























