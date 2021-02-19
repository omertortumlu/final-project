from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
from keras.models import model_from_json  # for json file update/save
from keras.models import load_model  # for .h5 file update/save
from keras.models import Model
import threading
import time
import sys
import testModul
import trainModul
import traceback


class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))
        pass

    def flush(self):
        pass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1601, 908)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/ytu1.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 5, 1600, 900))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
                                     "    alignment: center;\n"
                                     "  padding-left: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QTabWidget::pane {\n"
                                     "    background: transparent;\n"
                                     "    border:0;\n"
                                     "}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/iQIWOs.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setGeometry(QtCore.QRect(390, 250, 381, 51))
        self.widget_2.setObjectName("widget_2")
        self.widget_6 = QtWidgets.QWidget(self.tab)
        self.widget_6.setGeometry(QtCore.QRect(50, 90, 401, 701))
        self.widget_6.setStyleSheet("")
        self.widget_6.setObjectName("widget_6")
        self.label_23 = QtWidgets.QLabel(self.widget_6)
        self.label_23.setGeometry(QtCore.QRect(0, 250, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("border-radius: 2px;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "border:2px solid rgb(0, 255, 0);\n"
                                    "")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_5 = QtWidgets.QLabel(self.widget_6)
        self.label_5.setGeometry(QtCore.QRect(80, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
                                   "border-radius: 2px;\n"
                                   "color:rgb(255, 255, 255);\n"
                                   "border:2px solid rgb(0, 255, 0);\n"
                                   "")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_37 = QtWidgets.QLabel(self.widget_6)
        self.label_37.setGeometry(QtCore.QRect(0, 10, 401, 691))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("\n"
                                    "border-radius: 2px;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "border:2px solid rgb(0, 255, 0);\n"
                                    "")
        self.label_37.setText("")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.widget_6)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 310, 381, 381))
        self.tabWidget_2.setStyleSheet("QTabWidget::pane {\n"
                                       "    background: transparent;\n"
                                       "    border:0;\n"
                                       "}")
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_53 = QtWidgets.QLabel(self.tab_3)
        self.label_53.setGeometry(QtCore.QRect(20, 90, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_53.setFont(font)
        self.label_53.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_53.setAutoFillBackground(False)
        self.label_53.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_53.setTextFormat(QtCore.Qt.AutoText)
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.bm_imagenet = QtWidgets.QRadioButton(self.tab_3)
        self.bm_imagenet.setGeometry(QtCore.QRect(140, 245, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bm_imagenet.setFont(font)
        self.bm_imagenet.setStyleSheet("   border: 1px solid gray;\n"
                                       "    border-radius: 3px;\n"
                                       "    text-align: center;\n"
                                       "background-color: rgb(224, 220, 255);")
        self.bm_imagenet.setChecked(True)
        self.bm_imagenet.setObjectName("bm_imagenet")
        self.label_54 = QtWidgets.QLabel(self.tab_3)
        self.label_54.setGeometry(QtCore.QRect(60, 40, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_54.setFont(font)
        self.label_54.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_54.setAutoFillBackground(False)
        self.label_54.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_54.setTextFormat(QtCore.Qt.AutoText)
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.label_61 = QtWidgets.QLabel(self.tab_3)
        self.label_61.setGeometry(QtCore.QRect(20, 190, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_61.setFont(font)
        self.label_61.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_61.setAutoFillBackground(False)
        self.label_61.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_61.setTextFormat(QtCore.Qt.AutoText)
        self.label_61.setAlignment(QtCore.Qt.AlignCenter)
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.tab_3)
        self.label_62.setGeometry(QtCore.QRect(50, 240, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_62.setFont(font)
        self.label_62.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_62.setAutoFillBackground(False)
        self.label_62.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_62.setTextFormat(QtCore.Qt.AutoText)
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.bm_model = QtWidgets.QComboBox(self.tab_3)
        self.bm_model.setGeometry(QtCore.QRect(140, 40, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bm_model.setFont(font)
        self.bm_model.setStyleSheet("QComboBox {\n"
                                    "    border: 1px solid gray;\n"
                                    "    border-radius: 3px;\n"
                                    "    text-align: center;\n"
                                    "    border: 2px solid;\n"
                                    "background-color: rgb(224, 220, 255);\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.bm_model.setObjectName("bm_model")
        #There are 18 models in keras
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.bm_model.addItem("")
        self.label_63 = QtWidgets.QLabel(self.tab_3)
        self.label_63.setGeometry(QtCore.QRect(30, 140, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_63.setFont(font)
        self.label_63.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_63.setAutoFillBackground(False)
        self.label_63.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_63.setTextFormat(QtCore.Qt.AutoText)
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.bm_optimizer = QtWidgets.QComboBox(self.tab_3)
        self.bm_optimizer.setGeometry(QtCore.QRect(140, 140, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bm_optimizer.setFont(font)
        self.bm_optimizer.setStyleSheet("QComboBox {\n"
                                        "    border: 1px solid gray;\n"
                                        "    border-radius: 3px;\n"
                                        "    text-align: center;\n"
                                        "    border: 2px solid;\n"
                                        "background-color: rgb(224, 220, 255);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.bm_optimizer.setObjectName("bm_optimizer")
        self.bm_optimizer.addItem("")
        self.bm_optimizer.addItem("")
        self.bm_optimizer.addItem("")
        self.bm_optimizer.addItem("")
        self.bm_optimizer.addItem("")
        self.bm_optimizer.addItem("")
        self.bm_optimizer.addItem("")
        self.bm_activation = QtWidgets.QComboBox(self.tab_3)
        self.bm_activation.setGeometry(QtCore.QRect(140, 90, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bm_activation.setFont(font)
        self.bm_activation.setStyleSheet("QComboBox {\n"
                                         "    border: 1px solid gray;\n"
                                         "    border-radius: 3px;\n"
                                         "    text-align: center;\n"
                                         "    border: 2px solid;\n"
                                         "background-color: rgb(224, 220, 255);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.bm_activation.setObjectName("bm_activation")
        self.bm_activation.addItem("")
        self.bm_activation.addItem("")
        self.bm_activation.addItem("")
        self.bm_activation.addItem("")
        self.bm_activation.addItem("")
        self.bm_activation.addItem("")
        self.bm_activation.addItem("")
        self.bm_activation.addItem("")
        self.bm_activation.addItem("")
        self.bm_activation.addItem("")
        self.bm_activation.addItem("")
        self.bm_modelLoss = QtWidgets.QComboBox(self.tab_3)
        self.bm_modelLoss.setGeometry(QtCore.QRect(140, 190, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bm_modelLoss.setFont(font)
        self.bm_modelLoss.setStyleSheet("QComboBox {\n"
                                        "    border: 1px solid gray;\n"
                                        "    border-radius: 3px;\n"
                                        "    text-align: center;\n"
                                        "    border: 2px solid;\n"
                                        "background-color: rgb(224, 220, 255);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.bm_modelLoss.setObjectName("bm_modelLoss")
        #There are 26 models in keras
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_modelLoss.addItem("")
        self.bm_none = QtWidgets.QRadioButton(self.tab_3)
        self.bm_none.setGeometry(QtCore.QRect(260, 245, 91, 20))
        self.bm_none.setStyleSheet("   border: 1px solid gray;\n"
                                   "    border-radius: 3px;\n"
                                   "    text-align: center;\n"
                                   "background-color: rgb(224, 220, 255);")
        self.bm_none.setObjectName("bm_none")
        self.bm_optimizerLr = QtWidgets.QLineEdit(self.tab_3)
        self.bm_optimizerLr.setGeometry(QtCore.QRect(140, 290, 71, 21))
        self.bm_optimizerLr.setStyleSheet("   border: 1px solid gray;\n"
                                          "    border-radius: 3px;\n"
                                          "    text-align: center;\n"
                                          "    border: 2px;\n"
                                          "background-color: rgb(224, 220, 255);")
        self.bm_optimizerLr.setInputMask("")
        self.bm_optimizerLr.setText("0.01")
        self.bm_optimizerLr.setAlignment(QtCore.Qt.AlignCenter)
        self.bm_optimizerLr.setObjectName("bm_optimizerLr")
        self.label_68 = QtWidgets.QLabel(self.tab_3)
        self.label_68.setGeometry(QtCore.QRect(10, 285, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_68.setFont(font)
        self.label_68.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_68.setAutoFillBackground(False)
        self.label_68.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_68.setTextFormat(QtCore.Qt.AutoText)
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.bm_imageSize = QtWidgets.QLineEdit(self.tab_3)
        self.bm_imageSize.setGeometry(QtCore.QRect(140, 330, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bm_imageSize.setFont(font)
        self.bm_imageSize.setStyleSheet("   border: 1px solid gray;\n"
                                        "    border-radius: 3px;\n"
                                        "    text-align: center;\n"
                                        "    border: 2px;\n"
                                        "background-color: rgb(224, 220, 255);")
        self.bm_imageSize.setInputMask("")
        self.bm_imageSize.setText("")
        self.bm_imageSize.setAlignment(QtCore.Qt.AlignCenter)
        self.bm_imageSize.setObjectName("bm_imageSize")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(0, 320, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_14.setTextFormat(QtCore.Qt.AutoText)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.ptm_button_json = QtWidgets.QPushButton(self.tab_4)
        self.ptm_button_json.setGeometry(QtCore.QRect(330, 85, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.ptm_button_json.setFont(font)
        self.ptm_button_json.setStyleSheet("   border: 1px solid gray;\n"
                                           "    border-radius: 3px;\n"
                                           "    text-align: center;\n"
                                           "    border: 2px;\n"
                                           "background-color:#008CBA;\n"
                                           "color:white;")
        self.ptm_button_json.setObjectName("ptm_button_json")
        self.label_64 = QtWidgets.QLabel(self.tab_4)
        self.label_64.setGeometry(QtCore.QRect(20, 130, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_64.setFont(font)
        self.label_64.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_64.setAutoFillBackground(False)
        self.label_64.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_64.setTextFormat(QtCore.Qt.AutoText)
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.tab_4)
        self.label_65.setGeometry(QtCore.QRect(10, 230, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_65.setFont(font)
        self.label_65.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_65.setAutoFillBackground(False)
        self.label_65.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_65.setTextFormat(QtCore.Qt.AutoText)
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.tab_4)
        self.label_66.setGeometry(QtCore.QRect(20, 180, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_66.setFont(font)
        self.label_66.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_66.setAutoFillBackground(False)
        self.label_66.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_66.setTextFormat(QtCore.Qt.AutoText)
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.ptm_path_json = QtWidgets.QLineEdit(self.tab_4)
        self.ptm_path_json.setGeometry(QtCore.QRect(140, 85, 175, 20))
        self.ptm_path_json.setStyleSheet("   border: 1px solid gray;\n"
                                         "    border-radius: 3px;\n"
                                         "    text-align: center;\n"
                                         "    border: 2px;\n"
                                         "background-color: rgb(224, 220, 255);")
        self.ptm_path_json.setInputMask("")
        self.ptm_path_json.setText("")
        self.ptm_path_json.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ptm_path_json.setObjectName("ptm_path_json")
        self.ptm_optimizer = QtWidgets.QComboBox(self.tab_4)
        self.ptm_optimizer.setGeometry(QtCore.QRect(140, 180, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ptm_optimizer.setFont(font)
        self.ptm_optimizer.setStyleSheet("QComboBox {\n"
                                         "    border: 1px solid gray;\n"
                                         "    border-radius: 3px;\n"
                                         "    text-align: center;\n"
                                         "    border: 2px solid;\n"
                                         "background-color: rgb(224, 220, 255);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.ptm_optimizer.setObjectName("ptm_optimizer")
        self.ptm_optimizer.addItem("")
        self.ptm_optimizer.addItem("")
        self.ptm_optimizer.addItem("")
        self.ptm_optimizer.addItem("")
        self.ptm_optimizer.addItem("")
        self.ptm_optimizer.addItem("")
        self.ptm_optimizer.addItem("")
        self.ptm_path_h5 = QtWidgets.QLineEdit(self.tab_4)
        self.ptm_path_h5.setGeometry(QtCore.QRect(140, 40, 175, 20))
        self.ptm_path_h5.setStyleSheet("   border: 1px solid gray;\n"
                                       "    border-radius: 3px;\n"
                                       "    text-align: center;\n"
                                       "    border: 2px;\n"
                                       "background-color: rgb(224, 220, 255);")
        self.ptm_path_h5.setInputMask("")
        self.ptm_path_h5.setText("")
        self.ptm_path_h5.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ptm_path_h5.setObjectName("ptm_path_h5")
        self.ptm_button_h5 = QtWidgets.QPushButton(self.tab_4)
        self.ptm_button_h5.setGeometry(QtCore.QRect(330, 40, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.ptm_button_h5.setFont(font)
        self.ptm_button_h5.setStyleSheet("   border: 1px solid gray;\n"
                                         "    border-radius: 3px;\n"
                                         "    text-align: center;\n"
                                         "    border: 2px;\n"
                                         "background-color:#008CBA;\n"
                                         "color:white;")
        self.ptm_button_h5.setAutoDefault(True)
        self.ptm_button_h5.setDefault(True)
        self.ptm_button_h5.setObjectName("ptm_button_h5")
        self.ptm_activation = QtWidgets.QComboBox(self.tab_4)
        self.ptm_activation.setGeometry(QtCore.QRect(140, 130, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ptm_activation.setFont(font)
        self.ptm_activation.setStyleSheet("QComboBox {\n"
                                          "    border: 1px solid gray;\n"
                                          "    border-radius: 3px;\n"
                                          "    text-align: center;\n"
                                          "    border: 2px solid;\n"
                                          "background-color: rgb(224, 220, 255);\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "")
        self.ptm_activation.setObjectName("ptm_activation")
        self.ptm_activation.addItem("")
        self.ptm_activation.addItem("")
        self.ptm_activation.addItem("")
        self.ptm_activation.addItem("")
        self.ptm_activation.addItem("")
        self.ptm_activation.addItem("")
        self.ptm_activation.addItem("")
        self.ptm_activation.addItem("")
        self.ptm_activation.addItem("")
        self.ptm_activation.addItem("")
        self.ptm_activation.addItem("")
        self.ptm_modelLoss = QtWidgets.QComboBox(self.tab_4)
        self.ptm_modelLoss.setGeometry(QtCore.QRect(140, 230, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ptm_modelLoss.setFont(font)
        self.ptm_modelLoss.setStyleSheet("QComboBox {\n"
                                         "    border: 1px solid gray;\n"
                                         "    border-radius: 3px;\n"
                                         "    text-align: center;\n"
                                         "    border: 2px solid;\n"
                                         "background-color: rgb(224, 220, 255);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.ptm_modelLoss.setObjectName("ptm_modelLoss")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_modelLoss.addItem("")
        self.ptm_optimizerLr = QtWidgets.QLineEdit(self.tab_4)
        self.ptm_optimizerLr.setGeometry(QtCore.QRect(150, 290, 71, 21))
        self.ptm_optimizerLr.setStyleSheet("   border: 1px solid gray;\n"
                                           "    border-radius: 3px;\n"
                                           "    text-align: center;\n"
                                           "    border: 2px;\n"
                                           "background-color: rgb(224, 220, 255);")
        self.ptm_optimizerLr.setInputMask("")
        self.ptm_optimizerLr.setText("0.01")
        self.ptm_optimizerLr.setAlignment(QtCore.Qt.AlignCenter)
        self.ptm_optimizerLr.setObjectName("ptm_optimizerLr")
        self.label_67 = QtWidgets.QLabel(self.tab_4)
        self.label_67.setGeometry(QtCore.QRect(20, 285, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_67.setFont(font)
        self.label_67.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_67.setAutoFillBackground(False)
        self.label_67.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_67.setTextFormat(QtCore.Qt.AutoText)
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.label_69 = QtWidgets.QLabel(self.tab_4)
        self.label_69.setGeometry(QtCore.QRect(40, 40, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_69.setFont(font)
        self.label_69.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_69.setAutoFillBackground(False)
        self.label_69.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_69.setTextFormat(QtCore.Qt.AutoText)
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.tab_4)
        self.label_70.setGeometry(QtCore.QRect(40, 80, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_70.setFont(font)
        self.label_70.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_70.setAutoFillBackground(False)
        self.label_70.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_70.setTextFormat(QtCore.Qt.AutoText)
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setObjectName("label_70")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.widget_5 = QtWidgets.QWidget(self.widget_6)
        self.widget_5.setGeometry(QtCore.QRect(10, 50, 381, 191))
        self.widget_5.setObjectName("widget_5")
        self.lbl_augrate = QtWidgets.QLabel(self.widget_5)
        self.lbl_augrate.setGeometry(QtCore.QRect(220, 100, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_augrate.setFont(font)
        self.lbl_augrate.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                       "border-radius: 2px;\n"
                                       "color:rgb(20, 30, 40);")
        self.lbl_augrate.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_augrate.setObjectName("lbl_augrate")
        self.label_21 = QtWidgets.QLabel(self.widget_5)
        self.label_21.setGeometry(QtCore.QRect(80, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_21.setAutoFillBackground(False)
        self.label_21.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_21.setTextFormat(QtCore.Qt.AutoText)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_24 = QtWidgets.QLabel(self.widget_5)
        self.label_24.setGeometry(QtCore.QRect(30, 133, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_24.setAutoFillBackground(False)
        self.label_24.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_24.setTextFormat(QtCore.Qt.AutoText)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_22 = QtWidgets.QLabel(self.widget_5)
        self.label_22.setGeometry(QtCore.QRect(70, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_22.setAutoFillBackground(False)
        self.label_22.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_22.setTextFormat(QtCore.Qt.AutoText)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_12 = QtWidgets.QLabel(self.widget_5)
        self.label_12.setGeometry(QtCore.QRect(10, 90, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.hS_augrate = QtWidgets.QSlider(self.widget_5)
        self.hS_augrate.setGeometry(QtCore.QRect(250, 100, 121, 22))
        self.hS_augrate.setStyleSheet("color: rgb(255, 255, 255);")
        self.hS_augrate.setMaximum(10)
        self.hS_augrate.setOrientation(QtCore.Qt.Horizontal)
        self.hS_augrate.setInvertedAppearance(False)
        self.hS_augrate.setInvertedControls(False)
        self.hS_augrate.setObjectName("hS_augrate")
        self._trainEpoch = QtWidgets.QLineEdit(self.widget_5)
        self._trainEpoch.setGeometry(QtCore.QRect(220, 60, 61, 21))
        self._trainEpoch.setStyleSheet("   border: 1px solid gray;\n"
                                       "    border-radius: 3px;\n"
                                       "    text-align: center;\n"
                                       "    border: 2px;\n"
                                       "background-color: rgb(224, 220, 255);")
        self._trainEpoch.setInputMask("")
        self._trainEpoch.setText("20")
        self._trainEpoch.setAlignment(QtCore.Qt.AlignCenter)
        self._trainEpoch.setObjectName("_trainEpoch")
        self._batchSize = QtWidgets.QLineEdit(self.widget_5)
        self._batchSize.setGeometry(QtCore.QRect(220, 20, 61, 21))
        self._batchSize.setStyleSheet("   border: 1px solid gray;\n"
                                      "    border-radius: 3px;\n"
                                      "    text-align: center;\n"
                                      "    border: 2px;\n"
                                      "background-color: rgb(224, 220, 255);")
        self._batchSize.setInputMask("")
        self._batchSize.setText("16")
        self._batchSize.setAlignment(QtCore.Qt.AlignCenter)
        self._batchSize.setObjectName("_batchSize")
        self._rgb = QtWidgets.QCheckBox(self.widget_5)
        self._rgb.setGeometry(QtCore.QRect(220, 140, 20, 20))
        self._rgb.setText("")
        self._rgb.setObjectName("_rgb")
        self._rgb.setChecked(True)
        self.label_37.raise_()
        self.label_23.raise_()
        self.label_5.raise_()
        self.tabWidget_2.raise_()
        self.widget_5.raise_()
        self.widget_7 = QtWidgets.QWidget(self.tab)
        self.widget_7.setGeometry(QtCore.QRect(490, 90, 401, 701))
        self.widget_7.setObjectName("widget_7")
        self.label_6 = QtWidgets.QLabel(self.widget_7)
        self.label_6.setGeometry(QtCore.QRect(60, 10, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-radius: 2px;\n"
                                   "color:rgb(255, 255, 255);\n"
                                   "border:2px solid rgb(0, 255, 0);\n"
                                   "")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_20 = QtWidgets.QLabel(self.widget_7)
        self.label_20.setGeometry(QtCore.QRect(0, 280, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("border-radius: 2px;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "border:2px solid rgb(0, 255, 0);\n"
                                    "")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_36 = QtWidgets.QLabel(self.widget_7)
        self.label_36.setGeometry(QtCore.QRect(0, 10, 401, 691))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("border-radius: 2px;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "border:2px solid rgb(0, 255, 0);\n"
                                    "")
        self.label_36.setText("")
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.widget_8 = QtWidgets.QWidget(self.widget_7)
        self.widget_8.setGeometry(QtCore.QRect(0, 330, 401, 301))
        self.widget_8.setObjectName("widget_8")
        self.comboBox_fillMode = QtWidgets.QComboBox(self.widget_8)
        self.comboBox_fillMode.setGeometry(QtCore.QRect(230, 260, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_fillMode.setFont(font)
        self.comboBox_fillMode.setStyleSheet("QComboBox {\n"
                                             "    border: 1px solid gray;\n"
                                             "    border-radius: 3px;\n"
                                             "    text-align: center;\n"
                                             "    border: 2px solid;\n"
                                             "background-color: rgb(224, 220, 255);\n"
                                             "\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "")
        self.comboBox_fillMode.setObjectName("comboBox_fillMode")
        self.comboBox_fillMode.addItem("")
        self.comboBox_fillMode.addItem("")
        self.comboBox_fillMode.addItem("")
        self.comboBox_fillMode.addItem("")
        self.label_42 = QtWidgets.QLabel(self.widget_8)
        self.label_42.setGeometry(QtCore.QRect(30, 50, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_42.setFont(font)
        self.label_42.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_42.setAutoFillBackground(False)
        self.label_42.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_42.setTextFormat(QtCore.Qt.AutoText)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.widget_8)
        self.label_43.setGeometry(QtCore.QRect(30, 90, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_43.setFont(font)
        self.label_43.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_43.setAutoFillBackground(False)
        self.label_43.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_43.setTextFormat(QtCore.Qt.AutoText)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.lbl_wsr = QtWidgets.QLabel(self.widget_8)
        self.lbl_wsr.setGeometry(QtCore.QRect(230, 100, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_wsr.setFont(font)
        self.lbl_wsr.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                   "border-radius: 2px;\n"
                                   "color:rgb(20, 30, 40);")
        self.lbl_wsr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_wsr.setObjectName("lbl_wsr")
        self.hS_zr = QtWidgets.QSlider(self.widget_8)
        self.hS_zr.setGeometry(QtCore.QRect(260, 140, 121, 22))
        self.hS_zr.setStyleSheet("color: rgb(255, 255, 255);")
        self.hS_zr.setMaximum(10)
        self.hS_zr.setOrientation(QtCore.Qt.Horizontal)
        self.hS_zr.setInvertedAppearance(False)
        self.hS_zr.setInvertedControls(False)
        self.hS_zr.setObjectName("hS_zr")
        self.cB_horizantalFlip = QtWidgets.QCheckBox(self.widget_8)
        self.cB_horizantalFlip.setGeometry(QtCore.QRect(230, 223, 20, 20))
        self.cB_horizantalFlip.setText("")
        self.cB_horizantalFlip.setObjectName("cB_horizantalFlip")
        self.hS_sr = QtWidgets.QSlider(self.widget_8)
        self.hS_sr.setGeometry(QtCore.QRect(260, 180, 121, 22))
        self.hS_sr.setStyleSheet("color: rgb(255, 255, 255);")
        self.hS_sr.setMaximum(10)
        self.hS_sr.setOrientation(QtCore.Qt.Horizontal)
        self.hS_sr.setInvertedAppearance(False)
        self.hS_sr.setInvertedControls(False)
        self.hS_sr.setObjectName("hS_sr")
        self.label_46 = QtWidgets.QLabel(self.widget_8)
        self.label_46.setGeometry(QtCore.QRect(110, 260, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_46.setFont(font)
        self.label_46.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_46.setAutoFillBackground(False)
        self.label_46.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_46.setTextFormat(QtCore.Qt.AutoText)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.lbl_sr = QtWidgets.QLabel(self.widget_8)
        self.lbl_sr.setGeometry(QtCore.QRect(230, 180, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sr.setFont(font)
        self.lbl_sr.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                  "border-radius: 2px;\n"
                                  "color:rgb(20, 30, 40);")
        self.lbl_sr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sr.setObjectName("lbl_sr")
        self.label_44 = QtWidgets.QLabel(self.widget_8)
        self.label_44.setGeometry(QtCore.QRect(70, 170, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_44.setFont(font)
        self.label_44.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_44.setAutoFillBackground(False)
        self.label_44.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_44.setTextFormat(QtCore.Qt.AutoText)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.lbl_zr = QtWidgets.QLabel(self.widget_8)
        self.lbl_zr.setGeometry(QtCore.QRect(230, 140, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_zr.setFont(font)
        self.lbl_zr.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                  "border-radius: 2px;\n"
                                  "color:rgb(20, 30, 40);")
        self.lbl_zr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_zr.setObjectName("lbl_zr")
        self.hS_wsr = QtWidgets.QSlider(self.widget_8)
        self.hS_wsr.setGeometry(QtCore.QRect(260, 100, 121, 22))
        self.hS_wsr.setStyleSheet("color: rgb(255, 255, 255);")
        self.hS_wsr.setMaximum(10)
        self.hS_wsr.setOrientation(QtCore.Qt.Horizontal)
        self.hS_wsr.setInvertedAppearance(False)
        self.hS_wsr.setInvertedControls(False)
        self.hS_wsr.setObjectName("hS_wsr")
        self.label_45 = QtWidgets.QLabel(self.widget_8)
        self.label_45.setGeometry(QtCore.QRect(60, 210, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_45.setFont(font)
        self.label_45.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_45.setAutoFillBackground(False)
        self.label_45.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_45.setTextFormat(QtCore.Qt.AutoText)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.label_40 = QtWidgets.QLabel(self.widget_8)
        self.label_40.setGeometry(QtCore.QRect(50, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_40.setAutoFillBackground(False)
        self.label_40.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_40.setTextFormat(QtCore.Qt.AutoText)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.hS_rr = QtWidgets.QSlider(self.widget_8)
        self.hS_rr.setGeometry(QtCore.QRect(260, 20, 121, 21))
        self.hS_rr.setStyleSheet("color: rgb(255, 255, 255);")
        self.hS_rr.setMaximum(18)
        self.hS_rr.setOrientation(QtCore.Qt.Horizontal)
        self.hS_rr.setInvertedAppearance(False)
        self.hS_rr.setInvertedControls(False)
        self.hS_rr.setObjectName("hS_rr")
        self.lbl_rr = QtWidgets.QLabel(self.widget_8)
        self.lbl_rr.setGeometry(QtCore.QRect(230, 20, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_rr.setFont(font)
        self.lbl_rr.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                  "border-radius: 2px;\n"
                                  "color:rgb(20, 30, 40);")
        self.lbl_rr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rr.setObjectName("lbl_rr")
        self.lbl_hsr = QtWidgets.QLabel(self.widget_8)
        self.lbl_hsr.setGeometry(QtCore.QRect(230, 60, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_hsr.setFont(font)
        self.lbl_hsr.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                   "border-radius: 2px;\n"
                                   "color:rgb(20, 30, 40);")
        self.lbl_hsr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_hsr.setObjectName("lbl_hsr")
        self.label_41 = QtWidgets.QLabel(self.widget_8)
        self.label_41.setGeometry(QtCore.QRect(70, 130, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_41.setAutoFillBackground(False)
        self.label_41.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_41.setTextFormat(QtCore.Qt.AutoText)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.hS_hsr = QtWidgets.QSlider(self.widget_8)
        self.hS_hsr.setGeometry(QtCore.QRect(260, 60, 121, 22))
        self.hS_hsr.setStyleSheet("color: rgb(255, 255, 255);")
        self.hS_hsr.setMaximum(10)
        self.hS_hsr.setOrientation(QtCore.Qt.Horizontal)
        self.hS_hsr.setInvertedAppearance(False)
        self.hS_hsr.setInvertedControls(False)
        self.hS_hsr.setObjectName("hS_hsr")
        self.widget_4 = QtWidgets.QWidget(self.widget_7)
        self.widget_4.setGeometry(QtCore.QRect(10, 80, 391, 121))
        self.widget_4.setObjectName("widget_4")
        self._original = QtWidgets.QRadioButton(self.widget_4)
        self._original.setGeometry(QtCore.QRect(150, 60, 71, 21))
        self._original.setStyleSheet("   border: 1px solid gray;\n"
                                     "    border-radius: 3px;\n"
                                     "    text-align: center;\n"
                                     "background-color: rgb(224, 220, 255);")
        self._original.setChecked(False)
        self._original.setObjectName("_original")
        self.label_13 = QtWidgets.QLabel(self.widget_4)
        self.label_13.setGeometry(QtCore.QRect(10, 55, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.pr_original = QtWidgets.QLineEdit(self.widget_4)
        self.pr_original.setGeometry(QtCore.QRect(190, 90, 31, 20))
        self.pr_original.setStyleSheet("   border: 1px solid gray;\n"
                                       "    border-radius: 3px;\n"
                                       "    text-align: center;\n"
                                       "\n"
                                       "background-color: rgb(224, 220, 255);")
        self.pr_original.setInputMask("")
        self.pr_original.setText("")
        self.pr_original.setAlignment(QtCore.Qt.AlignCenter)
        self.pr_original.setObjectName("pr_original")
        self._folded = QtWidgets.QRadioButton(self.widget_4)
        self._folded.setEnabled(True)

        self._folded.setGeometry(QtCore.QRect(260, 60, 71, 20))
        self._folded.setStyleSheet("   border: 1px solid gray;\n"
                                   "    border-radius: 3px;\n"
                                   "    text-align: center;\n"
                                   "background-color: rgb(224, 220, 255);")
        self._folded.setChecked(True)
        self._folded.setObjectName("_folded")
        self.k_original = QtWidgets.QLineEdit(self.widget_4)
        self.k_original.setGeometry(QtCore.QRect(150, 90, 31, 20))
        self.k_original.setStyleSheet("   border: 1px solid gray;\n"
                                      "    border-radius: 3px;\n"
                                      "    text-align: center;\n"
                                      "\n"
                                      "background-color: rgb(224, 220, 255);")
        self.k_original.setInputMask("")
        self.k_original.setText("")
        self.k_original.setAlignment(QtCore.Qt.AlignCenter)
        self.k_original.setObjectName("k_original")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setGeometry(QtCore.QRect(55, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(224, 220, 255);")
        self.label_2.setObjectName("label_2")
        self.button_dataset = QtWidgets.QPushButton(self.widget_4)
        self.button_dataset.setGeometry(QtCore.QRect(350, 10, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.button_dataset.setFont(font)
        self.button_dataset.setStyleSheet("   border: 1px solid gray;\n"
                                          "    border-radius: 3px;\n"
                                          "    text-align: center;\n"
                                          "    border: 2px;\n"
                                          "background-color:#008CBA;\n"
                                          "color:white;")
        self.button_dataset.setObjectName("button_dataset")
        self.dataset_path = QtWidgets.QLineEdit(self.widget_4)
        self.dataset_path.setGeometry(QtCore.QRect(145, 10, 201, 20))
        self.dataset_path.setStyleSheet("   border: 1px solid gray;\n"
                                        "    border-radius: 3px;\n"
                                        "    text-align: center;\n"
                                        "    border: 2px rgb(0, 0, 255);\n"
                                        "background-color: rgb(224, 220, 255);")
        self.dataset_path.setInputMask("")
        self.dataset_path.setText("")
        self.dataset_path.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.dataset_path.setObjectName("dataset_path")
        self.label_36.raise_()
        self.label_6.raise_()
        self.label_20.raise_()
        self.widget_8.raise_()
        self.widget_4.raise_()
        self.widget_3 = QtWidgets.QWidget(self.tab)
        self.widget_3.setGeometry(QtCore.QRect(940, 90, 601, 711))
        self.widget_3.setObjectName("widget_3")
        self.label_16 = QtWidgets.QLabel(self.widget_3)
        self.label_16.setGeometry(QtCore.QRect(220, 370, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border-radius: 2px;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "border:2px solid rgb(0, 255, 0);\n"
                                    "")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(0, 370, 601, 335))
        self.label_7.setStyleSheet("border-radius: 2px;\n"
                                   "color:rgb(255, 255, 255);\n"
                                   "border:2px solid rgb(0, 255, 0);\n"
                                   "")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_18 = QtWidgets.QLabel(self.widget_3)
        self.label_18.setGeometry(QtCore.QRect(220, 10, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border-radius: 2px;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "border:2px solid rgb(0, 255, 0);\n"
                                    "")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_17 = QtWidgets.QLabel(self.widget_3)
        self.label_17.setGeometry(QtCore.QRect(0, 10, 601, 335))
        self.label_17.setStyleSheet("border-radius: 2px;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "border:2px solid rgb(0, 255, 0);\n"
                                    "")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.output_screen = QtWidgets.QTextEdit(self.widget_3)
        self.output_screen.setGeometry(QtCore.QRect(10, 60, 581, 271))
        self.output_screen.setObjectName("output_screen")
        self.scores_screen = QtWidgets.QTextEdit(self.widget_3)
        self.scores_screen.setGeometry(QtCore.QRect(20, 420, 371, 91))
        self.scores_screen.setObjectName("scores_screen")
        self.output_dataset_path = QtWidgets.QLineEdit(self.widget_3)
        self.output_dataset_path.setGeometry(QtCore.QRect(115, 600, 151, 20))
        self.output_dataset_path.setStyleSheet("   border: 1px solid gray;\n"
                                               "    border-radius: 3px;\n"
                                               "    text-align: center;\n"
                                               "    border: 2px rgb(0, 0, 255);\n"
                                               "background-color: rgb(224, 220, 255);")
        self.output_dataset_path.setInputMask("")
        self.output_dataset_path.setText("")
        self.output_dataset_path.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.output_dataset_path.setObjectName("output_dataset_path")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(40, 600, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(224, 220, 255);")
        self.label_4.setObjectName("label_4")
        self.label_38 = QtWidgets.QLabel(self.widget_3)
        self.label_38.setGeometry(QtCore.QRect(320, 590, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color:rgb(224, 220, 255);")
        self.label_38.setObjectName("label_38")
        self.output_model_path = QtWidgets.QLineEdit(self.widget_3)
        self.output_model_path.setGeometry(QtCore.QRect(410, 600, 151, 20))
        self.output_model_path.setStyleSheet("   border: 1px solid gray;\n"
                                             "    border-radius: 3px;\n"
                                             "    text-align: center;\n"
                                             "    border: 2px rgb(0, 0, 255);\n"
                                             "background-color: rgb(224, 220, 255);")
        self.output_model_path.setInputMask("")
        self.output_model_path.setText("")
        self.output_model_path.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.output_model_path.setObjectName("output_model_path")
        self.label_52 = QtWidgets.QLabel(self.widget_3)
        self.label_52.setGeometry(QtCore.QRect(15, 560, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color:rgb(224, 220, 255);")
        self.label_52.setObjectName("label_52")
        self.output_data_name = QtWidgets.QLineEdit(self.widget_3)
        self.output_data_name.setGeometry(QtCore.QRect(115, 560, 151, 20))
        self.output_data_name.setStyleSheet("   border: 1px solid gray;\n"
                                            "    border-radius: 3px;\n"
                                            "    text-align: center;\n"
                                            "    border: 2px rgb(0, 0, 255);\n"
                                            "background-color: rgb(224, 220, 255);")
        self.output_data_name.setInputMask("")
        self.output_data_name.setText("")
        self.output_data_name.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.output_data_name.setObjectName("output_data_name")
        self.start_button = QtWidgets.QPushButton(self.widget_3)
        self.start_button.setGeometry(QtCore.QRect(20, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(18)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("   border: 1px solid gray;\n"
                                        "    border-radius: 3px;\n"
                                        "    text-align: center;\n"
                                        "    border: 2px;\n"
                                        "background-color:#4CAF50;\n"
                                        "color:white;")
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(self.widget_3)
        self.stop_button.setGeometry(QtCore.QRect(390, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(18)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.stop_button.setFont(font)
        self.stop_button.setStyleSheet("   border: 1px solid gray;\n"
                                       "    border-radius: 3px;\n"
                                       "    text-align: center;\n"
                                       "    border: 2px;\n"
                                       "background-color:#f44336;\n"
                                       "color:white;")
        self.stop_button.setObjectName("stop_button")
        self.button_save = QtWidgets.QPushButton(self.widget_3)
        self.button_save.setGeometry(QtCore.QRect(140, 650, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.button_save.setFont(font)
        self.button_save.setStyleSheet("   border: 1px solid gray;\n"
                                       "    border-radius: 3px;\n"
                                       "    text-align: center;\n"
                                       "    border: 2px;\n"
                                       "background-color:#008CBA;\n"
                                       "color:white;")
        self.button_save.setObjectName("button_save")
        self.button_model_output = QtWidgets.QPushButton(self.widget_3)
        self.button_model_output.setGeometry(QtCore.QRect(570, 600, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.button_model_output.setFont(font)
        self.button_model_output.setStyleSheet("   border: 1px solid gray;\n"
                                               "    border-radius: 3px;\n"
                                               "    text-align: center;\n"
                                               "    border: 2px;\n"
                                               "background-color:#008CBA;\n"
                                               "color:white;")
        self.button_model_output.setObjectName("button_model_output")
        self.button_dataset_output = QtWidgets.QPushButton(self.widget_3)
        self.button_dataset_output.setGeometry(QtCore.QRect(275, 600, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.button_dataset_output.setFont(font)
        self.button_dataset_output.setStyleSheet("   border: 1px solid gray;\n"
                                                 "    border-radius: 3px;\n"
                                                 "    text-align: center;\n"
                                                 "    border: 2px;\n"
                                                 "background-color:#008CBA;\n"
                                                 "color:white;")
        self.button_dataset_output.setObjectName("button_dataset_output")
        self.progressBar = QtWidgets.QProgressBar(self.widget_3)
        self.progressBar.setGeometry(QtCore.QRect(40, 525, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.label_75 = QtWidgets.QLabel(self.widget_3)
        self.label_75.setGeometry(QtCore.QRect(295, 560, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.label_75.setFont(font)
        self.label_75.setStyleSheet("color:rgb(224, 220, 255);")
        self.label_75.setObjectName("label_75")
        self.output_model_name = QtWidgets.QLineEdit(self.widget_3)
        self.output_model_name.setGeometry(QtCore.QRect(410, 560, 151, 20))
        self.output_model_name.setStyleSheet("   border: 1px solid gray;\n"
                                             "    border-radius: 3px;\n"
                                             "    text-align: center;\n"
                                             "    border: 2px rgb(0, 0, 255);\n"
                                             "background-color: rgb(224, 220, 255);")
        self.output_model_name.setInputMask("")
        self.output_model_name.setText("")
        self.output_model_name.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.output_model_name.setObjectName("output_model_name")
        self.allModels = QtWidgets.QComboBox(self.widget_3)
        self.allModels.setGeometry(QtCore.QRect(420, 450, 121, 22))
        self.allModels.setObjectName("allModels")
        self.label_76 = QtWidgets.QLabel(self.widget_3)
        self.label_76.setGeometry(QtCore.QRect(430, 420, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.label_76.setFont(font)
        self.label_76.setStyleSheet("color:rgb(224, 220, 255);")
        self.label_76.setObjectName("label_76")
        self.button_confusion_matrix = QtWidgets.QPushButton(self.widget_3)
        self.button_confusion_matrix.setGeometry(
            QtCore.QRect(440, 490, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.button_confusion_matrix.setFont(font)
        self.button_confusion_matrix.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_confusion_matrix.setContextMenuPolicy(
            QtCore.Qt.DefaultContextMenu)
        self.button_confusion_matrix.setStyleSheet("   border: 1px solid gray;\n"
                                                   "    border-radius: 3px;\n"
                                                   "    text-align: center;\n"
                                                   "    border: 2px;\n"
                                                   "background-color:#008CBA;\n"
                                                   "color:white;")
        self.button_confusion_matrix.setObjectName("button_confusion_matrix")
        self.label_7.raise_()
        self.label_17.raise_()
        self.label_16.raise_()
        self.label_18.raise_()
        self.output_screen.raise_()
        self.scores_screen.raise_()
        self.output_dataset_path.raise_()
        self.label_4.raise_()
        self.label_38.raise_()
        self.output_model_path.raise_()
        self.label_52.raise_()
        self.output_data_name.raise_()
        self.start_button.raise_()
        self.stop_button.raise_()
        self.button_save.raise_()
        self.button_model_output.raise_()
        self.button_dataset_output.raise_()
        self.progressBar.raise_()
        self.label_75.raise_()
        self.output_model_name.raise_()
        self.allModels.raise_()
        self.label_76.raise_()
        self.button_confusion_matrix.raise_()
        self.pushButton_12 = QtWidgets.QPushButton(self.tab)
        self.pushButton_12.setGeometry(QtCore.QRect(290, 30, 1101, 51))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(27)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("border: 1px solid gray;\n"
                                         "border-radius: 5px;\n"
                                         "text-align: center;\n"
                                         "border: 2px;\n"
                                         "color:rgb(0, 255, 0);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_55 = QtWidgets.QLabel(self.tab)
        self.label_55.setGeometry(QtCore.QRect(1450, 10, 80, 80))
        self.label_55.setText("")
        self.label_55.setPixmap(QtGui.QPixmap("img/ytu1.ico"))
        self.label_55.setScaledContents(True)
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.label_57 = QtWidgets.QLabel(self.tab)
        self.label_57.setGeometry(QtCore.QRect(50, 50, 101, 31))
        self.label_57.setText("")
        self.label_57.setPixmap(QtGui.QPixmap("img/tenserflow.png"))
        self.label_57.setScaledContents(True)
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.tab)
        self.label_58.setGeometry(QtCore.QRect(160, 50, 101, 31))
        self.label_58.setText("")
        self.label_58.setPixmap(QtGui.QPixmap("img/keras_logo.png"))
        self.label_58.setScaledContents(True)
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab)
        self.pushButton_13.setGeometry(QtCore.QRect(1290, 800, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("border: 1px solid gray;\n"
                                         "border-radius: 5px;\n"
                                         "text-align: center;\n"
                                         "border: 2px;\n"
                                         "color:rgb(0, 255, 0);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.label_26.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("img/iQIWOs.jpg"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(430, 140, 5, 650))
        self.label_15.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                    "border-radius: 2px;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.test_button_h5 = QtWidgets.QPushButton(self.tab_2)
        self.test_button_h5.setGeometry(QtCore.QRect(340, 310, 51, 20))
        self.test_button_h5.setStyleSheet("   border: 1px solid gray;\n"
                                          "    border-radius: 3px;\n"
                                          "    text-align: center;\n"
                                          "    border: 2px;\n"
                                          "background-color: rgb(224, 220, 255);")
        self.test_button_h5.setObjectName("test_button_h5")
        self.test_path_h5 = QtWidgets.QLineEdit(self.tab_2)
        self.test_path_h5.setGeometry(QtCore.QRect(155, 310, 171, 20))
        self.test_path_h5.setStyleSheet("   border: 1px solid gray;\n"
                                        "    border-radius: 3px;\n"
                                        "    border: 2px rgb(0, 0, 255);\n"
                                        "background-color: rgb(224, 220, 255);")
        self.test_path_h5.setInputMask("")
        self.test_path_h5.setText("")
        self.test_path_h5.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.test_path_h5.setObjectName("test_path_h5")
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(130, 230, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "border:2px solid rgb(0, 255, 0);\n"
                                    "border-radius: 2px;")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(810, 140, 5, 650))
        self.label_28.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                    "border-radius: 2px;")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(222, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                    "border-radius: 2px;")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.label_32 = QtWidgets.QLabel(self.tab_2)
        self.label_32.setGeometry(QtCore.QRect(1120, 270, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                    "border-radius: 2px;\n"
                                    "color:rgb(20, 30, 40);")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab_2)
        self.label_33.setGeometry(QtCore.QRect(910, 270, 601, 5))
        self.label_33.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                    "border-radius: 2px;")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.test_button_dataset = QtWidgets.QPushButton(self.tab_2)
        self.test_button_dataset.setGeometry(QtCore.QRect(690, 290, 51, 20))
        self.test_button_dataset.setStyleSheet("   border: 1px solid gray;\n"
                                               "    border-radius: 3px;\n"
                                               "    text-align: center;\n"
                                               "    border: 2px;\n"
                                               "background-color: rgb(224, 220, 255);")
        self.test_button_dataset.setObjectName("test_button_dataset")
        self.label_34 = QtWidgets.QLabel(self.tab_2)
        self.label_34.setGeometry(QtCore.QRect(510, 230, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "border:2px solid rgb(0, 255, 0);\n"
                                    "border-radius: 2px;")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.test_dataset_path = QtWidgets.QLineEdit(self.tab_2)
        self.test_dataset_path.setGeometry(QtCore.QRect(475, 290, 201, 20))
        self.test_dataset_path.setStyleSheet("   border: 1px solid gray;\n"
                                             "    border-radius: 3px;\n"
                                             "    border: 2px rgb(0, 0, 255);\n"
                                             "background-color: rgb(224, 220, 255);")
        self.test_dataset_path.setInputMask("")
        self.test_dataset_path.setText("")
        self.test_dataset_path.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.test_dataset_path.setObjectName("test_dataset_path")
        self.test_path_json = QtWidgets.QLineEdit(self.tab_2)
        self.test_path_json.setGeometry(QtCore.QRect(155, 350, 171, 20))
        self.test_path_json.setStyleSheet("   border: 1px solid gray;\n"
                                          "    border-radius: 3px;\n"
                                          "    border: 2px rgb(0, 0, 255);\n"
                                          "background-color: rgb(224, 220, 255);")
        self.test_path_json.setInputMask("")
        self.test_path_json.setText("")
        self.test_path_json.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.test_path_json.setObjectName("test_path_json")
        self.test_button_json = QtWidgets.QPushButton(self.tab_2)
        self.test_button_json.setGeometry(QtCore.QRect(340, 350, 51, 20))
        self.test_button_json.setStyleSheet("   border: 1px solid gray;\n"
                                            "    border-radius: 3px;\n"
                                            "    text-align: center;\n"
                                            "    border: 2px;\n"
                                            "background-color: rgb(224, 220, 255);")
        self.test_button_json.setObjectName("test_button_json")
        self.test_screen = QtWidgets.QTextEdit(self.tab_2)
        self.test_screen.setGeometry(QtCore.QRect(900, 330, 601, 371))
        self.test_screen.setObjectName("test_screen")
        self.label_59 = QtWidgets.QLabel(self.tab_2)
        self.label_59.setGeometry(QtCore.QRect(170, 60, 101, 31))
        self.label_59.setText("")
        self.label_59.setPixmap(QtGui.QPixmap("img/keras_logo.png"))
        self.label_59.setScaledContents(True)
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)
        self.label_59.setObjectName("label_59")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_19.setGeometry(QtCore.QRect(300, 40, 1101, 51))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(27)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("border: 1px solid gray;\n"
                                         "border-radius: 5px;\n"
                                         "text-align: center;\n"
                                         "border: 2px;\n"
                                         "color:rgb(0, 255, 0);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_56 = QtWidgets.QLabel(self.tab_2)
        self.label_56.setGeometry(QtCore.QRect(1460, 20, 80, 80))
        self.label_56.setText("")
        self.label_56.setPixmap(QtGui.QPixmap("img/ytu1.ico"))
        self.label_56.setScaledContents(True)
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.label_60 = QtWidgets.QLabel(self.tab_2)
        self.label_60.setGeometry(QtCore.QRect(60, 60, 101, 31))
        self.label_60.setText("")
        self.label_60.setPixmap(QtGui.QPixmap("img/tenserflow.png"))
        self.label_60.setScaledContents(True)
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setObjectName("label_60")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_20.setGeometry(QtCore.QRect(1290, 790, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("border: 1px solid gray;\n"
                                         "border-radius: 5px;\n"
                                         "text-align: center;\n"
                                         "border: 2px;\n"
                                         "color:rgb(0, 255, 0);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.label_71 = QtWidgets.QLabel(self.tab_2)
        self.label_71.setGeometry(QtCore.QRect(30, 390, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_71.setFont(font)
        self.label_71.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_71.setAutoFillBackground(False)
        self.label_71.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_71.setTextFormat(QtCore.Qt.AutoText)
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.tab_2)
        self.label_72.setGeometry(QtCore.QRect(20, 440, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_72.setFont(font)
        self.label_72.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_72.setAutoFillBackground(False)
        self.label_72.setStyleSheet("color:rgb(224, 220, 255);\n"
                                    "")
        self.label_72.setTextFormat(QtCore.Qt.AutoText)
        self.label_72.setAlignment(QtCore.Qt.AlignCenter)
        self.label_72.setObjectName("label_72")
        self.test_optimizer = QtWidgets.QComboBox(self.tab_2)
        self.test_optimizer.setGeometry(QtCore.QRect(150, 390, 181, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_optimizer.setFont(font)
        self.test_optimizer.setStyleSheet("QComboBox {\n"
                                          "    border: 1px solid gray;\n"
                                          "    border-radius: 3px;\n"
                                          "    text-align: center;\n"
                                          "    border: 2px solid;\n"
                                          "background-color: rgb(224, 220, 255);\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "")
        self.test_optimizer.setObjectName("test_optimizer")
        self.test_optimizer.addItem("")
        self.test_optimizer.addItem("")
        self.test_optimizer.addItem("")
        self.test_optimizer.addItem("")
        self.test_optimizer.addItem("")
        self.test_optimizer.addItem("")
        self.test_optimizer.addItem("")
        self.test_modelLoss = QtWidgets.QComboBox(self.tab_2)
        self.test_modelLoss.setGeometry(QtCore.QRect(150, 440, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_modelLoss.setFont(font)
        self.test_modelLoss.setStyleSheet("QComboBox {\n"
                                          "    border: 1px solid gray;\n"
                                          "    border-radius: 3px;\n"
                                          "    text-align: center;\n"
                                          "    border: 2px solid;\n"
                                          "background-color: rgb(224, 220, 255);\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "")
        self.test_modelLoss.setObjectName("test_modelLoss")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.test_modelLoss.addItem("")
        self.label_73 = QtWidgets.QLabel(self.tab_2)
        self.label_73.setGeometry(QtCore.QRect(70, 340, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_73.setFont(font)
        self.label_73.setStyleSheet("color:rgb(224, 220, 255);")
        self.label_73.setObjectName("label_73")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(80, 310, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(224, 220, 255);")
        self.label_8.setObjectName("label_8")
        self.test_button_start = QtWidgets.QPushButton(self.tab_2)
        self.test_button_start.setGeometry(QtCore.QRect(1080, 210, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(18)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.test_button_start.setFont(font)
        self.test_button_start.setStyleSheet("   border: 1px solid gray;\n"
                                             "    border-radius: 3px;\n"
                                             "    text-align: center;\n"
                                             "    border: 2px;\n"
                                             "background-color:#4CAF50;\n"
                                             "color:white;")
        self.test_button_start.setObjectName("test_button_start")
        self.label_31 = QtWidgets.QLabel(self.tab_2)
        self.label_31.setGeometry(QtCore.QRect(600, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                    "border-radius: 2px;")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.label_74 = QtWidgets.QLabel(self.tab_2)
        self.label_74.setGeometry(QtCore.QRect(1180, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_74.setFont(font)
        self.label_74.setStyleSheet("background-color: rgb(224, 220, 255);\n"
                                    "border-radius: 2px;")
        self.label_74.setAlignment(QtCore.Qt.AlignCenter)
        self.label_74.setObjectName("label_74")
        self.button_confusion_matrix_2 = QtWidgets.QPushButton(self.tab_2)
        self.button_confusion_matrix_2.setGeometry(
            QtCore.QRect(1050, 720, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.button_confusion_matrix_2.setFont(font)
        self.button_confusion_matrix_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_confusion_matrix_2.setContextMenuPolicy(
            QtCore.Qt.DefaultContextMenu)
        self.button_confusion_matrix_2.setStyleSheet("   border: 1px solid gray;\n"
                                                     "    border-radius: 3px;\n"
                                                     "    text-align: center;\n"
                                                     "    border: 2px;\n"
                                                     "background-color:#008CBA;\n"
                                                     "color:white;")
        self.button_confusion_matrix_2.setObjectName(
            "button_confusion_matrix_2")
        self.label_26.raise_()
        self.label_15.raise_()
        self.test_button_h5.raise_()
        self.test_path_h5.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.test_button_dataset.raise_()
        self.label_34.raise_()
        self.test_dataset_path.raise_()
        self.test_path_json.raise_()
        self.test_button_json.raise_()
        self.test_screen.raise_()
        self.label_59.raise_()
        self.pushButton_19.raise_()
        self.label_56.raise_()
        self.label_60.raise_()
        self.pushButton_20.raise_()
        self.label_71.raise_()
        self.label_72.raise_()
        self.test_optimizer.raise_()
        self.test_modelLoss.raise_()
        self.label_73.raise_()
        self.label_8.raise_()
        self.test_button_start.raise_()
        self.label_31.raise_()
        self.label_74.raise_()
        self.button_confusion_matrix_2.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.label_25.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("img/iQIWOs.jpg"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.label_25.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ######################################################################
        ######################################################################
        ######################################################################

        self.hS_augrate.valueChanged.connect(self.hS_augrate_change)

        self.ptm_button_h5.clicked.connect(self.getPathH5)
        self.ptm_button_json.clicked.connect(self.getPathJson)

        self.button_dataset.clicked.connect(self.getPathDataset)

        self.hS_rr.valueChanged.connect(self.hS_rr_change)
        self.hS_hsr.valueChanged.connect(self.hS_hsr_change)
        self.hS_wsr.valueChanged.connect(self.hS_wsr_change)
        self.hS_zr.valueChanged.connect(self.hS_zr_change)
        self.hS_sr.valueChanged.connect(self.hS_sr_change)
        self.start_button.clicked.connect(self.startTrain)
        self.stop_button.clicked.connect(self.stopTrain)

        self.button_dataset_output.clicked.connect(self.setPathDataset)
        self.button_model_output.clicked.connect(self.setPathH5json)
        self.button_save.clicked.connect(self.saveToDisk)
        self.button_confusion_matrix.clicked.connect(self.confusionMatrix)
        ######################################################################
        self.test_button_h5.clicked.connect(self.testgetPathH5)
        self.test_button_json.clicked.connect(self.testgetPathJson)
        self.test_button_dataset.clicked.connect(self.getPathTestDataset)
        self.test_button_start.clicked.connect(self.startTest)
        self.button_confusion_matrix_2.clicked.connect(
            self.testConfusionMatrix)

        ######################################################################
        ######################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Transfer Learning"))
        self.label_23.setText(_translate("MainWindow", "Model Parameters"))
        self.label_5.setText(_translate("MainWindow", "Global Parameters"))
        self.label_53.setText(_translate("MainWindow", "Activation:"))
        self.bm_imagenet.setText(_translate("MainWindow", "Imagenet"))
        self.label_54.setText(_translate("MainWindow", "Model:"))
        self.label_61.setText(_translate("MainWindow", "Model_loss:"))
        self.label_62.setText(_translate("MainWindow", "Weight:"))
        self.bm_model.setItemText(0, _translate("MainWindow", "Xception"))
        self.bm_model.setItemText(1, _translate("MainWindow", "VGG16"))
        self.bm_model.setItemText(2, _translate("MainWindow", "VGG19"))
        self.bm_model.setItemText(3, _translate("MainWindow", "ResNet50"))
        self.bm_model.setItemText(4, _translate("MainWindow", "ResNet50V2"))
        self.bm_model.setItemText(5, _translate("MainWindow", "ResNet101"))
        self.bm_model.setItemText(6, _translate("MainWindow", "ResNet101V2"))
        self.bm_model.setItemText(7, _translate("MainWindow", "ResNet152"))
        self.bm_model.setItemText(8, _translate("MainWindow", "ResNet152V2"))
        self.bm_model.setItemText(9, _translate("MainWindow", "InceptionV3"))
        self.bm_model.setItemText(10, _translate("MainWindow", "InceptionResNetV2"))
        self.bm_model.setItemText(11, _translate("MainWindow", "MobileNet"))
        self.bm_model.setItemText(12, _translate("MainWindow", "MobileNetV2"))
        self.bm_model.setItemText(13, _translate("MainWindow", "DenseNet121"))
        self.bm_model.setItemText(14, _translate("MainWindow", "DenseNet169"))
        self.bm_model.setItemText(15, _translate("MainWindow", "DenseNet201"))
        self.bm_model.setItemText(16, _translate("MainWindow", "NASNetMobile"))
        self.bm_model.setItemText(17, _translate("MainWindow", "NASNetLarge"))
        self.label_63.setText(_translate("MainWindow", "Optimizer:"))
        self.bm_optimizer.setItemText(0, _translate("MainWindow", "SGD"))
        self.bm_optimizer.setItemText(1, _translate("MainWindow", "RMSprop"))
        self.bm_optimizer.setItemText(2, _translate("MainWindow", "Adagrad"))
        self.bm_optimizer.setItemText(3, _translate("MainWindow", "Adadelta"))
        self.bm_optimizer.setItemText(4, _translate("MainWindow", "Adam"))
        self.bm_optimizer.setItemText(5, _translate("MainWindow", "Adamax"))
        self.bm_optimizer.setItemText(6, _translate("MainWindow", "Nadam"))
        self.bm_activation.setItemText(0, _translate("MainWindow", "softmax"))
        self.bm_activation.setItemText(1, _translate("MainWindow", "softplus"))
        self.bm_activation.setItemText(2, _translate("MainWindow", "softsign"))
        self.bm_activation.setItemText(3, _translate("MainWindow", "sigmoid"))
        self.bm_activation.setItemText(
            4, _translate("MainWindow", "hard_sigmoid"))
        self.bm_activation.setItemText(5, _translate("MainWindow", "elu"))
        self.bm_activation.setItemText(6, _translate("MainWindow", "selu"))
        self.bm_activation.setItemText(7, _translate("MainWindow", "relu"))
        self.bm_activation.setItemText(8, _translate("MainWindow", "tanh"))
        self.bm_activation.setItemText(
            9, _translate("MainWindow", "exponential"))
        self.bm_activation.setItemText(10, _translate("MainWindow", "linear"))
        self.bm_modelLoss.setItemText(0, _translate(
            "MainWindow", "categorical_crossentropy"))
        self.bm_modelLoss.setItemText(1, _translate(
            "MainWindow", "binary_crossentropy"))
        self.bm_modelLoss.setItemText(
            2, _translate("MainWindow", "mean_squared_error"))
        self.bm_modelLoss.setItemText(3, _translate(
            "MainWindow", "mean_absolute_error"))
        self.bm_modelLoss.setItemText(4, _translate(
            "MainWindow", "mean_absolute_percentage_error"))
        self.bm_modelLoss.setItemText(5, _translate(
            "MainWindow", "mean_squared_logarithmic_error"))
        self.bm_modelLoss.setItemText(
            6, _translate("MainWindow", "squared_hinge"))
        self.bm_modelLoss.setItemText(7, _translate("MainWindow", "hinge"))
        self.bm_modelLoss.setItemText(
            8, _translate("MainWindow", "categorical_hinge"))
        self.bm_modelLoss.setItemText(9, _translate("MainWindow", "logcosh"))
        self.bm_modelLoss.setItemText(10, _translate(
            "MainWindow", "sparse_categorical_crossentropy"))
        self.bm_modelLoss.setItemText(11, _translate(
            "MainWindow", "kullback_leibler_divergence"))
        self.bm_modelLoss.setItemText(12, _translate("MainWindow", "poisson"))
        self.bm_modelLoss.setItemText(
            13, _translate("MainWindow", "cosine_proximity"))
        self.bm_none.setText(_translate("MainWindow", "None"))
        self.bm_optimizerLr.setPlaceholderText(_translate("MainWindow", "20"))
        self.label_68.setText(_translate("MainWindow", "Optimize_lr:"))
        self.bm_imageSize.setPlaceholderText(_translate("MainWindow", "Size"))
        self.label_14.setText(_translate("MainWindow", "  Image Size:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(
            self.tab_3), _translate("MainWindow", "Base Model"))
        self.ptm_button_json.setText(_translate("MainWindow", "..."))
        self.label_64.setText(_translate("MainWindow", "Activation:"))
        self.label_65.setText(_translate("MainWindow", "Model_loss:"))
        self.label_66.setText(_translate("MainWindow", "Optimizer:"))
        self.ptm_path_json.setPlaceholderText(
            _translate("MainWindow", "Path:...json"))
        self.ptm_optimizer.setItemText(0, _translate("MainWindow", "SGD"))
        self.ptm_optimizer.setItemText(1, _translate("MainWindow", "RMSprop"))
        self.ptm_optimizer.setItemText(2, _translate("MainWindow", "Adagrad"))
        self.ptm_optimizer.setItemText(3, _translate("MainWindow", "Adadelta"))
        self.ptm_optimizer.setItemText(4, _translate("MainWindow", "Adam"))
        self.ptm_optimizer.setItemText(5, _translate("MainWindow", "Adamax"))
        self.ptm_optimizer.setItemText(6, _translate("MainWindow", "Nadam"))
        self.ptm_path_h5.setPlaceholderText(
            _translate("MainWindow", "Path:...h5"))
        self.ptm_button_h5.setText(_translate("MainWindow", "..."))
        self.ptm_activation.setItemText(0, _translate("MainWindow", "softmax"))
        self.ptm_activation.setItemText(
            1, _translate("MainWindow", "softplus"))
        self.ptm_activation.setItemText(
            2, _translate("MainWindow", "softsign"))
        self.ptm_activation.setItemText(3, _translate("MainWindow", "sigmoid"))
        self.ptm_activation.setItemText(
            4, _translate("MainWindow", "hard_sigmoid"))
        self.ptm_activation.setItemText(5, _translate("MainWindow", "elu"))
        self.ptm_activation.setItemText(6, _translate("MainWindow", "selu"))
        self.ptm_activation.setItemText(7, _translate("MainWindow", "relu"))
        self.ptm_activation.setItemText(8, _translate("MainWindow", "tanh"))
        self.ptm_activation.setItemText(
            9, _translate("MainWindow", "exponential"))
        self.ptm_activation.setItemText(10, _translate("MainWindow", "linear"))
        self.ptm_modelLoss.setItemText(0, _translate(
            "MainWindow", "categorical_crossentropy"))
        self.ptm_modelLoss.setItemText(
            1, _translate("MainWindow", "binary_crossentropy"))
        self.ptm_modelLoss.setItemText(
            2, _translate("MainWindow", "mean_squared_error"))
        self.ptm_modelLoss.setItemText(
            3, _translate("MainWindow", "mean_absolute_error"))
        self.ptm_modelLoss.setItemText(4, _translate(
            "MainWindow", "mean_absolute_percentage_error"))
        self.ptm_modelLoss.setItemText(5, _translate(
            "MainWindow", "mean_squared_logarithmic_error"))
        self.ptm_modelLoss.setItemText(
            6, _translate("MainWindow", "squared_hinge"))
        self.ptm_modelLoss.setItemText(7, _translate("MainWindow", "hinge"))
        self.ptm_modelLoss.setItemText(
            8, _translate("MainWindow", "categorical_hinge"))
        self.ptm_modelLoss.setItemText(9, _translate("MainWindow", "logcosh"))
        self.ptm_modelLoss.setItemText(10, _translate(
            "MainWindow", "sparse_categorical_crossentropy"))
        self.ptm_modelLoss.setItemText(11, _translate(
            "MainWindow", "kullback_leibler_divergence"))
        self.ptm_modelLoss.setItemText(12, _translate("MainWindow", "poisson"))
        self.ptm_modelLoss.setItemText(
            13, _translate("MainWindow", "cosine_proximity"))
        self.ptm_optimizerLr.setPlaceholderText(_translate("MainWindow", "20"))
        self.label_67.setText(_translate("MainWindow", "Optimize_lr:"))
        self.label_69.setText(_translate("MainWindow", "/.h5:"))
        self.label_70.setText(_translate("MainWindow", "/.json:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(
            self.tab_4), _translate("MainWindow", "Pre-Trained Model"))
        self.lbl_augrate.setText(_translate("MainWindow", "0"))
        self.label_21.setText(_translate("MainWindow", "Batch Size:"))
        self.label_24.setText(_translate("MainWindow", "Convert to RGB:"))
        self.label_22.setText(_translate("MainWindow", "Train Epoch:"))
        self.label_12.setText(_translate("MainWindow", "Augmentation Rate:"))
        self._trainEpoch.setPlaceholderText(_translate("MainWindow", "20"))
        self._batchSize.setPlaceholderText(_translate("MainWindow", "Size"))
        self.label_6.setText(_translate("MainWindow", "Data Parameters"))
        self.label_20.setText(_translate(
            "MainWindow", "Data Generator Parameters"))
        self.comboBox_fillMode.setItemText(
            0, _translate("MainWindow", "nearest"))
        self.comboBox_fillMode.setItemText(
            1, _translate("MainWindow", "constant"))
        self.comboBox_fillMode.setItemText(
            2, _translate("MainWindow", "reflect"))
        self.comboBox_fillMode.setItemText(3, _translate("MainWindow", "wrap"))
        self.label_42.setText(_translate("MainWindow", "Height Shift Range:"))
        self.label_43.setText(_translate("MainWindow", "Width Shift Range:"))
        self.lbl_wsr.setText(_translate("MainWindow", "0"))
        self.label_46.setText(_translate("MainWindow", "Fill Mode:"))
        self.lbl_sr.setText(_translate("MainWindow", "0"))
        self.label_44.setText(_translate("MainWindow", "Shear Range:"))
        self.lbl_zr.setText(_translate("MainWindow", "0"))
        self.label_45.setText(_translate("MainWindow", "Horizontal Flip:"))
        self.label_40.setText(_translate("MainWindow", "Rotation Range:"))
        self.lbl_rr.setText(_translate("MainWindow", "0"))
        self.lbl_hsr.setText(_translate("MainWindow", "0"))
        self.label_41.setText(_translate("MainWindow", "Zoom Range:"))
        self._original.setText(_translate("MainWindow", "Original"))
        self.label_13.setText(_translate("MainWindow", "File structure:"))
        self.pr_original.setPlaceholderText(_translate("MainWindow", "%"))
        self._folded.setText(_translate("MainWindow", "Folded"))
        self.k_original.setPlaceholderText(_translate("MainWindow", "K"))
        self.label_2.setText(_translate("MainWindow", "Dataset:"))
        self.button_dataset.setText(_translate("MainWindow", "..."))
        self.dataset_path.setPlaceholderText(_translate("MainWindow", "Path:"))
        self.label_16.setText(_translate("MainWindow", "Results"))
        self.label_18.setText(_translate("MainWindow", "Training"))
        self.output_screen.setPlaceholderText(
            _translate("MainWindow", "Epoch..."))
        self.scores_screen.setPlaceholderText(
            _translate("MainWindow", "Scores:"))
        self.output_dataset_path.setPlaceholderText(
            _translate("MainWindow", "Path: "))
        self.label_4.setText(_translate("MainWindow", "Dataset:"))
        self.label_38.setText(_translate("MainWindow", ".h5/.json:"))
        self.output_model_path.setPlaceholderText(
            _translate("MainWindow", "Path:"))
        self.label_52.setText(_translate("MainWindow", "Data Name:"))
        self.output_data_name.setPlaceholderText(
            _translate("MainWindow", "Name"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "exit"))
        self.button_save.setText(_translate("MainWindow", "Save to disk"))
        self.button_model_output.setText(_translate("MainWindow", "..."))
        self.button_dataset_output.setText(_translate("MainWindow", "..."))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.label_75.setText(_translate("MainWindow", "Model Name:"))
        self.output_model_name.setPlaceholderText(
            _translate("MainWindow", "Name"))
        self.label_76.setText(_translate("MainWindow", "Select Model"))
        self.button_confusion_matrix.setText(_translate("MainWindow", "Confusion\n"
                                                        "Matrix"))
        self.pushButton_12.setText(_translate(
            "MainWindow", "Image Classification with Deep Learning"))
        self.pushButton_13.setText(_translate(
            "MainWindow", "ÖMER LÜTFÜ TORTUMLU"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "Train"))
        self.test_button_h5.setText(_translate("MainWindow", "Browse"))
        self.test_path_h5.setPlaceholderText(
            _translate("MainWindow", "Path: ...h5"))
        self.label_29.setText(_translate("MainWindow", "Training Model"))
        self.label_30.setText(_translate("MainWindow", "1"))
        self.label_32.setText(_translate("MainWindow", "RESULTS"))
        self.test_button_dataset.setText(_translate("MainWindow", "Browse"))
        self.label_34.setText(_translate("MainWindow", "Image Source"))
        self.test_dataset_path.setPlaceholderText(
            _translate("MainWindow", "Path:"))
        self.test_path_json.setPlaceholderText(
            _translate("MainWindow", "Path: ....json"))
        self.test_button_json.setText(_translate("MainWindow", "Browse"))
        self.test_screen.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11.12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.test_screen.setPlaceholderText(
            _translate("MainWindow", "Scores:"))
        self.pushButton_19.setText(_translate(
            "MainWindow", "Image Classification Test Section"))
        self.pushButton_20.setText(_translate(
            "MainWindow", "ÖMER LÜTFÜ TORTUMLU"))
        self.label_71.setText(_translate("MainWindow", "Optimizer:"))
        self.label_72.setText(_translate("MainWindow", "Model_loss:"))
        self.test_optimizer.setItemText(0, _translate("MainWindow", "SGD"))
        self.test_optimizer.setItemText(1, _translate("MainWindow", "RMSprop"))
        self.test_optimizer.setItemText(2, _translate("MainWindow", "Adagrad"))
        self.test_optimizer.setItemText(
            3, _translate("MainWindow", "Adadelta"))
        self.test_optimizer.setItemText(4, _translate("MainWindow", "Adam"))
        self.test_optimizer.setItemText(5, _translate("MainWindow", "Adamax"))
        self.test_optimizer.setItemText(6, _translate("MainWindow", "Nadam"))
        self.test_modelLoss.setItemText(0, _translate(
            "MainWindow", "categorical_crossentropy"))
        self.test_modelLoss.setItemText(
            1, _translate("MainWindow", "binary_crossentropy"))
        self.test_modelLoss.setItemText(
            2, _translate("MainWindow", "mean_squared_error"))
        self.test_modelLoss.setItemText(
            3, _translate("MainWindow", "mean_absolute_error"))
        self.test_modelLoss.setItemText(4, _translate(
            "MainWindow", "mean_absolute_percentage_error"))
        self.test_modelLoss.setItemText(5, _translate(
            "MainWindow", "mean_squared_logarithmic_error"))
        self.test_modelLoss.setItemText(
            6, _translate("MainWindow", "squared_hinge"))
        self.test_modelLoss.setItemText(7, _translate("MainWindow", "hinge"))
        self.test_modelLoss.setItemText(
            8, _translate("MainWindow", "categorical_hinge"))
        self.test_modelLoss.setItemText(9, _translate("MainWindow", "logcosh"))
        self.test_modelLoss.setItemText(10, _translate(
            "MainWindow", "sparse_categorical_crossentropy"))
        self.test_modelLoss.setItemText(11, _translate(
            "MainWindow", "kullback_leibler_divergence"))
        self.test_modelLoss.setItemText(
            12, _translate("MainWindow", "poisson"))
        self.test_modelLoss.setItemText(
            13, _translate("MainWindow", "cosine_proximity"))
        self.label_73.setText(_translate("MainWindow", "/.json:"))
        self.label_8.setText(_translate("MainWindow", "/.h5:"))
        self.test_button_start.setText(_translate("MainWindow", "Start Test"))
        self.label_31.setText(_translate("MainWindow", "2"))
        self.label_74.setText(_translate("MainWindow", "3"))
        self.button_confusion_matrix_2.setText(
            _translate("MainWindow", "Display Confusion Matrix"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "Test"))

    def hS_augrate_change(self):
        size = str(self.hS_augrate.value())
        self.lbl_augrate.setText(size)

    def hS_rr_change(self):
        size = str((self.hS_rr.value()-9)*10)
        self.lbl_rr.setText(size)

    def hS_hsr_change(self):
        size = str(self.hS_hsr.value()/10)
        self.lbl_hsr.setText(size)

    def hS_wsr_change(self):
        size = str(self.hS_wsr.value()/10)
        self.lbl_wsr.setText(size)

    def hS_zr_change(self):
        size = str(self.hS_zr.value()/10)
        self.lbl_zr.setText(size)

    def hS_sr_change(self):
        size = str(self.hS_sr.value()/10)
        self.lbl_sr.setText(size)

    def getPathH5(self):
        fname, _ = QFileDialog.getOpenFileName()
        path = str(fname)
        self.ptm_path_h5.setText(path)

    def getPathJson(self):
        fname, _ = QFileDialog.getOpenFileName()
        path = str(fname)
        self.ptm_path_json.setText(path)

    def getPathDataset(self):
        filename = QFileDialog.getExistingDirectory()
        path = str(filename)
        self.dataset_path.setText(path)

    def selectPathOutputDataset(self):
        filename = QFileDialog.getExistingDirectory()
        path = str(filename)
        self.output_dataset_path.setText(path)

    def setPathDataset(self):
        filename = QFileDialog.getExistingDirectory()
        path = str(filename)
        self.output_dataset_path.setText(path)

    def setPathH5json(self):
        filename = QFileDialog.getExistingDirectory()
        path = str(filename)
        self.output_model_path.setText(path)

    def selectPathOutputModel(self):
        filename = QFileDialog.getExistingDirectory()
        path = str(filename)
        self.output_model_path.setText(path)

    def startTrain(self):

        localtime = time.localtime(time.time())
        tm = str(localtime.tm_hour)+":" + \
            str(localtime.tm_min)+":"+str(localtime.tm_sec)
        self.scores_screen.setText("")
        # global values
        batchSize = int(self._batchSize.text())
        epoch = int(self._trainEpoch.text())
        convert_rgb = self._rgb.isChecked()
        augmentRate = int(self.lbl_augrate.text())

        # Augment values
        rr = int(self.lbl_rr.text())
        hsr = float(self.lbl_hsr.text())
        wsr = float(self.lbl_hsr.text())
        zr = float(self.lbl_zr.text())
        sr = float(self.lbl_sr.text())
        hf = self.cB_horizantalFlip.isChecked()
        fm = self.comboBox_fillMode.currentText()
        # Dataset values
        datasetPath = self.dataset_path.text()
        fileStructure = self._folded.isChecked()
        original_k = 1
        original_percent = 20
        # if selected original data k and percent values import
        try:
            if(self._original.isChecked()):
                # k fold bigger than zero and not empty
                if len(self.k_original.text()) > 0 and int(self.k_original.text()) > 0:
                    original_k = int(self.k_original.text())
                # percent value isEmpty value=20
                if len(self.pr_original.text()) > 0:
                    # test data 0-100
                    if(0 < int(self.pr_original.text()) < 100):
                        original_percent = int(self.pr_original.text())
        except:
            print("Exception fold values ​​are incorrect!!! ")

        # Select base model
        if(self.tabWidget_2.currentIndex() == 0):
            # self.output_screen.setStyleSheet("background-color: red")
            print("Start training with basemodel!!! ")
            try:
                self.output_screen.setStyleSheet("background-color: white")
                model = self.bm_model.currentText()
                activation = self.bm_activation.currentText()
                optimizer = self.bm_optimizer.currentText()
                loss = self.bm_modelLoss.currentText()
                imagenet = self.bm_imagenet.isChecked()
                optimizerLr = float(self.bm_optimizerLr.text())
                imageSize = int(self.bm_imageSize.text())

                try:
                    trainModul.baseModel(
                        self, model, activation, optimizer, loss, imagenet, optimizerLr, imageSize, batchSize, epoch, convert_rgb, augmentRate, rr, hsr, wsr, zr, sr, hf, fm, datasetPath, fileStructure, original_k, original_percent)
                    pass
                except Exception as err:
                    self.output_screen.setStyleSheet("background-color: red")
                    print(err)
                    pass
                pass
            except Exception as err:
                self.output_screen.setStyleSheet("background-color: red")
                print(str(err)+"\nYou should check the input values")
                pass

        else:
            try:
                self.output_screen.setStyleSheet("background-color: white")

                print("Start training with PreTrainingModel!!! ")
                _h5 = self.ptm_path_h5.text()
                _json = self.ptm_path_json.text()
                activation = self.ptm_activation.currentText()
                optimizer = self.ptm_optimizer.currentText()
                loss = self.ptm_modelLoss.currentText()
                optimizerLr = float(self.ptm_optimizerLr.text())
                try:
                    trainModul.preTrainedModel(self, _h5, activation, optimizer, loss, _json, optimizerLr, batchSize, epoch,
                                               augmentRate, rr, hsr, wsr, zr, sr, hf, fm, datasetPath, fileStructure, original_k, original_percent)
                    pass
                except Exception as err:
                    self.output_screen.setStyleSheet("background-color: red")
                    print(err)
                    pass
                pass
            except Exception as err:
                self.output_screen.setStyleSheet("background-color: red")
                print(str(err)+"\nYou should check the input values")
                pass
        # return newDataset, newModel
        localtime = time.localtime(time.time())
        etm = str(localtime.tm_hour)+":" + \
            str(localtime.tm_min)+":"+str(localtime.tm_sec)
        self.scores_screen.setText(
            self.scores_screen.toPlainText()+"Start Time: "+tm+" End Time: "+etm)

    def stopTrain(self):
        sys.exit("The player doesn't want to play again")

    def saveToDisk(self):
        try:
            fileStructure = self._original.isChecked()
            datasetPath = self.output_dataset_path.text()
            newModelPath = self.output_model_path.text()
            trainModul.savetodisk(self, fileStructure,
                                  datasetPath, newModelPath)
            pass
        except Exception as err:
            self.output_screen.setStyleSheet("background-color: red")
            print(str(err)+"\nYou don't save anything")
            pass

    def confusionMatrix(self):
        try:
            trainModul.confMat(self)
            pass
        except Exception as err:
            print(str(err)+"\nConfusion matrix could not display")
            pass

    #### TEST functions######
    #########################
    def testgetPathH5(self):
        fname, _ = QFileDialog.getOpenFileName()
        path = str(fname)
        self.test_path_h5.setText(path)

    def testgetPathJson(self):
        fname, _ = QFileDialog.getOpenFileName()
        path = str(fname)
        self.test_path_json.setText(path)

    def getPathTestDataset(self):
        filename = QFileDialog.getExistingDirectory()
        path = str(filename)
        self.test_dataset_path.setText(path)

    def startTest(self):
        testModul.test(self)

    def testConfusionMatrix(self):
        testModul.confMat(self)

    def __init__(self, parent=None, **kwargs):
        try:
            # ...
            # Install the custom output stream
            sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
            pass
        except:
            print("__init__")
            pass

    def __del__(self):
        try:
            # Restore sys.stdout
            sys.stdout = sys.__stdout__
            pass
        except:
            print("__del__")
            pass

    def normalOutputWritten(self, text):
        try:
            """Append text to the QTextEdit."""
            # Maybe QTextEdit.append() works as well, but this is how I do it:
            cursor = self.output_screen.textCursor()
            cursor.movePosition(QtGui.QTextCursor.End)
            cursor.insertText(text)
            self.output_screen.setTextCursor(cursor)
            self.output_screen.ensureCursorVisible()
            pass
        except:
            print("normalOutputWritten")
            pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
