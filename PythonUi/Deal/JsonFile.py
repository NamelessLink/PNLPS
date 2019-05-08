import datetime
import json


def jsonfile_save(dict={}, file_path=''):
    with open(file_path, "r") as json_file:
        load_dict = json.load(json_file)
        time_stamp = datetime.datetime.now().strftime('%y.%m.%d-%H:%M:%S:%f')
        load_dict[time_stamp] = dict

    with open(file_path, "w") as json_file:
        json.dump(load_dict, json_file, indent=4, separators=(',', ':'), ensure_ascii=False)
        json_file.close()


def jsonfile_load(file_path=''):
    with open(file_path, "r") as json_file:
        load_dict = json.load(json_file)
    return load_dict

if __name__ == '__main__':
    dict_ = {
                '原文本': '我不喜欢这个电影，太令人沮丧了！',
                '分词结果': '我/不/喜欢/这个/电影/，/太/令人/沮丧/了/！/',
                '为消极类别概率': 0.847257,
                '为积极类别概率': 0.152743,
                '置信度': 0.660571,
                '最终判断结果': '消极'
             }

    path = '../Affective_analysis.json'

    jsonfile_save(dict_, path)
