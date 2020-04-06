#!/usr/bin/env python3

# UNCOMMENT THIS FILE WHEN PROBLEM IS SOLVED


def matrix_product(a_rows, b_rows):
    a_h = len(a_rows)
    b_h = len(b_rows)
    a_w = len(a_rows[0])
    b_w = len(b_rows[0])
    for k in enumerate(a_rows):
        if len(k[1]) != a_w:
            return "Data error!"
    for k in enumerate(b_rows):
        if len(k[1]) != b_w:
            return "Data error!"
    if b_h != a_w:
        return "Data error!"
    ans = []
    for j in range(a_h):
        arrofans = []
        for i in range(b_w):
            arrofans.append(0)
        ans.append(arrofans)
    for i in range(0, a_h):
        for j in range(0, b_w):
            for k in range(0, a_w):
                ans[i][j] += a_rows[i][k] * b_rows[k][j]
    return ans


def matrix_pretty_print(mat):
    mat_h = len(mat)
    mat_w = len(mat[0])
    print("\n")
    for i in range(0, mat_h):
        for j in range(0, mat_w):
            print("(", '{:^7}'.format(mat[i][j]), ")", end='')
        print("\n")
