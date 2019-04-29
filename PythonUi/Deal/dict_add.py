import jieba
import sys
import re
import jieba.posseg as pseg

sys.path.append("D:\\PythonUi\\Deal")
text_sent = (
    "这是一架无敌飞机，谁都无法将其击落\n"
    "这个人是究极生物，我们无法杀死他\n"
    "这个自定义词汇被认定为是负面词汇\n"
    "这个究极无敌大风车是我最喜欢的游乐项目\n"
    "超级大飞车非常的有意思"
)


def dict_add_func(text):
    jieba.load_userdict("D:\\PythonUi\\Deal\\dict.txt")
    flag = True
    fp = open('D:\\PythonUi\\Deal\\dict.txt', "r", encoding='UTF-8')
    lines = []
    for line in fp:
        lines.append(line)
    fp.close()

    for line in lines:
        if re.match(text, line):
            flag = False
            break
        else:
            continue

    if flag is False:
        print('有重复了')
        return False
    else:
        lines.insert(-1, text+'\n')
        s = ''.join(lines)
        fp = open('D:\\PythonUi\\Deal\\dict.txt', "w", encoding='UTF-8')
        fp.write(s)
        fp.close()
        print('输入成功了')
        return True


def by_dict_division(text=""):
    jieba.load_userdict("D:\\PythonUi\\Deal\\dict.txt")
    word = jieba.cut(text)
    word = '/'.join(word)
    return word


if __name__ == '__main__':
    text = '盒马生鲜'
    dict_add_func(text)
    by_dict_division(text_sent)