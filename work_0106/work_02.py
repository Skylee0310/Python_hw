msg = input("데이터 입력 : ").split()
print(msg)
def num_save(args) :
    alist = []
    for i in args :
        if i.isnumeric() :
            i = int(i)
            alist.append(i)
    return sum(alist), max(alist), min(alist)
result, max_num, min_num = num_save(msg)
print(f'합계 : {result}, 최댓값 : {max_num}, 최솟값 : {min_num}')