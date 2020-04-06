#!/usr/bin/env python3


def remove_adjacent(lst):
    ans = []
    for i in enumerate(lst):
        if i[0] != len(lst) - 1:
            if lst[i[0]] != lst[i[0] + 1]:
                ans.append(i[1])
        else:
            ans.append(i[1])
    return ans


def linear_merge(lst1, lst2):
    ans = []
    islst1empt = False
    islst2empt = False
    i = 0
    j = 0
    while not (islst2empt or islst1empt):
        if i < len(lst1) and lst1[i] <= lst2[j] and not islst1empt:
            ans.append(lst1[i])
            if i >= len(lst1) - 1:
                islst1empt = True
            else:
                i += 1
        elif j < len(lst2) and lst1[i] >= lst2[j] and not islst2empt:
            ans.append(lst2[j])
            if j >= len(lst2) - 1:
                islst2empt = True
            else:
                j += 1
    if islst1empt:
        for k in range(j, len(lst2)):
            ans.append(lst2[k])
    if islst2empt:
        for k in range(i, len(lst1)):
            ans.append(lst1[k])
    return ans
