# 测试装饰器模式
import functools


def log(param):
    if callable(param):
        @functools.wraps(param)
        def wrapper(*args, **kwargs):
            for i in args:
                print(i)
            # param(*args, **kwargs)
            print('bye')
            return param(3, 4)
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print('param is {0} and func is {1}'.format(param, func))
                return func(args, kwargs)
            return wrapper
        return decorator


@log
def now(*args, **kwargs):
    print('%s %s' % (args[0], args[1]))


now(1, 2)
