# 승민 없는 승민팀!!!
'''서브웨이 키오스크 주문하기
1) 매장 이용 / 방문 포장

2) 메뉴 선택
    2-1) 샌드위치 (메뉴 출력)
        2-1-1) 클래식 : 에그마요, 이탈리안비엠티, 햄, 참치,
        2-1-2) 프레시 라이트 : 치킨슬라이스, 로티세리바비큐치킨
        2-1-3) 프리미엄 : 쉬림프, 풀드 포크 바비큐, 스테이크&치즈
        X 치즈 추가(슈레드/모차렐라/아메리칸 치즈) 선택 불가.
        X 야채(양상추/토마토/오이/피망/양파/피클/올리브/할라피뇨) 선택 불가.
        + 세트 메뉴 추가
        ※ 음료 선택 불가.
'''
#함수1 : 매장 이용 / 방문 포장 / 종료 선택 메뉴 출력
def print_togo() :
    print("1. 매장 이용")
    print("2. 방문 포장")
    print("3. 프로그램 종료")
#함수2 : 입력이 잘못되었을 경우 메시지를 출력
def wrong_num() :
    print("▶ 잘못된 번호를 입력하셨습니다.")

#함수3 : 인수가 decimal(십진수)일 때 정수(int)로 반환.
def num_int(n):
    #n은 str
    if n.isdecimal() :
        n=int(n)
        return n
    else:
        print("숫자를 입력해 주십시오.")

#함수4 : 샌드위치 항목 메뉴 출력
def print_menu1() :
    print("[샌드위치 선택]")
    print("1. [클래식] : 에그마요, 이탈리안비엠티")
    print("2. [프레시 라이트] : 치킨 슬라이스, 로티세리 바비큐 치킨")
    print("3. [프리미엄] : 쉬림프, 풀드 포크 바비큐")

#함수4 : 클래식 샌드위치 메뉴 출력
def print_classic() :
    print("[클래식]")
    print("1. 에그마요")
    print("2. 이탈리안 비엠티")

# 함수5 : 프레시 라이트 샌드위치 메뉴 출력
def print_fresh_light() :
    print("[프레시 라이트]")
    print("1. 치킨 슬라이스")
    print("2. 로티세리 바비큐 치킨")

# 함수6 : 프리미엄 샌드위치 메뉴 출력
def print_premium():
    print("[프리미엄]")
    print("1. 쉬림프")
    print("2. 풀드 포크 바비큐")

# 함수 7 : 주문개수
def order():
    num = input("주문 개수를 입력하세요(예 : 1) : ")
    num = num_int(num)
    return num
# 메뉴 (함수8~13) : 샌드위치 메뉴
# 함수8 : 에그마요
def egg_mayo() :
    num = order()
    global price
    price = 6500*num
    sandwich = "에그마요"
    print(f"▶ [{sandwich}]을/를 {num}개 선택하셨습니다.")
    return sandwich
#함수 9 : 이탈리안 BMT
def italian_BMT() :
    num = order()
    global price
    price =  6900*num
    sandwich = "이탈리안 비엠티"
    print(f"▶ [{sandwich}]을/를 {num}개 선택하셨습니다.")
    return sandwich
#함수 10 : 치킨 슬라이스
def chicken_slice() :
    num =order()
    global price
    price = 6500*num
    sandwich = "치킨 슬라이스"
    print(f"▶ [{sandwich}]을/를 {num}개 선택하셨습니다.")
    return sandwich

#함수 11 : 로티세리 바비큐 치킨
def chicken_BBQ() :
    num = order()
    global price
    price = 7300*num
    sandwich = "로티세리 바비큐 치킨"
    print(f"▶ [{sandwich}]을/를 {num}개 선택하셨습니다.")
    return sandwich
#함수 12 : 쉬림프
def shrimp() :
    num = order()
    global price
    price = 7100*num
    sandwich = "쉬림프"
    print(f"▶ [{sandwich}]을/를 {num}개 선택하셨습니다.")
    return sandwich

