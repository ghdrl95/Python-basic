#원본 문자열 입력받아 변수에 저장
원본 = input('원본 문자열 :')
#단어 문자열을 입력받아 변수에 저장
단어 = input('단어 문자열 :')
#원본 문자열에 단어 문자열이 몇개있는지 count함수 사용후 결과값 저장
#count 함수의 반환값은 숫자(정수) 데이터로 변수에 저장해서 사용하거나
#바로 print함수로 출력해도 됨
단어수 = 원본.count(단어)
#결과값 출력
print(단어수)
