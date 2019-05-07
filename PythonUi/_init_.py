import json
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidgetItem

from Deal import Typo_coorection
from Deal import Affective_analysis
from Deal.JsonFile import jsonfile_save, jsonfile_load
from Deal.input_alt import str_alt
from Deal.re_text import re_text
from Deal.dict_add import dict_add_func, dict_key_list
from Ui.Exit import Ui_Exit
from Ui.History import Ui_History
from Ui.HistoryDetail import Ui_HistoryDetail

from Ui.MainWindow import *
from Ui.Add_dict_Frame import *
from Ui.Result import *
from Ui.Tips import *
from Ui.Typo_coorection_Frame import *
from Ui.Affective_analysis_Frame import *


class Open_MainWindow(QMainWindow, Ui_MainWindow):
    list = []
    dict = {}

    def __init__(self, parent=None):
        super(Open_MainWindow, self).__init__(parent)
        self.setupUi(self)

    @staticmethod
    def slot_pushButton_Func():
        Affective_analysis_Frame.show()
        MainWindow.close()

    @staticmethod
    def slot_pushButton_2_Func():
        Typo_coorection_Frame.show()
        MainWindow.close()

    @staticmethod
    def slot_pushButton_3_Func():
        Add_dict_Frame.show()
        MainWindow.close()

    def slot_pushButton_4_Func(self):
        i = 0
        lenth = 7
        self.dict = jsonfile_load('./Affective_analysis.json')
        self.list = dict_key_list(self.dict)
        if len(self.list) <= lenth:
            lenth = len(self.list) - 1
        while i <= lenth:
            t = -(i + 1)
            newItem = QTableWidgetItem(self.list[t])
            newItem2 = QTableWidgetItem(self.dict[self.list[t]]['原文本'])
            History.tableWidget.setItem(i, 0, newItem)
            History.tableWidget.setItem(i, 1, newItem2)
            i += 1
        History.show()

    def slot_pushButton_5_Func(self):
        i = 0
        lenth = 7
        self.dict = jsonfile_load('./Typo_coorection.json')
        self.list = dict_key_list(self.dict)
        if len(self.list) <= lenth:
            lenth = len(self.list) - 1
        while i <= lenth:
            t = -(i + 1)
            newItem = QTableWidgetItem(self.list[t])
            newItem2 = QTableWidgetItem(self.dict[self.list[t]]['原文本'])
            History.tableWidget.setItem(i, 0, newItem)
            History.tableWidget.setItem(i, 1, newItem2)
            i += 1
        History.show()

    @staticmethod
    def slot_closeButton_Func():
        Exit.show()


class Open_Add_dict_Frame(QMainWindow, Ui_Add_dict_Frame):
    result = ""

    def __init__(self, parent=None):
        super(Open_Add_dict_Frame, self).__init__(parent)
        self.setupUi(self)

    # 确定按钮
    def slot_pushButton_2_Func(self):
        self.result = self.get_text()
        if self.result is None:
            Tips.label.setText("请正确输入一个词组")
            Tips.show()
        else:
            if dict_add_func(self.result) is True:
                Tips.label.setText("词组入库成功")
                Tips.show()
                self.textEdit.clear()
            else:
                Tips.label.setText("词典中存在该词")
                Tips.show()
                self.textEdit.clear()

    # 取消按钮
    def slot_pushButton_Func(self):
        self.textEdit.clear()
        self.close()
        MainWindow.show()

    # 文本获取
    def get_text(self):
        if self.textEdit.toPlainText() != '':
            Text = re_text(self.textEdit.toPlainText())
            return Text
        else:
            return

    # 关闭按钮
    @staticmethod
    def slot_closeButton_Func():
        Exit.show()