# 함수 13 : 풀드 포크
def pulled_pork() :
    num = order()
    global price
    price = 7100*num
    sandwich = "풀드 포크 바비큐"
    print(f"▶ [{sandwich}]을/를 {num}개 선택하셨습니다.")
    return sandwich

#함수 14 : 세트 메뉴 메뉴판 출력
def print_set() :
    print("[세트 메뉴]")
    print("1. 쿠키 세트")
    print("2. 칩 세트")
    print("3. 웨지 세트")
    print("4. 세트 선택 안함")
#함수 15 : 세트 메뉴 선택
def add_set() :
    global set_
    global price
    choice4 = input("세트 메뉴를 선택하세요 : ")
    choice4 = num_int(choice4)
    if choice4 == 1:
        set_ = "쿠키 세트"
        price_add = 2500
        num = order()
        price += price_add*num
        print(f"▶ {set_}를 {num}개 선택하셨습니다.")
        return price
    elif choice4 == 2:
        set_ = "칩 세트"
        price_add = 2500
        num = order()
        price += price_add*num
        print(f"▶ {set_}를 {num}개 선택하셨습니다.")
        return price
    elif choice4 == 3:
        set_ = "웨지 세트"
        price_add = 3100
        num = order()
        price += price_add*num
        print(f"▶ {set_}를 {num}개 선택하셨습니다.")
        return price
    elif choice4 == 4:
        set_ = "세트 선택 안함"
        print(f"▶ {set_}을 선택하셨습니다.")

    else :
        wrong_num()

#함수 16 : 주문 내역 확인
def print_result() :
    print("="*80)
    print(f"[🌮 주문 내역을 확인합니다 🌮]\n"
            f"◆ 메뉴 : {sandwich} \n◆ 세트 추가 : {set_}\n"
            f"◆ 가격 : {price}\n◆ 매장 이용 여부 : {here_togo}")
    print("[주문을 종료합니다!]")
    print("=" * 80) #

