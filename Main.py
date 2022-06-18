# Jump.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem

import lymp_predict_bygenerator_invoking
from detail.UI_Fail_Dialog import Fail_Dialog
from detail.bmob import *
from detail.UI_Detail_Folder import Ui_Detail_Folder
from detail.UI_Gradle_Detail_Picture import Ui_Gradle_Detail_Picture
from detail.UI_Login import Ui_Login
from detail.UI_Select_Detail_Way import Ui_Select_Detail_Way
from detail.UI_Select_Function import Ui_Select_Function
from detail.UI_Type_Detail_Picture import Ui_Type_Detail_Picture
from utils import invasive_predict_bygenerator_invoking
from utils import lymp_predict_bygenerator_invoking
from utils import invasive_predict_bygenerator_folder_invoking
from utils import lymp_predict_bygenerator_folder_invoking
import  random
class UiFailDialog(QtWidgets.QWidget, Fail_Dialog):
    def __init__(self):
        super(UiFailDialog, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.closeDialog)

    def closeDialog(self):
        self.close()

class UiTypeDetailPicture(QtWidgets.QWidget, Ui_Type_Detail_Picture):
    def __init__(self):
        super(UiTypeDetailPicture, self).__init__()
        self.setupUi(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.setWindowTitle(_translate("Form", "智能病理辅助诊断平台-浸润性乳腺癌分级辅助诊断"))
        self.label.setText(_translate("Form", "诊断级别"))
        self.textEdit.setFontPointSize(13)

class UiGradleDetailFolder(QtWidgets.QWidget, Ui_Detail_Folder):
    model = invasive_predict_bygenerator_folder_invoking.loadmodel()

    def __init__(self):
        super(UiGradleDetailFolder, self).__init__()
        self.setupUi(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.setWindowTitle(_translate("Form", "智能病理辅助诊断平台-浸润性导管癌分级辅助诊断"))
        self.pushButton_2.clicked.connect(self.getResult)

    def getResult(self):
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['文件名', '诊断类别', '诊断分析'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        filename_list, pre_list, advice_list =invasive_predict_bygenerator_folder_invoking.predict_folder(self.model,self.directory)
        filename_list1=[]
        pre_list1=[]
        advice_list1=[]
        for i in random.sample(range(1,len(filename_list)+1),len(filename_list)):
            filename_list1.append(filename_list[i-1])
            pre_list1.append(pre_list[i-1])
            advice_list1.append(advice_list[i-1])

        self.tableWidget.setRowCount(len(filename_list))

        for i in range(len(filename_list1)):
            item1 = QTableWidgetItem(str(filename_list1[i-1]))
            item3 = QTableWidgetItem(str(advice_list1[i-1]))
            item2 = QTableWidgetItem(str(pre_list1[i-1]))
            item1.setTextAlignment(Qt.AlignCenter)
            item2.setTextAlignment(Qt.AlignCenter)
            item3.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(i, 0, item1)
            self.tableWidget.setItem(i, 1, item2)
            self.tableWidget.setItem(i, 2, item3)


class UiGradleThreeDetailPicture(QtWidgets.QWidget, Ui_Type_Detail_Picture):
    model = lymp_predict_bygenerator_invoking.loadmodel()
    def __init__(self):
        super(UiGradleThreeDetailPicture, self).__init__()
        self.setupUi(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.setWindowTitle(_translate("Form", "智能病理辅助诊断平台-淋巴瘤亚型分类辅助诊断"))
        self.label.setText(_translate("Form", "诊断类别"))
        self.textEdit.setFontPointSize(13)

    def getResult(self):
        grade = lymp_predict_bygenerator_invoking.predict(self.model, self.imgName)
        if grade == "CLL":
            advice="    慢性淋巴细胞白血病（CLL）是一种原发于造血组织的恶性肿瘤。肿瘤细胞为单克隆的B淋巴细胞，形态类似正常成熟的小淋巴细胞，蓄积于血液、骨髓及淋巴组织中。慢性淋巴细胞白血病虽发展缓慢，但难以治愈。部分患者可向幼淋巴细胞白血病、弥漫大B细胞淋巴瘤、霍奇金淋巴瘤、急淋等其他恶性淋巴增殖性疾病转化。 "
        if grade == "FL":
            advice="    滤泡淋巴瘤（FL）是一种偏惰性的淋巴瘤，一般进展缓慢，患者生存期较长。部分病人会转化为弥漫大B细胞淋巴瘤，转化时往往会出现淋巴结快速生长，并有可能出现发热、盗汗、体重减轻等全身症状。即使发生了弥漫大B细胞转化，经规范化疗、放疗及分子靶向治疗仍有较好的疗效。"
        if grade == "MCL":
            advice="    套细胞淋巴瘤（MCL）是以高度侵袭性及预后不良为特征的一种特殊类型的B细胞非霍奇金淋巴瘤。ISMCN不需要治疗。惰性白血病样非淋巴结性MCL，如果没有治疗指征[参见中国慢性淋巴细胞白血病/小淋巴细胞淋巴瘤的诊断与治疗指南(2015年版)]可以先采取观察等待的策略。经典型MCL绝大部分应在诊断后即开始治疗。"
        self.lineEdit_2.setText("   "+grade)
        self.textEdit.setText(advice)

class UiGradleThreeDetailFolder(QtWidgets.QWidget, Ui_Detail_Folder):
    model = lymp_predict_bygenerator_folder_invoking.loadmodel()

    def __init__(self):
        super(UiGradleThreeDetailFolder, self).__init__()
        self.setupUi(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.setWindowTitle(_translate("Form", "智能病理辅助诊断平台-淋巴瘤亚型分类辅助诊断"))
        self.pushButton_2.clicked.connect(self.getResult)

    def getResult(self):

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['文件名', '诊断类别', '诊断分析'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        filename_list, pre_list, advice_list =lymp_predict_bygenerator_folder_invoking.predict_folder(self.model,self.directory)

        filename_list1 = []
        pre_list1 = []
        advice_list1 = []
        for i in random.sample(range(1, len(filename_list) + 1), len(filename_list)):
            filename_list1.append(filename_list[i - 1])
            pre_list1.append(pre_list[i - 1])
            advice_list1.append(advice_list[i - 1])

        self.tableWidget.setRowCount(len(filename_list))

        for i in range(len(filename_list1)):
            item1 = QTableWidgetItem(str(filename_list1[i-1]))
            item3 = QTableWidgetItem(str(advice_list1[i-1]))
            item2 = QTableWidgetItem(str(pre_list1[i-1]))
            item1.setTextAlignment(Qt.AlignCenter)
            item2.setTextAlignment(Qt.AlignCenter)
            item3.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(i, 0, item1)
            self.tableWidget.setItem(i, 1, item2)
            self.tableWidget.setItem(i, 2, item3)

class UiGradleDetailPicture(QtWidgets.QWidget, Ui_Gradle_Detail_Picture):
    model = invasive_predict_bygenerator_invoking.loadmodel()
    def __init__(self):
        super(UiGradleDetailPicture, self).__init__()
        self.setupUi(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.setWindowTitle(_translate("Form", "智能病理辅助诊断平台-浸润性导管癌分级辅助诊断"))
        self.label.setText(_translate("Form", "诊断类别"))
        self.textEdit.setFontPointSize(13)

    def getResult(self):
        grade = invasive_predict_bygenerator_invoking.predict(self.model, self.imgName)
        if grade == "Grade_1":
            advice = "    浸润性导管癌1级属于早期的病变，分裂程度较高，肿瘤恶变程度较低，及时进行综合性的治疗，有可能完全治愈。首先要尽早手术切除病灶。其次可以配合放疗、化疗、靶向细胞治疗等方法进行治疗。第三要进行饮食调理，患者要多吃含维生素多的蔬菜和水果、多吃高蛋白食物，不可吃油炸油煎食物。"
        if grade == "Grade_2":
            advice = "    浸润性导管癌2级属于乳腺癌癌症早期，预后相对比较好。建议进一步排查是否有远处转移，若内有远处转移，可尽早手术配合积极治疗，有效延长患者生命周期。术后建议根据病理检查结果配合放化疗，内分泌治疗，以及中药辅助治疗，调整心态，定期复查。"
        if grade == "Grade_3":
            advice = "    浸润性导管癌3级患者疾病处于中期，患者癌细胞可能出现转移和扩散。对患者进行积极有效的治疗，以很好的控制浸润性导管癌三级患者的病情，延长患者的生存期，也可提高浸润性导管癌三级患者的生存率。若不积极治疗，浸润性导管癌三级患者的疾病将迅速恶化。癌细胞可能扩散到全身，存活率大大降低，且可能导致生命危险。"

        self.lineEdit_2.setText("   "+grade)
        self.textEdit.setText(advice)

class UiTypeSelectDetailWay(QtWidgets.QWidget, Ui_Select_Detail_Way):
    def __init__(self):
        super(UiTypeSelectDetailWay, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.TypeDetailPicture)
        self.pushButton_2.clicked.connect(self.TypeDetailFolder)

    def TypeDetailPicture(self):
        self.dia = UiTypeDetailPicture()
        self.dia.show()

    def TypeDetailFolder(self):
        self.dia = UiTypeDetailFolder()
        self.dia.show()


class UiGradleThreeSelectDetailWay(QtWidgets.QWidget, Ui_Select_Detail_Way):
    def __init__(self):
        super(UiGradleThreeSelectDetailWay, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.GradleDetailPicture)
        self.pushButton_2.clicked.connect(self.GradleDetailFolder)

    def GradleDetailPicture(self):
        self.dia = UiGradleThreeDetailPicture()
        self.dia.show()

    def GradleDetailFolder(self):
        self.dia = UiGradleThreeDetailFolder()
        self.dia.show()


class UiGradleSelectDetailWay(QtWidgets.QWidget, Ui_Select_Detail_Way):
    def __init__(self):
        super(UiGradleSelectDetailWay, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.GradleDetailPicture)
        self.pushButton_2.clicked.connect(self.GradleDetailFolder)

    def GradleDetailPicture(self):
        self.dia = UiGradleDetailPicture()
        self.dia.show()

    def GradleDetailFolder(self):
        self.dia = UiGradleDetailFolder()
        self.dia.show()


class UiSelectFunction(QtWidgets.QWidget, Ui_Select_Function):
    def __init__(self):
        super(UiSelectFunction, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ThreeDetail)
        self.pushButton_2.clicked.connect(self.GradleDetail)
        self.pushButton_3.clicked.connect(self.ThreeDetail)

    def GradleDetail(self):
        self.dia = UiGradleSelectDetailWay()
        self.dia.show()

    def TypeDetail(self):
        self.dia = UiTypeSelectDetailWay()
        self.dia.show()

    def ThreeDetail(self):
        self.dia = UiGradleThreeSelectDetailWay()
        self.dia.show()


class login(QtWidgets.QMainWindow, Ui_Login):
    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.loginSystem)

    def loginEvent(self):
        if self.lineEdit.text() != None and self.lineEdit_2.text() != None:
            self.close()
            self.dia = UiSelectFunction()
            self.dia.show()

    def loginSystem(self):
        if str(self.lineEdit.text()) is None or str(self.lineEdit_2.text()) is None:
            self.dia = UiFailDialog()
            self.dia.show()
        else:
            b = Bmob("0781caa7f2e03c4a606378c78a65b06a", "9d285f2c2c80a2ecce44c3406ec450da")
            account = b.find(
                "Account",
                BmobQuerier().
                    addWhereEqualTo("account", str(self.lineEdit.text().strip())).
                    addWhereEqualTo("password", str(self.lineEdit_2.text().strip()))
            )
            if account.err is None:
                data2 = json.loads(account.stringData)
                d1 = data2["results"]
                if len(d1) > 0:
                    self.loginEvent()
                else:
                    self.dia = UiFailDialog()
                    self.dia.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('LOGO.png'))
    first = login()
    first.show()
    # first.pushButton.clicked.connect(first.loginEvent)
    sys.exit(app.exec_())
