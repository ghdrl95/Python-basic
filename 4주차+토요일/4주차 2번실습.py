#학생별 영어,수학 성적의 평균
성적 = [[50,30],[80,50],[30,100],[99,20],[60,70]]
영어 = 수학 = 0
#for문을 사용했을 경우
#성적 변수가 가진 리스트의 요소를 순차적으로 추출해 점수 변수에 대입
'''
for 점수 in 성적:
    print(점수)
    영어 += 점수[0]
    수학 += 점수[1]
'''
#언패키징을 for문에서 활용
for 학영, 학수 in 성적:
    print(학영,학수)
    영어 += 학영
    수학 += 학수
print(영어//5 , 수학 //5)