#주문하기
print("[🌮 서브웨이에 오신 것을 환영합니다! 🌮]")
price = 0 #가격을 누적할 변수 price
menuEnd = False
while True :
    # 매장 이용 여부 선택
    print_togo()
    choice1 = input("선택(예 : 1) : ")
    choice1 =num_int(choice1)
    #매장 이용 시
    if choice1 == 1 :
        here_togo = "매장 이용"
        print_menu1()

        #항목 선택
        choice2 = input("메뉴 선택 : ")
        choice2 = num_int(choice2)
        if choice2 == 1:
            print_classic() # 매장이용 > 클래식 항목 하위 메뉴 출력

        #샌드위치 선택
            choice3 = input("샌드위치 선택 : ")
            choice3 = num_int(choice3)
            if choice3 == 1 : #에그 마요 선택
                sandwich = egg_mayo()
                print_set() #세트메뉴 메뉴 출력
                price = add_set()
                print_result()
                break

            elif choice3 == 2 : #이탈리안 비엠티 선택
                sandwich = italian_BMT()
                print_set() #세트메뉴 메뉴 출력
                price = add_set()
                print_result()
                break
        #잘못된 숫자
            else :
                wrong_num()
        elif choice2 == 2:
        #프레시 라이트 항목 하위 메뉴 출력
            print_fresh_light()

        #프레시 라이트 샌드위치 메뉴 중 선택
            choice3 = input("샌드위치 선택 : ")
            choice3 = num_int(choice3)
            if choice3 == 1 :
                sandwich = chicken_slice()
                print_set() #세트메뉴 출력
                price = add_set()
                print_result()
                break

            elif choice3 == 2:
                sandwich = chicken_BBQ()
                print_set()  # 세트메뉴 출력
                price = add_set()
                print_result()
                break

            else :
                wrong_num()
                continue

        elif choice2 == 3:
        #프리미엄 항목 하위 메뉴 출력
            print_premium()
        # 프리미엄 샌드위치 선택
            choice3 = input("샌드위치 선택 : ")
            choice3 = num_int(choice3)
            if choice3 == 1:
                sandwich = shrimp()
            #세트메뉴 메뉴판 출력 후 선택
                print_set()
                price = add_set()
                print_result()
                break
            elif choice3 == 2:
                sandwich = pulled_pork()
            # 세트메뉴 메뉴판 출력 후 선택
                print_set()
                price = add_set()
                print_result()
                break
            else :
                wrong_num()
                continue

        else:
            wrong_num()
            continue
    elif choice1 == 2 : #방문 포장
        here_togo = "방문 포장"
        print_menu1()
        choice2 = input("메뉴 선택 : ")
        choice2 = num_int(choice2)
        #항목 선택 (클래식 / /프리미엄)
        if choice2 == 1: #방문포장 > 클래식 항목 하위 메뉴 출력
            print_classic()
            choice3 = input("샌드위치 선택 : ") #샌드위치 선택
            choice3 = num_int(choice3)
            if choice3 == 1 :
                sandwich = egg_mayo() #에그 마요 선택
                print_set()
                add_set()
                print_result()
                break

            elif choice3 == 2 : #이탈리안 BMT 선택
                sandwich = italian_BMT()
                print_set()  # 세트메뉴 출력
                price = add_set()
                print_result()
                break
            else:
                wrong_num()
                continue
        elif choice2 == 2: #방문포장 > 프레시 라이트 항목 하위 메뉴 출력
            print_fresh_light()
            choice3 = input("샌드위치 선택 : ") #샌드위치 선택
            choice3 = num_int(choice3)
            if choice3 == 1:#치킨 슬라이스 선택
                sandwich = chicken_slice()
                print_set()  # 세트메뉴 출력
                price = add_set()
                print_result()
                break
            elif choice3 == 2:#로티세리 바비큐 치킨 선택
                sandwich = chicken_BBQ()
                print_set()  # 세트메뉴 출력
                price = add_set()
                print_result()
                break
            else:
                wrong_num()
                continue

        elif choice2 == 3: #방문포장 > 프리미엄 항목 하위 메뉴 출력
            print_premium()
            choice3 = input("샌드위치 선택(예 : 1) : ") #샌드위치 선택
            choice3 = num_int(choice3)
            if choice3 == 1: #쉬림프 선택
                sandwich = shrimp()
                print_set()  # 세트메뉴 출력
                price = add_set()
                print_result()
                break

            elif choice3 == 2:#풀드 포크 바비큐 선택
                sandwich = pulled_pork()
                print_set()  # 세트메뉴 출력
                price = add_set()
                print_result()
                break

            else:
                wrong_num()
                continue
        else:
            wrong_num()
            continue
    elif choice1 ==3 :
        print("시스템을 종료합니다.")
        break
    else : #잘못된 입력
        wrong_num()
        continue


# 문제점
#2) [샌드위치] 선택(choice2, 3) 중에 잘못된 번호를 입력하면 [매장이용] 항목으로 돌아가 버림. = 미해결
#           3) 샌드위치 개수 선택을 어떻게 해야할지 모르겠음. => 해결
#4) 도중에 종료할 수 없음. -> 버튼을 하나 더 만들고 flag변수를 써서 도중에 나가기 설정
#5) 한번에 한 메뉴만 선택 가능

# 추가하고 싶은 기능.
#)  + 코드가 너무 길어진 탓에 가독성이 떨어짐. = 미해결?
# 1) 야채 / 소스 추가
#   번호 = input().split()
#   veggie = {1:"양상추", 2:"토마토", 3:"오이", 4:"피망", 5:"올리브", 6:"할라피뇨"}
# 2) 세트 메뉴 양 제한 (샌드위치 주문 숫자 이상으로 주문 불가능하게 제한..) + 세트 음료 선택
# 3) 결과에 주문 개수 추가
# 4) 음료/사이드 메뉴 추가
# 5) import time 선언 후 결과 나오는 윗줄에 time.sleep(초)
#6) 결제 시스템
