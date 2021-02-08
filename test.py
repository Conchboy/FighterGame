def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


@static_vars(f = 1)


def fun(n):
    fun.f *= n
    return fun.f


for i in range(10):
    print("fun(%d) = %d\n" % (i, fun(i)))