class Open_Affective_analysis_Frame(QMainWindow, Ui_Affective_analysis_Frame):
    # 变量
    result = ''

    path = 'Affective_analysis.json'

    def __init__(self, parent=None):
        super(Open_Affective_analysis_Frame, self).__init__(parent)
        self.setupUi(self)

    # 取消按钮
    def slot_pushButton_Func(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.close()
        MainWindow.show()

    # 选择文件按钮
    def slot_pushButton_2_Func(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, "选取文件", self.cwd,  # 起始路径
                                                                "Text Files (*.txt)")  # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\n取消选择")
            return

        self.textEdit_2.setPlainText(fileName_choose)

    # 确定按钮
    def slot_pushButton_3_Func(self):
        self.result = self.get_text()
        if self.result is None:
            Tips.label.setText("输入为空或输入非中文字符")
            Tips.show()
        elif self.result == "FileNotFound":
            Tips.label.setText("无法找到文件")
            Tips.show()
            self.textEdit_2.clear()
        elif self.result == "FileNotTxt":
            Tips.label.setText("传入文件非 T X T 格式")
            Tips.show()
            self.textEdit_2.clear()
        else:
            self.text_deal()
            self.textEdit.clear()
            self.textEdit_2.clear()
            self.close()

    # 获取文本
    def get_text(self):
        if self.textEdit.toPlainText() != '':
            Text = re_text(self.textEdit.toPlainText())
            return Text
        if self.textEdit_2.toPlainText() != '':
            Path = self.textEdit_2.toPlainText()
            try:
                TemPath = os.path.splitext(Path)
                filename, filetype = TemPath
                if filetype == '.txt':
                    file = open(Path)
                else:
                    return "FileNotTxt"
            except FileNotFoundError as e:
                print("错误:", e)
                return "FileNotFound"
            else:
                Text = re_text(file.read())
                file.close()
                return Text
        return

    # 进行文本处理
    def text_deal(self):
        result_dict = Affective_analysis.sentimentClassify(self.result)
        str1 = json.dumps(result_dict, indent=4, separators=(',', ':'), ensure_ascii=False)
        str2 = str_alt(str1)
        jsonfile_save(result_dict, self.path)
        Result.textEdit.setPlainText(str2)
        Result.show()

    # 关闭按钮
    @staticmethod
    def slot_closeButton_Func():
        Exit.show()


class Open_Typo_coorection_Frame(QMainWindow, Ui_Typo_coorection_Frame):
    # 变量
    result = ''

    path = 'Typo_coorection.json'

    def __init__(self, parent=None):
        super(Open_Typo_coorection_Frame, self).__init__(parent)
        self.setupUi(self)

    # 确定按钮
    def slot_pushButton_3_Func(self):
        self.result = self.get_text()
        if self.result is None:
            Tips.label.setText("输入为空或输入非中文字符")
            Tips.show()
        elif self.result == "FileNotFound":
            Tips.label.setText("无法找到文件")
            Tips.show()
            self.textEdit_2.clear()
        elif self.result == "FileNotTxt":
            Tips.label.setText("传入文件非 T X T 格式")
            Tips.show()
            self.textEdit_2.clear()
        else:
            self.text_deal()
            self.textEdit.clear()
            self.textEdit_2.clear()
            self.close()

    # 取消按钮
    def slot_pushButton_Func(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.close()
        MainWindow.show()

    #  选择文件
    def slot_pushButton_2_Func(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, "选取文件", self.cwd,  # 起始路径
                                                                "Text Files (*.txt);;All Files(*)")  # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\n取消选择")
            return

        self.textEdit_2.setPlainText(fileName_choose)

    #  获取文本
    def get_text(self):
        if self.textEdit.toPlainText() != '':
            Text = re_text(self.textEdit.toPlainText())
            return Text
        if self.textEdit_2.toPlainText() != '':
            Path = self.textEdit_2.toPlainText()
            try:
                TemPath = os.path.splitext(Path)
                filename, filetype = TemPath
                if filetype == '.txt':
                    file = open(Path)
                else:
                    return "FileNotTxt"
            except FileNotFoundError as e:
                print("错误:", e)
                return "FileNotFound"
            else:
                Text = re_text(file.read())
                file.close()
                return Text
        return

    # 文本处理
    def text_deal(self):
        result_dict = Typo_coorection.encet(self.result)
        str1 = json.dumps(result_dict, indent=4, separators=(',', ':'), ensure_ascii=False)
        str2 = str_alt(str1)
        jsonfile_save(result_dict, self.path)
        if result_dict['准确率'] == 0:
            str1 = '该文本认定无错别字\n原文本：' + result_dict['原文本'] + '\n分词结果：' + result_dict['分词结果']
            # print(str1)
            Result.textEdit.setPlainText(str1)
            Result.show()
        else:
            Result.textEdit.setPlainText(str2)
            Result.show()

    # 关闭按钮
    @staticmethod
    def slot_closeButton_Func():
        Exit.show()


class Open_History_Frame(QMainWindow, Ui_History):
    def __init__(self, parent=None):
        super(Open_History_Frame, self).__init__(parent)
        self.setupUi(self)

    def slot_Item_Func(self, item=QtWidgets.QTableWidgetItem()):
        key = self.tableWidget.item(item.row(), 0).text()
        str1 = MainWindow.dict[key]
        str2 = json.dumps(str1, indent=4, separators=(',', ':'), ensure_ascii=False)
        str2 = str_alt(str2)
        History_Detail.textEdit.setPlainText(str2)
        History_Detail.show()

    @staticmethod
    def slot_closeButton_Func():
        History.tableWidget.clear()
        newItem = QTableWidgetItem("时间")
        newItem2 = QTableWidgetItem("文本")
        History.tableWidget.setHorizontalHeaderItem(0, newItem)
        History.tableWidget.setHorizontalHeaderItem(1, newItem2)
        History.close()


class Open_History_Detail_Frame(QDialog, Ui_HistoryDetail):
    def __init__(self, parent=None):
        super(Open_History_Detail_Frame, self).__init__(parent)
        self.setupUi(self)

    @staticmethod
    def slot_closeButton_Func():
        History_Detail.textEdit.clear()
        History_Detail.close()


class Open_Result(QMainWindow, Ui_Result):
    def __init__(self, parent=None):
        super(Open_Result, self).__init__(parent)
        self.setupUi(self)

    # 退出按钮
    @staticmethod
    def slot_pushButton_Func():
        Exit.show()

    # 主界面按钮
    @staticmethod
    def slot_pushButton_2_Func():
        Result.close()
        MainWindow.show()


class Open_Exit(QDialog, Ui_Exit):
    def __init__(self, parent=None):
        super(Open_Exit, self).__init__(parent)
        self.setupUi(self)

    # 是按钮
    @staticmethod
    def slot_pushButton_Func():
        sys.exit(app.exec_())

    # 否按钮
    @staticmethod
    def slot_pushButton_2_Func():
        Exit.close()


class Open_Tips(QMainWindow, Ui_Tips):
    def __init__(self, parent=None):
        super(Open_Tips, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 实例化
    MainWindow = Open_MainWindow()
    Add_dict_Frame = Open_Add_dict_Frame()
    Affective_analysis_Frame = Open_Affective_analysis_Frame()
    Typo_coorection_Frame = Open_Typo_coorection_Frame()
    Result = Open_Result()
    History = Open_History_Frame()
    History_Detail = Open_History_Detail_Frame()
    Tips = Open_Tips()
    Exit = Open_Exit()

    # MainWindow按钮绑定
    MainWindow.pushButton.clicked.connect(MainWindow.slot_pushButton_Func)
    MainWindow.pushButton_2.clicked.connect(MainWindow.slot_pushButton_2_Func)
    MainWindow.pushButton_3.clicked.connect(MainWindow.slot_pushButton_3_Func)
    MainWindow.pushButton_4.clicked.connect(MainWindow.slot_pushButton_4_Func)
    MainWindow.pushButton_5.clicked.connect(MainWindow.slot_pushButton_5_Func)
    MainWindow.Close_Button.clicked.connect(MainWindow.slot_closeButton_Func)

    # Add_dict_Frame按钮绑定
    Add_dict_Frame.pushButton.clicked.connect(Add_dict_Frame.slot_pushButton_Func)
    Add_dict_Frame.pushButton_2.clicked.connect(Add_dict_Frame.slot_pushButton_2_Func)
    Add_dict_Frame.Close_Button.clicked.connect(Add_dict_Frame.slot_closeButton_Func)

    # Affective_analysis_Frame按钮绑定
    Affective_analysis_Frame.pushButton.clicked.connect(Affective_analysis_Frame.slot_pushButton_Func)
    Affective_analysis_Frame.pushButton_2.clicked.connect(Affective_analysis_Frame.slot_pushButton_2_Func)
    Affective_analysis_Frame.pushButton_3.clicked.connect(Affective_analysis_Frame.slot_pushButton_3_Func)
    Affective_analysis_Frame.Close_Button.clicked.connect(Affective_analysis_Frame.slot_closeButton_Func)

    # Typo_coorection_Frame按钮绑定
    Typo_coorection_Frame.pushButton.clicked.connect(Typo_coorection_Frame.slot_pushButton_Func)
    Typo_coorection_Frame.pushButton_2.clicked.connect(Typo_coorection_Frame.slot_pushButton_2_Func)
    Typo_coorection_Frame.pushButton_3.clicked.connect(Typo_coorection_Frame.slot_pushButton_3_Func)
    Typo_coorection_Frame.Close_Button.clicked.connect(Typo_coorection_Frame.slot_closeButton_Func)

    # History事件绑定
    History.tableWidget.itemDoubleClicked.connect(History.slot_Item_Func)
    History.closeButton.clicked.connect(History.slot_closeButton_Func)

    # History_Detail按钮绑定
    History_Detail.closeButton.clicked.connect(History_Detail.slot_closeButton_Func)

    # Tips按钮绑定
    Tips.pushButton.clicked.connect(Tips.close)

    # Result按钮绑定
    Result.pushButton.clicked.connect(Result.slot_pushButton_Func)
    Result.pushButton_2.clicked.connect(Result.slot_pushButton_2_Func)

    # Exit 按钮绑定
    Exit.pushButton.clicked.connect(Exit.slot_pushButton_Func)
    Exit.pushButton_2.clicked.connect(Exit.slot_pushButton_2_Func)

    MainWindow.show()
    sys.exit(app.exec_())
