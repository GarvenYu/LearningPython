# 测试__getattr__


class Chain(object):
    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, item):
        print(Chain('%s/%s' % (self.__path, item)))

    def __str__(self):
        print(self.__path)


class User(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name


Chain().status