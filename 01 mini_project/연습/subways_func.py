'''
서브웨이 키오스크 주문하기(약식)
1) 매장 이용/ 방문 포장
(1) 매장 이용
(2) 방문 포장
(3) 주문 종료


2) 메뉴 선택 + 개수 선택
    2-1) 샌드위치 메뉴 (메뉴 출력)
        2-1-1) 클래식 : 에그마요, 이탈리안비엠티, 햄, 참치,
        2-1-2) 프레시 라이트 : 치킨슬라이스, 치킨베이컨아보카도, 로티세리바비큐치킨, 써브웨이클럽
        2-1-3) 프리미엄 : 스파이시 쉬림프, 쉬림프, 풀드 포크 바비큐, 스테이크&치즈, 치킨 데리야끼
    2-2) 개수 선택

3) 세트 메뉴 추가 선택

4) 주문 내역 출력
'''
def wrong_num() :
    print("잘못된 번호를 입력하셨습니다.")

#주문하기
print("[서브웨이에 오신 것을 환영합니다!]")
price = 0
while True :
    print("1. 매장 이용")
    print("2. 방문 포장")
    print("3. 주문 종료")
    choice1 = input("선택(예 : 1) : ")

    if choice1.isdecimal() :
        if choice1 == '1' : #매장 이용
            here_togo = "매장 이용"
            print("1. 클래식 (에그마요, 이탈리안비엠티)")
            print("2. 프레시 라이트 (치킨슬라이스, 로티세리바비큐치킨)")
            print("3. 프리미엄 (쉬림프, 풀드 포크 바비큐)")
            choice2 = input("메뉴 선택 : ")
            if choice2.isdecimal():
                #항목 선택
                if choice2 == '1': #클래식 항목 하위 메뉴 출력
                    print("[클래식]")
                    print("1. 에그마요")
                    print("2. 이탈리안 비엠티")
                    choice3 = input("샌드위치 선택 : ") #샌드위치 선택
                    if choice3.isdecimal():
                        if choice3 == '1' :
                            sandwich = "에그마요"
                            price = 5500
                            print(f"▶ {sandwich}을/를 선택하셨습니다.")
                            
                        elif choice3 == '2' :
                            sandwich = "이탈리안 비엠티"
                            price = 6900
                            print(f"▶ {sandwich}을/를 선택하셨습니다.")

                        else :
                            wrong_num()
                elif choice2 == '2':
                    #프레시 라이트 항목 하위 메뉴 출력
                    print("[프레시 라이트]")
                    print("1. 치킨 슬라이스")
                    print("2. 로티세리 바비큐 치킨")
                    #프레시 라이트 샌드위치 선택
                    choice3 = input("샌드위치 선택 : ")
                    if choice3.isdecimal():
                        if choice3 == '1' :
                            sandwich = "치킨 슬라이스"
                            price = 6500
                            print(f"▶ {sandwich}을/를 선택하셨습니다.")

                        elif choice3 == '2':
                            sandwich = "로티세리 바비큐 치킨"
                            price = 7300
                            print(f"▶ {sandwich}을/를 선택하셨습니다.")

                        else :
                            wrong_num()
                            continue

                elif choice2 == '3':
                    #프리미엄 항목 하위 메뉴 출력
                    print("[프리미엄]")
                    print("1. 쉬림프")
                    print("2. 풀드 포크 바비큐")
                    # 프리미엄 샌드위치 선택
                    choice3 = input("샌드위치 선택 : ")
                    if choice3.isdecimal(): #
                        if choice3 == '1' :
                            sandwich = "쉬림프"
                            price = 7100
                            print(f"▶ {sandwich}을/를 선택하셨습니다.")
                        elif choice3 == '2':
                            sandwich = "풀드 포크 바비큐"
                            price = 7200
                            print(f"▶ {sandwich}을/를 선택하셨습니다.")
                        else :
                            wrong_num()
                            continue

            else:
                print("▶ 잘못된 번호입니다. 다시 입력해 주십시오.")
                continue
        elif choice1 == '2': #방문 포장
            here_togo = "방문 포장"
            print("1. 클래식 (에그마요, 이탈리안비엠티)")
            print("2. 프레시 라이트 (치킨슬라이스,로티세리바비큐치킨)")
            print("3. 프리미엄 (쉬림프, 풀드 포크 바비큐)")
            choice2 = input("메뉴 선택 : ")
            if choice2.isdecimal():
                #항목 선택
                if choice2 == '1': #클래식 항목 하위 메뉴 출력
                    print("[클래식]")
                    print("1. 에그마요")
                    print("2. 이탈리안 비엠티")
                    choice3 = input("샌드위치 선택 : ") #샌드위치 선택
                    if choice3 == '1':
                        sandwich = "에그마요"
                        price = 5500
                        print(f"▶ {sandwich}을/를 선택하셨습니다.")

                    elif choice3 == '2':
                        sandwich = "이탈리안 비엠티"
                        price = 6900
                        print(f"▶ {sandwich}을/를 선택하셨습니다.")

                    else:
                        print("▶ 잘못된 메뉴를 선택하셨습니다.")
                        continue
                elif choice2 == '2': #프레시 라이트 항목 하위 메뉴 출력
                    print("[프레시 라이트]")
                    print("1. 치킨 슬라이스")
                    print("2. 로티세리 바비큐 치킨")
                    choice3 = input("샌드위치 선택 : ") #샌드위치 선택
                    if choice3 == '1':
                        sandwich = "치킨 슬라이스"
                        price = 6500
                        print(f"▶ {sandwich}을/를 선택하셨습니다.")

                    elif choice3 == '2':
                        sandwich = "로티세리 바비큐 치킨"
                        price = 7300
                        print(f"▶ {sandwich}을/를 선택하셨습니다.")

                    else:
                        wrong_num()
                        continue

                elif choice2 == '3': #프리미엄 항목 하위 메뉴 출력
                    print("[프리미엄]")
                    print("1. 쉬림프")
                    print("2. 풀드 포크 바비큐")
                    choice3 = input("샌드위치 선택 : ") #샌드위치 선택
                    if choice3 == '1':
                        sandwich = "쉬림프"
                        price = 7100
                        print(f"▶ {sandwich}을/를 선택하셨습니다.")

                    elif choice3 == '2':
                        sandwich = "풀드 포크 바비큐"
                        price = 7200
                        print(f"▶ {sandwich}을/를 선택하셨습니다.")

                    else:
                        wrong_num()
                        continue
            else:
                wrong_num()
                continue

        else : #잘못된 입력
            wrong_num()
            continue
    else : #잘못된 입력
        wrong_num()
        continue
    
    #세트 메뉴 주문
    print("[세트 메뉴]")
    print("1. 쿠키 세트")
    print("2. 칩 세트")
    print("3. 웨지 세트")
    print("4. 세트 선택 안함")
    choice4 = input("세트 메뉴를 선택하세요 : ")
    if choice4.isdecimal() :
        if choice4 == '1':
            set_ = "쿠키 세트"
            price += 2500
            print(f"▶ {set_}를 선택하셨습니다.")
            break
        elif choice4 == '2':
            set_ = "칩 세트"
            price += 2500
            print(f"▶ {set_}를 선택하셨습니다.")
            break
        elif choice4 == '3':
            set_ = "웨지 세트"
            price += 3100
            print(f"▶ {set_}를 선택하셨습니다.")
            break
        elif choice4 == '4':
            set_ = "세트 선택 안함"
            print(f"▶ 세트를 선택하지 않으셨습니다.")
            break

        else :
            wrong_num()
            continue

print("="*80)
print(f"주문 내역을 확인합니다.\n"
        f"◆ 메뉴 : {sandwich}\n◆ 세트 추가 : {set_}\n"
        f"◆ 가격 : {price}\n◆ 매장 이용 여부 : {here_togo}")
print("주문을 종료합니다.")
print("=" * 80)