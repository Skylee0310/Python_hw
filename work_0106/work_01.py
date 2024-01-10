#1. 문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을 출력하는 함수를 구현하세요.
# msg = input("문자열 리스트 입력(공백으로 분리) : ").split()
# print(type(msg))
# msg.sort()
# print(f"정렬 결과 : [{msg}]\n가장 높은 문자열 : {max(msg)}, 가장 낮은 문자열 :{min(msg)}")

msg = input("문자열 입력 : ").split()
def msg_check(args) :
     args.sort()
     return msg, max(msg), min(msg)

result, max_msg, min_msg = msg_check(msg)
print(f"정렬 결과 : {result}\n가장 높은 문자열 : {max_msg}, 가장 낮은 문자열 :{min_msg}")
