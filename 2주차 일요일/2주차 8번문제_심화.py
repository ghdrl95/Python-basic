#40분 까지 직접해보기
#정수값 입력
값 = int(input())
#카운팅할때 사용할 변수 초기화
수 = 1
#누적할때 사용할 변수 초기화
누적 = 0
#사용자 입력만큼 반복 (카운트변수 <= 사용자 정수값)
while 수 <= 값:
    #누적 연산
    누적 += 수 #1+2+3+...+값 까지 누적
    #카운팅
    수 += 1 #수 : 1,2,3,...,값 변경
#결과출력
print(누적)
