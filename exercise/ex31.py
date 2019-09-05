# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母


def fx31(*letter):
    list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if letter[0] == 'M':
        print(list[0])
    if letter[0] == 'T':
        if letter[1] == 'u':
            print(list[1])
        if letter[1] == 'h':
            print(list[3])
    if letter[0] == 'W':
        print(list[2])
    if letter[0] == 'F':
        print(list[4])
    if letter[0] == 'S':
        if letter[1] == 'a':
            print(list[5])
        if letter[1] == 'u':
            print(list[6])


fx31('T', 'u')
