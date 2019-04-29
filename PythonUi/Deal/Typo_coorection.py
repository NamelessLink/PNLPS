from aip import AipNlp

from Deal import Lexical_analysis
from Deal.dict_add import by_dict_division

APP_ID = '16075105'
API_KEY = 'a6buAu53EH23iuOkjlL53aZQ'
SECRET_KEY = '3btBkBGWqyj95KmaYImiPn8qMhav9svh'
Client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def encet(text = ""):
    wrong_list = []
    right_list = []
    lexer_dict = Lexical_analysis.lexer(text)
    temp_result = Client.ecnet(text)
    for word in temp_result['item']['vec_fragment']:
        # print(word['ori_frag'] + '\t' + word['correct_frag'])
        wrong_list.append(word['ori_frag'])
        right_list.append(word['correct_frag'])
    encet_dict = {
        '原文本': text,
        '分词结果': by_dict_division(text),
        '分词结果 by 百度': lexer_dict['lexer'],
        '错词': wrong_list,
        '错词纠正': right_list,
        '准确率': temp_result['item']['score'],
        '替换后文本': temp_result['item']['correct_query']
    }

    return encet_dict


if __name__ == '__main__':
    f = open("../1.txt", "r")
    s = f.read()
    encet(s)
