# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.max_number = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_number.sizePolicy().hasHeightForWidth())
        self.max_number.setSizePolicy(sizePolicy)
        self.max_number.setMaximum(100)
        self.max_number.setObjectName("max_number")
        self.gridLayout.addWidget(self.max_number, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.top_type = QtWidgets.QComboBox(self.groupBox)
        self.top_type.setObjectName("top_type")
        self.gridLayout.addWidget(self.top_type, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.reverse = QtWidgets.QCheckBox(self.groupBox)
        self.reverse.setObjectName("reverse")
        self.verticalLayout_3.addWidget(self.reverse)
        self.top_list = QtWidgets.QListWidget(self.groupBox)
        self.top_list.setObjectName("top_list")
        self.verticalLayout_3.addWidget(self.top_list)
        self.build_top = QtWidgets.QPushButton(self.groupBox)
        self.build_top.setObjectName("build_top")
        self.verticalLayout_3.addWidget(self.build_top)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.groupBox_2)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.count_parameter = QtWidgets.QComboBox(self.frame)
        self.count_parameter.setObjectName("count_parameter")
        self.horizontalLayout.addWidget(self.count_parameter)
        self.verticalLayout_2.addWidget(self.frame)
        self.count_laptops = QtWidgets.QPushButton(self.groupBox_2)
        self.count_laptops.setObjectName("count_laptops")
        self.verticalLayout_2.addWidget(self.count_laptops)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.correlation = QtWidgets.QPushButton(self.groupBox_2)
        self.correlation.setObjectName("correlation")
        self.verticalLayout_2.addWidget(self.correlation)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, 40, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.key_parameter = QtWidgets.QComboBox(self.groupBox_3)
        self.key_parameter.setObjectName("key_parameter")
        self.horizontalLayout_2.addWidget(self.key_parameter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.number_parameter = QtWidgets.QComboBox(self.groupBox_3)
        self.number_parameter.setObjectName("number_parameter")
        self.horizontalLayout_3.addWidget(self.number_parameter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.average_bar = QtWidgets.QPushButton(self.groupBox_3)
        self.average_bar.setObjectName("average_bar")
        self.verticalLayout_5.addWidget(self.average_bar)
        self.line_2 = QtWidgets.QFrame(self.groupBox_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.company = QtWidgets.QComboBox(self.groupBox_3)
        self.company.setObjectName("company")
        self.horizontalLayout_8.addWidget(self.company)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.average_price = QtWidgets.QPushButton(self.groupBox_3)
        self.average_price.setObjectName("average_price")
        self.verticalLayout_5.addWidget(self.average_price)
        self.line_3 = QtWidgets.QFrame(self.groupBox_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_5.addWidget(self.line_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.memory_type = QtWidgets.QComboBox(self.groupBox_3)
        self.memory_type.setObjectName("memory_type")
        self.horizontalLayout_6.addWidget(self.memory_type)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.number_parameter_memory = QtWidgets.QComboBox(self.groupBox_3)
        self.number_parameter_memory.setObjectName("number_parameter_memory")
        self.horizontalLayout_7.addWidget(self.number_parameter_memory)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.average_memory = QtWidgets.QPushButton(self.groupBox_3)
        self.average_memory.setObjectName("average_memory")
        self.verticalLayout_5.addWidget(self.average_memory)
        self.horizontalLayout_5.addWidget(self.groupBox_3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Tops"))
        self.label.setText(_translate("MainWindow", "Max number of items"))
        self.label_2.setText(_translate("MainWindow", "Top type"))
        self.reverse.setText(_translate("MainWindow", "Reverse"))
        self.build_top.setText(_translate("MainWindow", "Build top"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Plots"))
        self.label_3.setText(_translate("MainWindow", "Parameter"))
        self.count_laptops.setText(_translate("MainWindow", "Build count of laptops by parameter"))
        self.correlation.setText(_translate("MainWindow", "Build Correlation"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Other"))
        self.label_4.setText(_translate("MainWindow", "Key"))
        self.label_5.setText(_translate("MainWindow", "Number"))
        self.average_bar.setText(_translate("MainWindow", "Build average bar"))
        self.label_10.setText(_translate("MainWindow", "Company"))
        self.average_price.setText(_translate("MainWindow", "Show average company prices"))
        self.label_8.setText(_translate("MainWindow", "Memory type"))
        self.label_9.setText(_translate("MainWindow", "Number parameter"))
        self.average_memory.setText(_translate("MainWindow", "Show averege param from memory type"))