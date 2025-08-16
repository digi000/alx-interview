#!/usr/bin/python3
def pascal_triangle(n):
    return_list = [[1], [1,1]]
    if n == 1:
        del return_list[-1]
        return return_list
    elif n == 2:
        return return_list

    i = 2
    while i < n:
        m = 0
        a = 0
        b = 1
        row_list = []
        while m <= i:
            if m == 0:
                row_list.append(1)
            elif m == i:
                row_list.append(1)
            else:
                value = return_list[-1][a] + return_list[-1][b]
                a += 1
                b += 1
                row_list.append(value)
            m += 1
        return_list.append(row_list)
        i += 1
    return return_list
