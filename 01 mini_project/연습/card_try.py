# 카드 뒤집기 3 * 4
# 빈 리스트에

# 1) 시작
# 1-1) 난이도 선택
# 2) 불러오기
# 3) 중단하고 게임 저장.
card = "♥", "◇", "♠", "♧"
card_board = []

while True :
    print("[카드 뒤집기]")
    print("1. 시작 ")
    print("2. 불러오기 ")
    print("3. 중단 후 게임 저장. ")
    print("4. 게임 종료")
    choice = input("메뉴 선택 : ")
    if choice.isdecimal() :
        if choice == '1' :
            choice2 = input ("(1) 난이도 선택 : ")
            if choice2.isdecimal() :
                if choice2 == '1':
                    pass
                elif choice2 == '2':
                    pass
                elif choice2 == '3':
                    pass
                elif choice2 == '4':
                    pass
                else :
                    print("입력하신 난이도가 존재하지 않습니다.")
            else :
                print("잘못된 입력입니다.")

        elif choice == '2' :
            pass
        elif choice == '3' :
            pass
        elif choice == '4' :
            print("게임을 종료합니다.")
            break
        else :
            print("해당 메뉴가 존재하지 않습니다.")



