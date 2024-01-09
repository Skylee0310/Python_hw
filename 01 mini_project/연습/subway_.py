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
def take_out() :
    choice1 = input("매장 이용 여부 선택 (예 : 1) : ")
    if choice1.isdecimal() :
        return int(choice1)
def wrong_num():
    while True :
        choice1 = take_out()
        if choice1 >3:
            break

# 메뉴 출력 + 선택 함수
def print_menu() :
    print("1. 클래식 (에그마요, 이탈리안비엠티)")
    print("2. 프레시 라이트 (치킨슬라이스, 로티세리바비큐치킨)")
    print("3. 프리미엄 (쉬림프, 풀드 포크 바비큐)")
def menu1():
    choice2 = input("메뉴 선택 : ")
    if choice2.isdecimal() :
        return int(choice2)

#클래식 항목 출력 + 선택 함수
def print_classic_menu() :
    print("[클래식]")
    print("1. 에그마요")
    print("2. 이탈리안 비엠티")
def classic_menu():
    choice3 = input("샌드위치 선택 : ") #샌드위치 선택
    if choice3.isdecimal():
        if choice3 == 1:
            sandwich = "에그마요"
            price = 5500
            return sandwich, price
        elif choice3 == 2:
            sandwich = "이탈리안 비엠티"
            price = 6900
            return sandwich, price
        else:
            print("▶ 잘못된 메뉴를 선택하셨습니다.")

def print_fresh_light_menu() :
    print("[프레시 라이트]")
    print("1. 치킨 슬라이스")
    print("2. 로티세리 바비큐 치킨")
def fresh_light_menu() :
    choice3 = input("샌드위치 선택 : ") #샌드위치 선택
    if choice3.isdecimal():
        if choice3 == 1:
            sandwich = "치킨 슬라이스"
            price = 6500
            return sandwich, price
        elif choice3 == 2:
            sandwich = "로티세리 바비큐 치킨"
            price = 7300
            return sandwich, price
        else:
            print("▶ 잘못된 메뉴를 선택하셨습니다.")

def print_premium_menu() :
    print("[프리미엄]")
    print("1. 쉬림프")
    print("2. 풀드 포크 바비큐")
def premium_menu() :
    choice3 = input("샌드위치 선택 : ")
    if choice3.isdecimal():
        if choice3 == 1:
            sandwich = "쉬림프"
            price = 7100
            return sandwich, price
        elif choice3 == 2:
            sandwich = "풀드 포크 바비큐"
            price = 7200
            return sandwich, price
        else:
            print("▶ 잘못된 메뉴를 선택하셨습니다.")

# 메뉴를 잘못 선택했을 때
def wrong_menu():
    while True:
        choice2 = print_menu()
        if choice2 >3 :
            break



# 세트 메뉴 선택
def print_set_menu() :
    print("[세트 메뉴]")
    print("1. 쿠키 세트")
    print("2. 칩 세트")
    print("3. 웨지 세트")
    print("4. 세트 선택 안함")
def set_menu():
    choice4 = input("세트 메뉴를 선택하세요 : ")
    if choice4.isdecimal():
        global price
        if choice4 == 1:
            set_ = "쿠키 세트"
            price += 2500
            return set_, price
        elif choice4 == 2:
            set_ = "칩 세트"
            price += 2500
            return set_, price
        elif choice4 == 3:
            set_ = "웨지 세트"
            price += 3100
            return set_, price
        elif choice4 == 4:
            print(f"▶ 세트를 선택하지 않으셨습니다.")
            set_ = "세트 선택 안함"
            return set_, price
        else :
            print("▶ 잘못된 번호입니다. 다시 입력해 주십시오.")

#매장 취식 및 포장 메뉴 출력
print_take_out()

# 매장 취식 및 포장 메뉴 선택
forHere_toGo = take_out()
if forHere_toGo == 1 :
    choice1 = "매장 이용"
    print(f"▶{choice1}을 선택하셨습니다.")
if forHere_toGo == 2 :
    choice1 = "방문 포장"
    print(f"▶{choice1}을 선택하셨습니다.")
# 샌드위치 항목(클래식, 프래시 라이트, 프리미엄) 출력
print_menu()
choice2 = menu1()
if choice2 == 1 :
    print_classic_menu()
    classic_menu()
elif choice2 ==2:
    print_fresh_light_menu()
elif choice2 ==3:
    print_premium_menu()
wrong_num()





