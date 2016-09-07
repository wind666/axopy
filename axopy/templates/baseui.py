# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/baseui.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BaseUI(object):
    def setupUi(self, BaseUI):
        BaseUI.setObjectName("BaseUI")
        BaseUI.setWindowModality(QtCore.Qt.NonModal)
        BaseUI.resize(665, 516)
        BaseUI.setStyleSheet("")
        BaseUI.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        BaseUI.setDocumentMode(False)
        BaseUI.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(BaseUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.participantTab = QtWidgets.QWidget()
        self.participantTab.setObjectName("participantTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.participantTab)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.participantTab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.participantTab)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 1)
        self.newParticipantButton = QtWidgets.QPushButton(self.participantTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newParticipantButton.sizePolicy().hasHeightForWidth())
        self.newParticipantButton.setSizePolicy(sizePolicy)
        self.newParticipantButton.setObjectName("newParticipantButton")
        self.gridLayout_2.addWidget(self.newParticipantButton, 2, 0, 1, 1)
        self.tabWidget.addTab(self.participantTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startTaskButton = QtWidgets.QPushButton(self.centralwidget)
        self.startTaskButton.setObjectName("startTaskButton")
        self.horizontalLayout.addWidget(self.startTaskButton)
        self.stopTaskButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopTaskButton.setObjectName("stopTaskButton")
        self.horizontalLayout.addWidget(self.stopTaskButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        BaseUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BaseUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 26))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        BaseUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BaseUI)
        self.statusbar.setObjectName("statusbar")
        BaseUI.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(BaseUI)
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.actionQuit.setIcon(icon)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(BaseUI)
        self.tabWidget.setCurrentIndex(0)
        self.actionQuit.triggered.connect(BaseUI.close)
        QtCore.QMetaObject.connectSlotsByName(BaseUI)

    def retranslateUi(self, BaseUI):
        _translate = QtCore.QCoreApplication.translate
        BaseUI.setWindowTitle(_translate("BaseUI", "axopy"))
        self.label.setText(_translate("BaseUI", "Existing Participants:"))
        self.listWidget.setSortingEnabled(True)
        self.newParticipantButton.setText(_translate("BaseUI", "New Participant"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.participantTab), _translate("BaseUI", "Participants"))
        self.startTaskButton.setText(_translate("BaseUI", "Start Task"))
        self.stopTaskButton.setText(_translate("BaseUI", "Stop Task"))
        self.menuFile.setTitle(_translate("BaseUI", "&File"))
        self.actionQuit.setText(_translate("BaseUI", "&Quit"))
        self.actionQuit.setShortcut(_translate("BaseUI", "Ctrl+Q"))
