import re


def judge_regex(s):
    if re.match(r'^[a-z0-9A-Z.]+@[a-z]+[.\w]+$', s):
        print('OK')
    else:
        print('failed')


# if __name__ == '__main':

judge_regex('qq.678@qq.com')