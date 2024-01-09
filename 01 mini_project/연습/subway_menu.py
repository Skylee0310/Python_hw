'''
서브웨이 키오스크 주문하기(약식)
1) 매장 이용/ 방문 포장

2) 메뉴 선택 + 개수 선택
    2-1) 샌드위치 (메뉴 출력)
     2-1-1) 클래식 : 에그마요, 이탈리안비엠티, 햄, 참치,
        2-1-2) 프레시 라이트 : 치킨슬라이스, 치킨베이컨아보카도, 로티세리바비큐치킨, 써브웨이클럽
        2-1-3) 프리미엄 : 스파이시 쉬림프, 쉬림프, 풀드 포크 바비큐, 스테이크&치즈, 치킨 데리야끼
        + 세트 메뉴 추가
     2-2) 세트 메뉴 추가 선택
'''
# 함수1 : 매장이용/방문 포장 선택
# 함수2 : 메뉴 출력
# 함수3 : 가격

def print_take_out() :
    print("1. 매장 이용")
    print("2. 방문 포장")
    print("3. 주문 종료")
    hereToGo = input("매장 이용 여부 선택 (예: 1) : ")
    if hereToGo.isdecimal() :
        hereToGo=int(hereToGo)
        if hereToGo == 1 :
            print("▶ 매장 이용을 선택하셨습니다.")
        elif hereToGo == 2 :
            print("▶ 방문 포장을 선택하셨습니다.")
    return hereToGo
def take_out() :
    while True :
        hereToGo = print_take_out()
        if hereToGo == 3:
            print("▶ 주문을 종료합니다.")
            break
        elif hereToGo > 3:
            print("▶ 잘못된 번호를 입력하셨습니다.")


def print_menu() :
    print("1. 클래식 (에그마요, 이탈리안비엠티)")
    print("2. 프레시 라이트 (치킨슬라이스, 로티세리바비큐치킨)")
    print("3. 프리미엄 (쉬림프, 풀드 포크 바비큐)")
    while True :
        menu1 = input("메뉴 번호를 입력하세요 : ")
        if menu1.isdecimal() :
            menu1 = int(menu1)
            if menu1 == 1 :
                print("▶ 클래식 메뉴를 선택하셨습니다")
                break
            elif menu1 == 2 :
                print("▶ 프레시 라이트 메뉴를 선택하셨습니다")
                break
            elif menu1 == 3 :
                print("▶ 프리미엄 메뉴를 선택하셨습니다")
                break
            return menu1
def menu1() :
    while True :
        menu1 = print_menu()
        if print_menu()>3 :
            print("▶ 잘못된 번호를 입력하셨습니다.")





#매장 이용 여부 선택
print_take_out()
take_out()

#메뉴 선택
print_menu()
menu1()