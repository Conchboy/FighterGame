# Python中的静态变量定义

# class Fun:
#     f = 9
#
#
# def fun(n):
#     Fun.f = 9
#     Fun.f = Fun.f * n
#     return Fun.f
#
#
# for i in range(10):
#     print("fun(%d) = %d\n" % (i, fun(i)))
def f(a, b=[]):
    # b.append(a)
    b.append(a)
    return b


print(f(1))
print(f(2))
print(f(3))
print(f(4, ['']))
print(f(5))
