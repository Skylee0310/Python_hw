msg = input("데이터 입력 : ").split()
def num_save(*args) :
    alist = []
    for i in args :
        if i.isdigit() :
            alist.append(i)
    return sum(alist), max(alist), min(alist)
numlist, max_num, min_num = num_save(msg)