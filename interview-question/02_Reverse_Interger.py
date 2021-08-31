num = -123


def rev_int(num):
    name = str(num)
    if name[0] == "-":
        num = int("-" + name[:0:-1])
    else:
        num = int(name[::-1])

    if -2**31 <= num <= (2**31 - 1):
        return num
    else:
        return 0


print(rev_int(num))
