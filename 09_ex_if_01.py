'''
[요청] 키보드로 숫자를 입력 받아서 입력 받은 숫자 만큼
    *을 화면에 출력해 주세요.
[해결]   (1) 숫자 입력 받기 => input()
            str => int 형 변환
        (2) 입력 받은 숫자 만큼 * 출력 => '*' *숫자
'''
# 1) 숫자 입력
num = input("정수 입력 : ")

# 입력 받은 문자 有/無 => len(num) > 0
if len(num) > 0 : # num의 길이가 0보다 클 때 (=> 입력값이 있을 때)
    # 2) str => int 형 변환
    num = int(num)

    # 3) '*' 출력
    print('*'*num)
else : #조건 len(num)>0이 False일 때 실행되는 코드 부분
    print("입력된 숫자가 없습니다.")

print("END") # 조건에 상관없이 실행.
