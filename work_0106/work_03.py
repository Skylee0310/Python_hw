'''
1. 반복문
2. q, Q 입력 전까지 동작.
3. 대문자 Q 제외한 나머지
4.
'''
while True :
    alpha = input("'q', 'Q' 입력 전까지 동작 : ")
    if alpha.isdecimal() :
        alpha = int(alpha)
        print(alpha * " ◎ ")
    elif alpha.isalpha() :
        if alpha.isupper() and alpha != "Q" :
            print("♠")
        elif alpha.islower() and alpha != "q" :
            print("♤")
        elif alpha == 'q' or alpha == 'Q':
            print("프로그램 종료합니다.")
            break


