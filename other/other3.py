# a = 15
# b = a
# print(b)
# a = 10
# print(b)

# l = [1,2,3] 
# m = l
# print(m)
# m[0] = 3
# print(l)

# 寻找第一个字符所在index
print("d3abcdaoijl".find('a'))

def test_1(first,*vars):
    print(first)
    for var in vars:
        print(var)

test_1("a","b","c")

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

greet_me(name="yasoob")