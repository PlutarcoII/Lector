# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw/settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1139, 612)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = SaysHelloWhenClicked(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.treeViewPage = QtWidgets.QWidget()
        self.treeViewPage.setObjectName("treeViewPage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.treeViewPage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.treeView = QtWidgets.QTreeView(self.treeViewPage)
        self.treeView.setObjectName("treeView")
        self.gridLayout_5.addWidget(self.treeView, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.treeViewPage)
        self.switchPage = QtWidgets.QWidget()
        self.switchPage.setObjectName("switchPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.switchPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.switchPage)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.readAtLabel = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readAtLabel.sizePolicy().hasHeightForWidth())
        self.readAtLabel.setSizePolicy(sizePolicy)
        self.readAtLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.readAtLabel.setObjectName("readAtLabel")
        self.horizontalLayout_14.addWidget(self.readAtLabel)
        self.readAtPercent = QtWidgets.QSpinBox(self.groupBox)
        self.readAtPercent.setMinimum(90)
        self.readAtPercent.setProperty("value", 95)
        self.readAtPercent.setObjectName("readAtPercent")
        self.horizontalLayout_14.addWidget(self.readAtPercent)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.darkIconsRadio = QtWidgets.QRadioButton(self.groupBox)
        self.darkIconsRadio.setObjectName("darkIconsRadio")
        self.horizontalLayout_7.addWidget(self.darkIconsRadio)
        self.lightIconsRadio = QtWidgets.QRadioButton(self.groupBox)
        self.lightIconsRadio.setObjectName("lightIconsRadio")
        self.horizontalLayout_7.addWidget(self.lightIconsRadio)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.refreshLibrary = QtWidgets.QCheckBox(self.groupBox)
        self.refreshLibrary.setObjectName("refreshLibrary")
        self.horizontalLayout_4.addWidget(self.refreshLibrary)
        self.fileRemember = QtWidgets.QCheckBox(self.groupBox)
        self.fileRemember.setObjectName("fileRemember")
        self.horizontalLayout_4.addWidget(self.fileRemember)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.coverShadows = QtWidgets.QCheckBox(self.groupBox)
        self.coverShadows.setObjectName("coverShadows")
        self.horizontalLayout_3.addWidget(self.coverShadows)
        self.performCulling = QtWidgets.QCheckBox(self.groupBox)
        self.performCulling.setObjectName("performCulling")
        self.horizontalLayout_3.addWidget(self.performCulling)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.autoTags = QtWidgets.QCheckBox(self.groupBox)
        self.autoTags.setObjectName("autoTags")
        self.horizontalLayout_9.addWidget(self.autoTags)
        self.attenuateTitles = QtWidgets.QCheckBox(self.groupBox)
        self.attenuateTitles.setObjectName("attenuateTitles")
        self.horizontalLayout_9.addWidget(self.attenuateTitles)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.autoCover = QtWidgets.QCheckBox(self.groupBox)
        self.autoCover.setObjectName("autoCover")
        self.horizontalLayout_16.addWidget(self.autoCover)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.switchPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.hideScrollBars = QtWidgets.QCheckBox(self.groupBox_2)
        self.hideScrollBars.setObjectName("hideScrollBars")
        self.horizontalLayout_6.addWidget(self.hideScrollBars)
        self.cachingEnabled = QtWidgets.QCheckBox(self.groupBox_2)
        self.cachingEnabled.setObjectName("cachingEnabled")
        self.horizontalLayout_6.addWidget(self.cachingEnabled)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.smallIncrementLabel = QtWidgets.QLabel(self.groupBox_2)
        self.smallIncrementLabel.setObjectName("smallIncrementLabel")
        self.horizontalLayout_15.addWidget(self.smallIncrementLabel)
        self.smallIncrementBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.smallIncrementBox.setMinimum(4)
        self.smallIncrementBox.setMaximum(10)
        self.smallIncrementBox.setProperty("value", 4)
        self.smallIncrementBox.setObjectName("smallIncrementBox")
        self.horizontalLayout_15.addWidget(self.smallIncrementBox)
        self.largeIncrementLabel = QtWidgets.QLabel(self.groupBox_2)
        self.largeIncrementLabel.setObjectName("largeIncrementLabel")
        self.horizontalLayout_15.addWidget(self.largeIncrementLabel)
        self.largeIncrementBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.largeIncrementBox.setMinimum(1)
        self.largeIncrementBox.setMaximum(10)
        self.largeIncrementBox.setProperty("value", 2)
        self.largeIncrementBox.setObjectName("largeIncrementBox")
        self.horizontalLayout_15.addWidget(self.largeIncrementBox)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_15)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.languageLabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.languageLabel.sizePolicy().hasHeightForWidth())
        self.languageLabel.setSizePolicy(sizePolicy)
        self.languageLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.languageLabel.setObjectName("languageLabel")
        self.horizontalLayout_5.addWidget(self.languageLabel)
        self.languageBox = QtWidgets.QComboBox(self.groupBox_2)
        self.languageBox.setObjectName("languageBox")
        self.horizontalLayout_5.addWidget(self.languageBox)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollSpeedLabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollSpeedLabel.sizePolicy().hasHeightForWidth())
        self.scrollSpeedLabel.setSizePolicy(sizePolicy)
        self.scrollSpeedLabel.setObjectName("scrollSpeedLabel")
        self.horizontalLayout.addWidget(self.scrollSpeedLabel)
        self.scrollSpeedSlider = QtWidgets.QSlider(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollSpeedSlider.sizePolicy().hasHeightForWidth())
        self.scrollSpeedSlider.setSizePolicy(sizePolicy)
        self.scrollSpeedSlider.setMinimum(3)
        self.scrollSpeedSlider.setMaximum(15)
        self.scrollSpeedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.scrollSpeedSlider.setObjectName("scrollSpeedSlider")
        self.horizontalLayout.addWidget(self.scrollSpeedSlider)
        self.horizontalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.switchPage)
        self.annotationsPage = QtWidgets.QWidget()
        self.annotationsPage.setObjectName("annotationsPage")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.annotationsPage)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.annotationsPage)
        self.tabWidget.setObjectName("tabWidget")
        self.textTab = QtWidgets.QWidget()
        self.textTab.setObjectName("textTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.textTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.newAnnotation = QtWidgets.QPushButton(self.textTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newAnnotation.sizePolicy().hasHeightForWidth())
        self.newAnnotation.setSizePolicy(sizePolicy)
        self.newAnnotation.setMinimumSize(QtCore.QSize(30, 0))
        self.newAnnotation.setMaximumSize(QtCore.QSize(45, 16777215))
        self.newAnnotation.setText("")
        self.newAnnotation.setObjectName("newAnnotation")
        self.verticalLayout_6.addWidget(self.newAnnotation)
        self.deleteAnnotation = QtWidgets.QPushButton(self.textTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteAnnotation.sizePolicy().hasHeightForWidth())
        self.deleteAnnotation.setSizePolicy(sizePolicy)
        self.deleteAnnotation.setMinimumSize(QtCore.QSize(30, 0))
        self.deleteAnnotation.setMaximumSize(QtCore.QSize(45, 16777215))
        self.deleteAnnotation.setText("")
        self.deleteAnnotation.setObjectName("deleteAnnotation")
        self.verticalLayout_6.addWidget(self.deleteAnnotation)
        self.editAnnotation = QtWidgets.QPushButton(self.textTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editAnnotation.sizePolicy().hasHeightForWidth())
        self.editAnnotation.setSizePolicy(sizePolicy)
        self.editAnnotation.setMinimumSize(QtCore.QSize(30, 0))
        self.editAnnotation.setMaximumSize(QtCore.QSize(45, 16777215))
        self.editAnnotation.setText("")
        self.editAnnotation.setObjectName("editAnnotation")
        self.verticalLayout_6.addWidget(self.editAnnotation)
        self.moveUp = QtWidgets.QPushButton(self.textTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moveUp.sizePolicy().hasHeightForWidth())
        self.moveUp.setSizePolicy(sizePolicy)
        self.moveUp.setMinimumSize(QtCore.QSize(30, 0))
        self.moveUp.setMaximumSize(QtCore.QSize(45, 16777215))
        self.moveUp.setText("")
        self.moveUp.setObjectName("moveUp")
        self.verticalLayout_6.addWidget(self.moveUp)
        self.moveDown = QtWidgets.QPushButton(self.textTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moveDown.sizePolicy().hasHeightForWidth())
        self.moveDown.setSizePolicy(sizePolicy)
        self.moveDown.setMinimumSize(QtCore.QSize(30, 0))
        self.moveDown.setMaximumSize(QtCore.QSize(45, 16777215))
        self.moveDown.setText("")
        self.moveDown.setObjectName("moveDown")
        self.verticalLayout_6.addWidget(self.moveDown)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_11.addLayout(self.verticalLayout_6)
        self.annotationsList = QtWidgets.QListView(self.textTab)
        self.annotationsList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.annotationsList.setProperty("showDropIndicator", False)
        self.annotationsList.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.annotationsList.setObjectName("annotationsList")
        self.horizontalLayout_11.addWidget(self.annotationsList)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.gridLayout_8.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previewView = QtWidgets.QTextBrowser(self.textTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewView.sizePolicy().hasHeightForWidth())
        self.previewView.setSizePolicy(sizePolicy)
        self.previewView.setMaximumSize(QtCore.QSize(16777215, 100))
        self.previewView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.previewView.setObjectName("previewView")
        self.horizontalLayout_2.addWidget(self.previewView)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.textTab, "")
        self.imageTab = QtWidgets.QWidget()
        self.imageTab.setObjectName("imageTab")
        self.tabWidget.addTab(self.imageTab, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.annotationsPage)
        self.aboutPage = QtWidgets.QWidget()
        self.aboutPage.setObjectName("aboutPage")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.aboutPage)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.aboutTabWidget = QtWidgets.QTabWidget(self.aboutPage)
        self.aboutTabWidget.setObjectName("aboutTabWidget")
        self.aboutTab = QtWidgets.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.aboutTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.aboutBox = QtWidgets.QTextBrowser(self.aboutTab)
        self.aboutBox.setOpenExternalLinks(True)
        self.aboutBox.setOpenLinks(False)
        self.aboutBox.setObjectName("aboutBox")
        self.gridLayout_6.addWidget(self.aboutBox, 0, 0, 1, 1)
        self.aboutTabWidget.addTab(self.aboutTab, "")
        self.logTab = QtWidgets.QWidget()
        self.logTab.setObjectName("logTab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.logTab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.logBox = QtWidgets.QPlainTextEdit(self.logTab)
        self.logBox.setObjectName("logBox")
        self.gridLayout_10.addWidget(self.logBox, 0, 0, 1, 1)
        self.aboutTabWidget.addTab(self.logTab, "")
        self.gridLayout_9.addWidget(self.aboutTabWidget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.aboutPage)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.resetButton = QtWidgets.QPushButton(Dialog)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_10.addWidget(self.resetButton)
        self.clearLogButton = QtWidgets.QPushButton(Dialog)
        self.clearLogButton.setObjectName("clearLogButton")
        self.horizontalLayout_10.addWidget(self.clearLogButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_10.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_10.addWidget(self.cancelButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.aboutTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.groupBox.setTitle(_translate("Dialog", "Library"))
        self.readAtLabel.setText(_translate("Dialog", "Consider book read at percent"))
        self.label.setToolTip(_translate("Dialog", "Restart application to see changes"))
        self.label.setText(_translate("Dialog", "Icon theme: "))
        self.darkIconsRadio.setToolTip(_translate("Dialog", "Restart application to see changes"))
        self.darkIconsRadio.setText(_translate("Dialog", "&Dark"))
        self.lightIconsRadio.setToolTip(_translate("Dialog", "Restart application to see changes"))
        self.lightIconsRadio.setText(_translate("Dialog", "L&ight"))
        self.refreshLibrary.setText(_translate("Dialog", "Startup: Refresh library"))
        self.fileRemember.setText(_translate("Dialog", "Remember open files"))
        self.coverShadows.setText(_translate("Dialog", "Cover shadows"))
        self.performCulling.setToolTip(_translate("Dialog", "Enabling reduces startup time and memory usage"))
        self.performCulling.setText(_translate("Dialog", "Load covers only when needed"))
        self.autoTags.setText(_translate("Dialog", "Generate tags from files"))
        self.attenuateTitles.setText(_translate("Dialog", "Shrink long book titles"))
        self.autoCover.setToolTip(_translate("Dialog", "<html><head/><body><p>Attempt to download missing book covers from Google books - SLOW</p></body></html>"))
        self.autoCover.setText(_translate("Dialog", "Download missing covers"))
        self.groupBox_2.setTitle(_translate("Dialog", "Reading"))
        self.hideScrollBars.setToolTip(_translate("Dialog", "Horizontal scrolling with Alt + Scroll\n"
"Reopen book to see changes"))
        self.hideScrollBars.setText(_translate("Dialog", "Hide scrollbars when reading"))
        self.cachingEnabled.setToolTip(_translate("Dialog", "Greatly reduces page transition time at the cost of more memory"))
        self.cachingEnabled.setText(_translate("Dialog", "Cache comic / pdf pages"))
        self.smallIncrementLabel.setToolTip(_translate("Dialog", "<html><head/><body><p>UP/DOWN ARROW - Steps to take before turning comicbook page</p></body></html>"))
        self.smallIncrementLabel.setText(_translate("Dialog", "Small increment"))
        self.smallIncrementBox.setToolTip(_translate("Dialog", "<html><head/><body><p>UP/DOWN ARROW - Steps to take before turning comicbook page</p></body></html>"))
        self.largeIncrementLabel.setToolTip(_translate("Dialog", "<html><head/><body><p>SPACEBAR - Steps to take before turning comicbook page</p></body></html>"))
        self.largeIncrementLabel.setText(_translate("Dialog", "Large increment"))
        self.largeIncrementBox.setToolTip(_translate("Dialog", "<html><head/><body><p>SPACEBAR - Steps to take before turning comicbook page</p></body></html>"))
        self.languageLabel.setText(_translate("Dialog", "Dictionary language"))
        self.scrollSpeedLabel.setText(_translate("Dialog", "Scroll speed"))
        self.newAnnotation.setToolTip(_translate("Dialog", "New"))
        self.deleteAnnotation.setToolTip(_translate("Dialog", "Delete"))
        self.editAnnotation.setToolTip(_translate("Dialog", "Edit"))
        self.moveUp.setToolTip(_translate("Dialog", "Move Up"))
        self.moveDown.setToolTip(_translate("Dialog", "Move Down"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.textTab), _translate("Dialog", "Text"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageTab), _translate("Dialog", "Image"))
        self.aboutTabWidget.setTabText(self.aboutTabWidget.indexOf(self.aboutTab), _translate("Dialog", "About"))
        self.aboutTabWidget.setTabText(self.aboutTabWidget.indexOf(self.logTab), _translate("Dialog", "Log"))
        self.resetButton.setText(_translate("Dialog", "Reset Application"))
        self.clearLogButton.setText(_translate("Dialog", "Clear Log"))
        self.okButton.setText(_translate("Dialog", "Scan Library"))
        self.cancelButton.setText(_translate("Dialog", "Close"))

from lector.widgets import SaysHelloWhenClicked
