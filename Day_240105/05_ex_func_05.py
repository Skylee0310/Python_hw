#다양한 함수의 형태 - (3) 매개변수가 존재하지 않는 형태
#-> 함수에게 전달되는 데이터
# < 함수 생성 문법 >
# def 함수 이름( ) :
#     조건 코드와 return 값
#     실행코드
#     실행코드
#     return 결과값
#----------------------------------------------------------------
# 함수 기능 : 인사 메시지 출력 기능
# 할수 이름 : welcome
# 매개 변수 : x
# 반환값   : 없음

def welcome() :
    print("반갑습니다~ 짝!짝!짝!")

welcome()
#_----------------------------------------------------------------
# 함수 기능 : 프로그램 정보 출력 기능
# 함수 이름 : printinfo
# 매개 변수 : 없음
# 반환값 : str
#----------------------------------------------------------------
def printInfo() :
    return "MYGAME VERSION : 1.0\nDEVELOPER KK\nEMAIL:mater@game.com"
#함수 사용 즉 호출
welcome()
infoMsg= printInfo()
print(infoMsg)