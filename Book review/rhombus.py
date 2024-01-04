'''
마름모 출력
1) 왼쪽 공백 + '*' * i(홀수로 증가)
2) '*'*num
3) 왼쪽공백(1...n) + '*'*i(점점 줄어듦)
'''


'''
1줄 : 1 (i)
2줄 : 3 (i+i)
3줄 : 5 (i = num)
4줄 : 3 (num-1)
5줄 : 1 (num-i)

'''

num = 11
#num = int(input("정수 입력 : "))
for i in range(1, num+1) :
    num2 = num//2+1
    if i < num2 :
        print(' '*(num2-i)+'*'*i+'*'*(i-1)+' '*(num2-i))
    elif i == num2 :
        print("*"*num)
    elif i>num2 :
        print(' '*(i-num2) +"*"*((-2)*(i-num2)+num) +" "*(i-num2))

