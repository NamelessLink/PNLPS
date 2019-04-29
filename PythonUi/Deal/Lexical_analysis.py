from aip import AipNlp

APP_ID = '16075105'
API_KEY = 'a6buAu53EH23iuOkjlL53aZQ'
SECRET_KEY = '3btBkBGWqyj95KmaYImiPn8qMhav9svh'
Client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def lexer(text = ""):
    word_list = []
    str1 = ""
    temp_result = Client.lexer(text)
    for item in temp_result['items']:
        for word in item['basic_words']:
            word_list.append(word)
            str1 += word + "/"

    lexer_dict = {
        'text': temp_result['text'],
        'lexer': str1,
        'word_list' : word_list
    }
    return lexer_dict


def dict_lexer(text):
    return


if __name__ == '__main__':
    f = open("../1.txt", "r")
    s = f.read()
    lexer(s)