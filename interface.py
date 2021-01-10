# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1108, 802)
        font = QtGui.QFont()
        font.setPointSize(10)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName("mainLayout")
        self.leftVertLayout = QtWidgets.QVBoxLayout()
        self.leftVertLayout.setContentsMargins(10, 10, 20, 10)
        self.leftVertLayout.setSpacing(10)
        self.leftVertLayout.setObjectName("leftVertLayout")
        self.graphicsView = VideoView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.leftVertLayout.addWidget(self.graphicsView)
        self.videoControlsLayout = QtWidgets.QHBoxLayout()
        self.videoControlsLayout.setObjectName("videoControlsLayout")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.playButton.setFont(font)
        self.playButton.setObjectName("playButton")
        self.videoControlsLayout.addWidget(self.playButton)
        self.mediaDurationSlider = QtWidgets.QSlider(self.centralwidget)
        self.mediaDurationSlider.setEnabled(False)
        self.mediaDurationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.mediaDurationSlider.setObjectName("mediaDurationSlider")
        self.videoControlsLayout.addWidget(self.mediaDurationSlider)
        self.leftVertLayout.addLayout(self.videoControlsLayout)
        self.graphLayout = QtWidgets.QHBoxLayout()
        self.graphLayout.setObjectName("graphLayout")
        self.leftVertLayout.addLayout(self.graphLayout)
        self.leftVertLayout.setStretch(0, 2)
        self.leftVertLayout.setStretch(2, 1)
        self.mainLayout.addLayout(self.leftVertLayout)
        self.rightVertLayout = QtWidgets.QVBoxLayout()
        self.rightVertLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.rightVertLayout.setContentsMargins(10, 10, 10, 10)
        self.rightVertLayout.setSpacing(10)
        self.rightVertLayout.setObjectName("rightVertLayout")
        self.pickDirectory = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pickDirectory.sizePolicy().hasHeightForWidth()
        )
        self.pickDirectory.setSizePolicy(sizePolicy)
        self.pickDirectory.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pickDirectory.setFont(font)
        self.pickDirectory.setObjectName("pickDirectory")
        self.rightVertLayout.addWidget(self.pickDirectory)
        self.showDataBase = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.showDataBase.setFont(font)
        self.showDataBase.setCheckable(False)
        self.showDataBase.setChecked(False)
        self.showDataBase.setObjectName("showDataBase")
        self.rightVertLayout.addWidget(self.showDataBase)
        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.rightVertLayout.addItem(spacerItem)
        self.clearScene = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clearScene.setFont(font)
        self.clearScene.setCheckable(False)
        self.clearScene.setChecked(False)
        self.clearScene.setObjectName("clearScene")
        self.rightVertLayout.addWidget(self.clearScene)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum
        )
        self.rightVertLayout.addItem(spacerItem1)
        self.userData = QtWidgets.QTextEdit(self.centralwidget)
        self.userData.setEnabled(True)
        self.userData.setMinimumSize(QtCore.QSize(400, 0))
        self.userData.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.userData.setReadOnly(True)
        self.userData.setObjectName("userData")
        self.rightVertLayout.addWidget(self.userData)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.rightVertLayout.addItem(spacerItem2)
        self.exitApplication = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exitApplication.setFont(font)
        self.exitApplication.setObjectName("exitApplication")
        self.rightVertLayout.addWidget(self.exitApplication)
        self.mainLayout.addLayout(self.rightVertLayout)
        self.mainLayout.setStretch(0, 2)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(
            _translate(
                "mainWindow", "Oprogramowanie wspomagające diagnozę objawu Raynauda"
            )
        )
        self.playButton.setText(_translate("mainWindow", "Play"))
        self.pickDirectory.setText(_translate("mainWindow", "Wybierz plik wideo"))
        self.showDataBase.setText(_translate("mainWindow", "Wybierz plik bazy danych"))
        self.clearScene.setText(_translate("mainWindow", "Wyczyść zaznaczenie"))
        self.exitApplication.setText(_translate("mainWindow", "Wyjdź z programu"))
        self.exitApplication.setShortcut(_translate("mainWindow", "Esc"))


from videoview import VideoView
