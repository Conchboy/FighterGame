def static_vars(**kwargs):
    def decorate(fun):
        for k in kwargs:
            setattr(fun, k, kwargs[k])
        return fun
    return decorate


@static_vars(f = 1)


def fun(n):
    f = 1
    fun.f *= n
    return fun.f


for i in range(10):
    print("fun(%d) = %d\n" % (i, fun(i)))


