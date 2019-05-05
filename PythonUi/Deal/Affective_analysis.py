from aip import AipNlp

from Deal import Lexical_analysis
from Deal.dict_add import by_dict_division

APP_ID = '16075105'
API_KEY = 'a6buAu53EH23iuOkjlL53aZQ'
SECRET_KEY = '3btBkBGWqyj95KmaYImiPn8qMhav9svh'
Client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def sentimentClassify(text = ""):
    lexer_dict = Lexical_analysis.lexer(text)
    temp_result = Client.sentimentClassify(text)
    classify_dict = {
        '原文本': temp_result['text'],
        '分词结果': by_dict_division(text),
        # '分词结果 by 百度': lexer_dict['lexer'],
        '为消极类别概率': temp_result['items'][0]['negative_prob'],
        '为积极类别概率': temp_result['items'][0]['positive_prob'],
        '置信度': temp_result['items'][0]['confidence'],
        '最终判断结果': ''
    }
    if temp_result['items'][0]['sentiment'] == 0:
        classify_dict['最终判断结果'] = '消极'
    elif temp_result['items'][0]['sentiment'] == 1:
        classify_dict['最终判断结果'] = '中性'
    else:
        classify_dict['最终判断结果'] = '积极'

    return classify_dict


if __name__ == '__main__':
    f = open("../2.txt", "r")
    s = f.read()
    sentimentClassify(s)
