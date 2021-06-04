test_num = 10


def cal_factorial(num):
    factorial = 1
    if num < 0:
        return "No factorial for negative number"
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            factorial = factorial*i
        return factorial


def count_trailing_zeros(fac_result):
    return len(str(fac))-len(str(fac).rstrip('0'))


fac = cal_factorial(test_num)
print(fac)
print(count_trailing_zeros(fac))
