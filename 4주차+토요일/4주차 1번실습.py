성적 = [50,80,30,99,60]
#while문을 사용했을 경우
횟수 = 0
while 횟수 < 5:
    if 성적[횟수] >= 60:
        print('%s번째 학생 합격' % (횟수+1) )
    else:
        print('%s번째 학생 불합격'% (횟수+1) )
    횟수 += 1
#for문을 사용했을 경우
#성적 변수가 가진 리스트의 요소를 순차적으로 추출해 점수 변수에 대입
'''
enumerate(리스트,튜플) : 해당 리스트/튜플의 값과 반복횟수를 페어로 묶어주는 함수
enumerate([50,60,70,80])
-> [ (0, 50), (1,60), (2,70), (3,80) ]
'''
#print(enumerate(성적))
for 횟수, 점수 in enumerate(성적):
    print(횟수, 점수)

    if 점수 >= 60:
        print('%s번째 학생 합격' % (횟수+1) )
    else:
        print('%s번째 학생 불합격' % (횟수+1))


















