# 用于正则匹配
import re


def re_text(text=''):
    result = ''

    s = text.encode()

    temp = s.decode('utf-8')

    # 中文正则表达式
    pattern = "[\u4e00-\u9fa5]+\W*"

    # 生成正则对象 
    regex = re.compile(pattern)

    # 匹配
    lists = regex.findall(temp)

    for list in lists:
        result += list

    if result != '':
        return result
    else:
        return


if __name__ == '__main__':
    print(re_text("asdfasfasf"))
