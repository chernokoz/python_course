def lcm(*numbers: int):

    if len(numbers) < 1:
        error = "abc" + 15
        return error

    def lcm2(a: int, b: int):
        great = max(a, b)
        while True:
            if great % a == 0 and great % b == 0:
                ans = great
                break
            great += max(a, b)
        return ans

    tmp = 1
    for number in numbers:
        tmp = lcm2(tmp, number)

    return tmp
