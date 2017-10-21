import hashlib


d = {}


def input_account_pass():
    account = input('请输入账号')
    password = input('请输入密码')
    md5 = hashlib.md5()
    md5.update((password + 'the_salt').encode('utf-8'))
    d[account] = md5.hexdigest()
    print(d[account])


def check_pass():
    account = input('请输入账号')
    password = input('请输入密码')
    md5 = hashlib.md5()
    md5.update((password + 'the_salt').encode('utf-8'))
    if d[account] == md5.hexdigest():
        print('success')
    else:
        print('failed')


input_account_pass()
check_pass()
