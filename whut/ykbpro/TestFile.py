import os.path
import json

print(os.path.abspath('.'))
print(__name__)


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def readfile(self):
        with open(os.path.abspath('.') + '\\test_py.txt', 'w', encoding='utf-8') as f:
            # print(f.read())
            f.write('克里斯蒂亚诺')

    def __str__(self):
        return '学生姓名是{0},年龄为{1}'.format(self.name, self.age)


def stu2dict(s):
    return {'name': s.name, 'age': s.age}


def dict2stu(dict):
    return Student(dict['name'], dict['age'])

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。


def get_file_paths_by_key(path, key):
    for x in os.listdir(path):
        x_path = os.path.join(path, x)
        if os.path.isfile(x_path):
            if key in os.path.split(x_path)[1]:
                print(os.path.relpath(x_path))
            elif os.path.isdir(x_path):
                get_file_paths_by_key(x_path, key)


get_file_paths_by_key('.', '.py')


s = Student('CR7', 20)
json_str = json.dumps(s, default=stu2dict)  # 序列化为dict
print(json.loads(json_str, object_hook=dict2stu))  # 反序列化为Student对象

# print(s.stu2dict())