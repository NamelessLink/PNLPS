import json
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from Deal import Typo_coorection, JsonFile
from Deal import Affective_analysis
from Deal.input_alt import str_alt
from Deal.re_text import re_text

from Ui.MainWindow import *
from Ui.Add_dict_Frame import *
from Ui.Result import *
from Ui.Tips import *
from Ui.Typo_coorection_Frame import *
from Ui.Affective_analysis_Frame import *


class Open_MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Open_MainWindow, self).__init__(parent)
        self.setupUi(self)

    def slot_pushButton_Func(self):
        Affective_analysis_Frame.show()
        MainWindow.close()

    def slot_pushButton_2_Func(self):
        Typo_coorection_Frame.show()
        MainWindow.close()

    def slot_pushButton_3_Func(self):
        Add_dict_Frame.show()
        MainWindow.close()

    def slot_closeButton_Func(self):
        sys.exit(app.exec_())


class Open_Add_dict_Frame(QMainWindow, Ui_Add_dict_Frame):
    result = ""

    def __init__(self, parent=None):
        super(Open_Add_dict_Frame, self).__init__(parent)
        self.setupUi(self)

    # 确定按钮
    def slot_pushButton_2_Func(self):
        self.result = self.get_text()
        if self.result is None:
            Tips.label.setText("请输入一个词组")
            Tips.show()
        else:
            Result.show()
            self.textEdit.clear()
            self.close()

    # 取消按钮
    def slot_pushButton_Func(self):
        self.textEdit.clear()
        self.close()
        MainWindow.show()

    # 文本获取
    def get_text(self):
        if self.textEdit.toPlainText() != '':
            Text = re_text(self.textEdit.toPlainText())
            print(Text)
            return Text
        else:
            return

    # 关闭按钮
    def slot_closeButton_Func(self):
        sys.exit(app.exec_())


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
                file = open(Path, "r")
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
        JsonFile.jsonfile_save(result_dict, self.path)
        Result.textEdit.setPlainText(str2)
        Result.show()

    # 关闭按钮
    def slot_closeButton_Func(self):
        sys.exit(app.exec_())


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
                file = open(Path, "r")
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
        JsonFile.jsonfile_save(result_dict, self.path)
        if result_dict['准确率'] == 0:
            str1 = '该文本认定无错别字\n原文本：' + result_dict['原文本'] + '\n分词结果：' + result_dict['分词结果']
            print(str1)
            Result.textEdit.setPlainText(str1)
            Result.show()
        else:
            Result.textEdit.setPlainText(str2)
            Result.show()

    # 关闭按钮
    def slot_closeButton_Func(self):
        sys.exit(app.exec_())


class Open_Result(QMainWindow, Ui_Result):
    def __init__(self, parent=None):
        super(Open_Result, self).__init__(parent)
        self.setupUi(self)

    # 退出按钮
    def slot_pushButton_Func(self):
        sys.exit(app.exec_())

    # 主界面按钮
    def slot_pushButton_2_Func(self):
        Result.close()
        MainWindow.show()


class Open_Tips(QMainWindow, Ui_Tips):
    def __init__(self, parent=None):
        super(Open_Tips, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWindow = Open_MainWindow()
    Add_dict_Frame = Open_Add_dict_Frame()
    Affective_analysis_Frame = Open_Affective_analysis_Frame()
    Typo_coorection_Frame = Open_Typo_coorection_Frame()
    Result = Open_Result()
    # File_Select = Open_File_Select()
    Tips = Open_Tips()

    # MainWindow按钮绑定
    MainWindow.pushButton.clicked.connect(MainWindow.slot_pushButton_Func)
    MainWindow.pushButton_2.clicked.connect(MainWindow.slot_pushButton_2_Func)
    MainWindow.pushButton_3.clicked.connect(MainWindow.slot_pushButton_3_Func)
    MainWindow.Close_Button.clicked.connect(MainWindow.slot_closeButton_Func)

    # Add_dict_Frame按钮绑定
    Add_dict_Frame.pushButton.clicked.connect(Add_dict_Frame.slot_pushButton_Func)
    Add_dict_Frame.pushButton_2.clicked.connect(Add_dict_Frame.slot_pushButton_2_Func)

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

    # Tips按钮绑定
    Tips.pushButton.clicked.connect(Tips.close)

    # Result按钮绑定
    Result.pushButton.clicked.connect(Result.slot_pushButton_Func)
    Result.pushButton_2.clicked.connect(Result.slot_pushButton_2_Func)

    MainWindow.show()
    sys.exit(app.exec_())
