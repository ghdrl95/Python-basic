'''
컴퓨터랑 가위바위보 게임하기
사용자가 가위(1), 바위(2), 보(3) 입력
컴퓨터가 랜덤하게 가위/바위/보 선택
10판했을때 얼마나이겼는지 출력
'''
#다른 개발자가 만들어 놓은 함수/변수를 사용할때, import 라이브러리명으로 사용할 수 있음
import random #random 라이브러리를 쓸수있도록 설정
#사용자가 이긴횟수 저장하는 변수, 반복문에 사용할 변수 초기화
이김 = 0
횟수 = 0
#반복문 - 10번 반복
while 횟수 < 10:
    print("%s번째 게임 시작" % (횟수+1) )
    #반복문 - 가위바위보 게임이 끝날때까지
    while True:
        #사용자 입력 - 가위/바위/보
        입력 = input('가위(1) 바위(2) 보(3) 입력 : ')
        #입력이 '1','2','3'이 아닌경우
        if not (입력 == '1' or 입력 =='2' or 입력 =='3'):
            print('잘못된 입력입니다.')
            continue
        #컴퓨터가 랜덤으로 가위/바위/보 선택
        #random.randint(시작범위,종료범위) : 시작범위~종료범위 값중 정수값 하나를 출력하는 함수
        컴퓨터 = str(random.randint(1,3))#'1'
        #if문 활용 누가 이겼는지/ 비겼는지 확인
        #비겼는지 확인
        if 입력 == 컴퓨터:
            print('비겼습니다!')
        #사용자가 이겼는지 확인
        elif (입력 == '1' and 컴퓨터 =='3') or (입력 == '2' and 컴퓨터 =='1') or (입력=='3' and 컴퓨터 == '2'):
            print('이겼습니다!')
            이김 += 1
            break
        else :
            print('졌습니다!')
            break
    횟수 += 1
print('컴퓨터를 %s번 이겼습니다' % 이김)
















