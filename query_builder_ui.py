# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/epinux/Desktop/QT_APP/imagebrowser_01/HBC-browser/qtui/query_builder_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(542, 616)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/element-vector.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 516, 590))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.scrollAreaWidgetContents)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 488, 382))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.qb_pointdatasource = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qb_pointdatasource.sizePolicy().hasHeightForWidth())
        self.qb_pointdatasource.setSizePolicy(sizePolicy)
        self.qb_pointdatasource.setMaximumSize(QtCore.QSize(180, 16777215))
        self.qb_pointdatasource.setObjectName("qb_pointdatasource")
        self.horizontalLayout_2.addWidget(self.qb_pointdatasource)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 7, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.qb_histogram = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.qb_histogram.setObjectName("qb_histogram")
        self.horizontalLayout_7.addWidget(self.qb_histogram)
        self.qb_scatter2d = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.qb_scatter2d.setObjectName("qb_scatter2d")
        self.horizontalLayout_7.addWidget(self.qb_scatter2d)
        self.qb_scatter3d = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.qb_scatter3d.setObjectName("qb_scatter3d")
        self.horizontalLayout_7.addWidget(self.qb_scatter3d)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 6, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.qb_ellipsemajoraxis = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.qb_ellipsemajoraxis.setMaximumSize(QtCore.QSize(180, 16777215))
        self.qb_ellipsemajoraxis.setStyleSheet("")
        self.qb_ellipsemajoraxis.setObjectName("qb_ellipsemajoraxis")
        self.gridLayout.addWidget(self.qb_ellipsemajoraxis, 5, 1, 1, 1)
        self.qb_shapeselection = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.qb_shapeselection.setMaximumSize(QtCore.QSize(180, 16777215))
        self.qb_shapeselection.setObjectName("qb_shapeselection")
        self.qb_shapeselection.addItem("")
        self.qb_shapeselection.setItemText(0, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/ellipse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.qb_shapeselection.addItem(icon1, "")
        self.gridLayout.addWidget(self.qb_shapeselection, 4, 1, 1, 1)
        self.qb_ellipseminoraxis = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.qb_ellipseminoraxis.setMaximumSize(QtCore.QSize(180, 16777215))
        self.qb_ellipseminoraxis.setStyleSheet("")
        self.qb_ellipseminoraxis.setObjectName("qb_ellipseminoraxis")
        self.gridLayout.addWidget(self.qb_ellipseminoraxis, 6, 1, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.qb_latlabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.qb_latlabel.setMinimumSize(QtCore.QSize(100, 0))
        self.qb_latlabel.setObjectName("qb_latlabel")
        self.horizontalLayout_13.addWidget(self.qb_latlabel)
        self.qb_latitude = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.qb_latitude.setMinimumSize(QtCore.QSize(160, 0))
        self.qb_latitude.setMaximumSize(QtCore.QSize(180, 16777215))
        self.qb_latitude.setStyleSheet("")
        self.qb_latitude.setAlignment(QtCore.Qt.AlignCenter)
        self.qb_latitude.setObjectName("qb_latitude")
        self.horizontalLayout_13.addWidget(self.qb_latitude)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_13, 3, 0, 1, 3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.qb_imageindex = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.qb_imageindex.setMaximumSize(QtCore.QSize(180, 16777215))
        self.qb_imageindex.setStyleSheet("")
        self.qb_imageindex.setAlignment(QtCore.Qt.AlignCenter)
        self.qb_imageindex.setObjectName("qb_imageindex")
        self.horizontalLayout_5.addWidget(self.qb_imageindex)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 3)
        self.qb_ellipseorientation_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.qb_ellipseorientation_label.setMinimumSize(QtCore.QSize(100, 0))
        self.qb_ellipseorientation_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.qb_ellipseorientation_label.setObjectName("qb_ellipseorientation_label")
        self.gridLayout.addWidget(self.qb_ellipseorientation_label, 7, 0, 1, 1)
        self.qb_minoraxis_lablel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.qb_minoraxis_lablel.setMinimumSize(QtCore.QSize(100, 0))
        self.qb_minoraxis_lablel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.qb_minoraxis_lablel.setObjectName("qb_minoraxis_lablel")
        self.gridLayout.addWidget(self.qb_minoraxis_lablel, 6, 0, 1, 1)
        self.Iconlabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.Iconlabel.setMinimumSize(QtCore.QSize(90, 0))
        self.Iconlabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Iconlabel.setObjectName("Iconlabel")
        self.gridLayout.addWidget(self.Iconlabel, 4, 0, 1, 1)
        self.qb_majoraxis_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.qb_majoraxis_label.setMinimumSize(QtCore.QSize(100, 0))
        self.qb_majoraxis_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.qb_majoraxis_label.setObjectName("qb_majoraxis_label")
        self.gridLayout.addWidget(self.qb_majoraxis_label, 5, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.qb_ellipseorientation = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.qb_ellipseorientation.setStyleSheet("")
        self.qb_ellipseorientation.setObjectName("qb_ellipseorientation")
        self.horizontalLayout_9.addWidget(self.qb_ellipseorientation)
        self.gridLayout.addLayout(self.horizontalLayout_9, 7, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.qb_lonlabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.qb_lonlabel.setMinimumSize(QtCore.QSize(100, 0))
        self.qb_lonlabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.qb_lonlabel.setObjectName("qb_lonlabel")
        self.horizontalLayout_3.addWidget(self.qb_lonlabel)
        self.qb_longitude = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.qb_longitude.setMinimumSize(QtCore.QSize(160, 0))
        self.qb_longitude.setMaximumSize(QtCore.QSize(180, 16777215))
        self.qb_longitude.setStyleSheet("")
        self.qb_longitude.setAlignment(QtCore.Qt.AlignCenter)
        self.qb_longitude.setObjectName("qb_longitude")
        self.horizontalLayout_3.addWidget(self.qb_longitude)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 7, 2, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setMinimumSize(QtCore.QSize(100, 0))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_15.addWidget(self.label_7)
        self.qb_imagebuffer = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.qb_imagebuffer.setMinimumSize(QtCore.QSize(80, 0))
        self.qb_imagebuffer.setMaximumSize(QtCore.QSize(120, 16777215))
        self.qb_imagebuffer.setObjectName("qb_imagebuffer")
        self.horizontalLayout_15.addWidget(self.qb_imagebuffer)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_15, 1, 0, 1, 3)
        self.gridLayout_5.addLayout(self.gridLayout, 4, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addlink = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addlink.sizePolicy().hasHeightForWidth())
        self.addlink.setSizePolicy(sizePolicy)
        self.addlink.setMaximumSize(QtCore.QSize(32, 32))
        self.addlink.setStyleSheet("")
        self.addlink.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addlink.setIcon(icon2)
        self.addlink.setIconSize(QtCore.QSize(21, 21))
        self.addlink.setObjectName("addlink")
        self.horizontalLayout.addWidget(self.addlink)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.clean = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clean.sizePolicy().hasHeightForWidth())
        self.clean.setSizePolicy(sizePolicy)
        self.clean.setMaximumSize(QtCore.QSize(32, 32))
        self.clean.setStyleSheet("")
        self.clean.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clean.setIcon(icon3)
        self.clean.setIconSize(QtCore.QSize(21, 21))
        self.clean.setObjectName("clean")
        self.horizontalLayout.addWidget(self.clean)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.update = QtWidgets.QPushButton(self.groupBox_2)
        self.update.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.update.setFont(font)
        self.update.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update.setIcon(icon4)
        self.update.setIconSize(QtCore.QSize(21, 21))
        self.update.setObjectName("update")
        self.horizontalLayout.addWidget(self.update)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.groupBox_2)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout.addWidget(self.webEngineView)
        self.verticalLayout_6.addWidget(self.splitter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        self.qb_shapeselection.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Query_builder"))
        self.label.setText(_translate("Form", "Point Data Source"))
        self.label_2.setText(_translate("Form", "Plot"))
        self.qb_histogram.setText(_translate("Form", "Histogram"))
        self.qb_scatter2d.setText(_translate("Form", "Scatter 2D"))
        self.qb_scatter3d.setText(_translate("Form", "Scatter 3D"))
        self.qb_shapeselection.setItemText(1, _translate("Form", "Ellipse"))
        self.qb_latlabel.setText(_translate("Form", "Latitude"))
        self.label_6.setText(_translate("Form", "Image Index"))
        self.qb_imageindex.setText(_translate("Form", "1000"))
        self.qb_ellipseorientation_label.setText(_translate("Form", "Orientation"))
        self.qb_minoraxis_lablel.setText(_translate("Form", "Minor Axis [m]"))
        self.Iconlabel.setText(_translate("Form", "Shape"))
        self.qb_majoraxis_label.setText(_translate("Form", "Major Axis [m]"))
        self.qb_lonlabel.setText(_translate("Form", "Longitude"))
        self.label_7.setText(_translate("Form", "Image Buffer"))
        self.groupBox_2.setTitle(_translate("Form", "Output"))
from PyQt5 import QtWebEngineWidgets
import resources_rc
