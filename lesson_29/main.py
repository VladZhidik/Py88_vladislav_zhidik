def first_task(arr: list[int]) -> int:
    return sum([i for i in arr if i > 0])


'print(first_task([2,3,-5,-8]))'


def second_task(x):
    return -x


'print(second_task(5))'


def third_task(x):
    return -x


def fourth_task_1(istr, n):
    if n % 1 == 0:
        return istr * n
    return 0


'print(fourth_task_1(tuc , 5))'


def fourth_task_2(istr, n):
    if isinstance(n, int):
        return istr * n
    return 0


'print(fourth_task_2(tuc , 3))'


def fifth_task(istr, n):
