# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '單形法.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        self.horizontalLayout_13 = QHBoxLayout(Form)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_13.addWidget(self.graphicsView)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.label_17)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spinBox_1 = QSpinBox(Form)
        self.spinBox_1.setObjectName(u"spinBox_1")
        sizePolicy.setHeightForWidth(self.spinBox_1.sizePolicy().hasHeightForWidth())
        self.spinBox_1.setSizePolicy(sizePolicy)
        self.spinBox_1.setReadOnly(False)
        self.spinBox_1.setMinimum(-99)

        self.horizontalLayout.addWidget(self.spinBox_1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.label_2)

        self.spinBox_2 = QSpinBox(Form)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setMinimum(-99)

        self.horizontalLayout.addWidget(self.spinBox_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.label_3)

        self.spinBox_3 = QSpinBox(Form)
        self.spinBox_3.setObjectName(u"spinBox_3")
        sizePolicy.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy)
        self.spinBox_3.setMinimum(-99)

        self.horizontalLayout.addWidget(self.spinBox_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.label_4)

        self.spinBox_4 = QSpinBox(Form)
        self.spinBox_4.setObjectName(u"spinBox_4")
        sizePolicy.setHeightForWidth(self.spinBox_4.sizePolicy().hasHeightForWidth())
        self.spinBox_4.setSizePolicy(sizePolicy)
        self.spinBox_4.setMinimum(-99)

        self.horizontalLayout.addWidget(self.spinBox_4)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.label_5)

        self.spinBox_5 = QSpinBox(Form)
        self.spinBox_5.setObjectName(u"spinBox_5")
        sizePolicy.setHeightForWidth(self.spinBox_5.sizePolicy().hasHeightForWidth())
        self.spinBox_5.setSizePolicy(sizePolicy)
        self.spinBox_5.setMinimum(-99)

        self.horizontalLayout.addWidget(self.spinBox_5)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(74, 0))

        self.horizontalLayout.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(160, 0))

        self.verticalLayout.addWidget(self.label_18)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.spinBox_11 = QSpinBox(Form)
        self.spinBox_11.setObjectName(u"spinBox_11")
        sizePolicy.setHeightForWidth(self.spinBox_11.sizePolicy().hasHeightForWidth())
        self.spinBox_11.setSizePolicy(sizePolicy)
        self.spinBox_11.setReadOnly(True)
        self.spinBox_11.setMinimum(-99)

        self.horizontalLayout_5.addWidget(self.spinBox_11)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.label_12)

        self.spinBox_12 = QSpinBox(Form)
        self.spinBox_12.setObjectName(u"spinBox_12")
        sizePolicy.setHeightForWidth(self.spinBox_12.sizePolicy().hasHeightForWidth())
        self.spinBox_12.setSizePolicy(sizePolicy)
        self.spinBox_12.setReadOnly(True)
        self.spinBox_12.setMinimum(-99)

        self.horizontalLayout_5.addWidget(self.spinBox_12)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.label_13)

        self.spinBox_13 = QSpinBox(Form)
        self.spinBox_13.setObjectName(u"spinBox_13")
        sizePolicy.setHeightForWidth(self.spinBox_13.sizePolicy().hasHeightForWidth())
        self.spinBox_13.setSizePolicy(sizePolicy)
        self.spinBox_13.setReadOnly(True)
        self.spinBox_13.setMinimum(-99)

        self.horizontalLayout_5.addWidget(self.spinBox_13)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.label_14)

        self.spinBox_14 = QSpinBox(Form)
        self.spinBox_14.setObjectName(u"spinBox_14")
        sizePolicy.setHeightForWidth(self.spinBox_14.sizePolicy().hasHeightForWidth())
        self.spinBox_14.setSizePolicy(sizePolicy)
        self.spinBox_14.setReadOnly(True)
        self.spinBox_14.setMinimum(-99)

        self.horizontalLayout_5.addWidget(self.spinBox_14)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.label_15)

        self.spinBox_15 = QSpinBox(Form)
        self.spinBox_15.setObjectName(u"spinBox_15")
        sizePolicy.setHeightForWidth(self.spinBox_15.sizePolicy().hasHeightForWidth())
        self.spinBox_15.setSizePolicy(sizePolicy)
        self.spinBox_15.setReadOnly(True)
        self.spinBox_15.setMinimum(-99)

        self.horizontalLayout_5.addWidget(self.spinBox_15)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.label_16)

        self.spinBox_16 = QSpinBox(Form)
        self.spinBox_16.setObjectName(u"spinBox_16")
        sizePolicy.setHeightForWidth(self.spinBox_16.sizePolicy().hasHeightForWidth())
        self.spinBox_16.setSizePolicy(sizePolicy)
        self.spinBox_16.setReadOnly(True)
        self.spinBox_16.setMinimum(-99)

        self.horizontalLayout_5.addWidget(self.spinBox_16)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.spinBox_17 = QSpinBox(Form)
        self.spinBox_17.setObjectName(u"spinBox_17")
        sizePolicy.setHeightForWidth(self.spinBox_17.sizePolicy().hasHeightForWidth())
        self.spinBox_17.setSizePolicy(sizePolicy)
        self.spinBox_17.setReadOnly(True)
        self.spinBox_17.setMinimum(-99)

        self.horizontalLayout_7.addWidget(self.spinBox_17)

        self.label_19 = QLabel(Form)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.label_19)

        self.spinBox_18 = QSpinBox(Form)
        self.spinBox_18.setObjectName(u"spinBox_18")
        sizePolicy.setHeightForWidth(self.spinBox_18.sizePolicy().hasHeightForWidth())
        self.spinBox_18.setSizePolicy(sizePolicy)
        self.spinBox_18.setReadOnly(True)
        self.spinBox_18.setMinimum(-99)

        self.horizontalLayout_7.addWidget(self.spinBox_18)

        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.label_20)

        self.spinBox_19 = QSpinBox(Form)
        self.spinBox_19.setObjectName(u"spinBox_19")
        sizePolicy.setHeightForWidth(self.spinBox_19.sizePolicy().hasHeightForWidth())
        self.spinBox_19.setSizePolicy(sizePolicy)
        self.spinBox_19.setReadOnly(True)
        self.spinBox_19.setMinimum(-99)

        self.horizontalLayout_7.addWidget(self.spinBox_19)

        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.label_21)

        self.spinBox_20 = QSpinBox(Form)
        self.spinBox_20.setObjectName(u"spinBox_20")
        sizePolicy.setHeightForWidth(self.spinBox_20.sizePolicy().hasHeightForWidth())
        self.spinBox_20.setSizePolicy(sizePolicy)
        self.spinBox_20.setReadOnly(True)
        self.spinBox_20.setMinimum(-99)

        self.horizontalLayout_7.addWidget(self.spinBox_20)

        self.label_22 = QLabel(Form)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.label_22)

        self.spinBox_21 = QSpinBox(Form)
        self.spinBox_21.setObjectName(u"spinBox_21")
        sizePolicy.setHeightForWidth(self.spinBox_21.sizePolicy().hasHeightForWidth())
        self.spinBox_21.setSizePolicy(sizePolicy)
        self.spinBox_21.setReadOnly(True)
        self.spinBox_21.setMinimum(-99)

        self.horizontalLayout_7.addWidget(self.spinBox_21)

        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.label_23)

        self.spinBox_22 = QSpinBox(Form)
        self.spinBox_22.setObjectName(u"spinBox_22")
        sizePolicy.setHeightForWidth(self.spinBox_22.sizePolicy().hasHeightForWidth())
        self.spinBox_22.setSizePolicy(sizePolicy)
        self.spinBox_22.setReadOnly(True)
        self.spinBox_22.setMinimum(-99)

        self.horizontalLayout_7.addWidget(self.spinBox_22)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.spinBox_23 = QSpinBox(Form)
        self.spinBox_23.setObjectName(u"spinBox_23")
        sizePolicy.setHeightForWidth(self.spinBox_23.sizePolicy().hasHeightForWidth())
        self.spinBox_23.setSizePolicy(sizePolicy)
        self.spinBox_23.setReadOnly(True)
        self.spinBox_23.setMinimum(-99)

        self.horizontalLayout_8.addWidget(self.spinBox_23)

        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.label_24)

        self.spinBox_24 = QSpinBox(Form)
        self.spinBox_24.setObjectName(u"spinBox_24")
        sizePolicy.setHeightForWidth(self.spinBox_24.sizePolicy().hasHeightForWidth())
        self.spinBox_24.setSizePolicy(sizePolicy)
        self.spinBox_24.setReadOnly(True)
        self.spinBox_24.setMinimum(-99)

        self.horizontalLayout_8.addWidget(self.spinBox_24)

        self.label_25 = QLabel(Form)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.label_25)

        self.spinBox_25 = QSpinBox(Form)
        self.spinBox_25.setObjectName(u"spinBox_25")
        sizePolicy.setHeightForWidth(self.spinBox_25.sizePolicy().hasHeightForWidth())
        self.spinBox_25.setSizePolicy(sizePolicy)
        self.spinBox_25.setReadOnly(True)
        self.spinBox_25.setMinimum(-99)

        self.horizontalLayout_8.addWidget(self.spinBox_25)

        self.label_26 = QLabel(Form)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.label_26)

        self.spinBox_26 = QSpinBox(Form)
        self.spinBox_26.setObjectName(u"spinBox_26")
        sizePolicy.setHeightForWidth(self.spinBox_26.sizePolicy().hasHeightForWidth())
        self.spinBox_26.setSizePolicy(sizePolicy)
        self.spinBox_26.setReadOnly(True)
        self.spinBox_26.setMinimum(-99)

        self.horizontalLayout_8.addWidget(self.spinBox_26)

        self.label_27 = QLabel(Form)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.label_27)

        self.spinBox_27 = QSpinBox(Form)
        self.spinBox_27.setObjectName(u"spinBox_27")
        sizePolicy.setHeightForWidth(self.spinBox_27.sizePolicy().hasHeightForWidth())
        self.spinBox_27.setSizePolicy(sizePolicy)
        self.spinBox_27.setReadOnly(True)
        self.spinBox_27.setMinimum(-99)

        self.horizontalLayout_8.addWidget(self.spinBox_27)

        self.label_28 = QLabel(Form)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.label_28)

        self.spinBox_28 = QSpinBox(Form)
        self.spinBox_28.setObjectName(u"spinBox_28")
        sizePolicy.setHeightForWidth(self.spinBox_28.sizePolicy().hasHeightForWidth())
        self.spinBox_28.setSizePolicy(sizePolicy)
        self.spinBox_28.setReadOnly(True)
        self.spinBox_28.setMinimum(-99)

        self.horizontalLayout_8.addWidget(self.spinBox_28)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.spinBox_29 = QSpinBox(Form)
        self.spinBox_29.setObjectName(u"spinBox_29")
        sizePolicy.setHeightForWidth(self.spinBox_29.sizePolicy().hasHeightForWidth())
        self.spinBox_29.setSizePolicy(sizePolicy)
        self.spinBox_29.setReadOnly(True)
        self.spinBox_29.setMinimum(-99)

        self.horizontalLayout_9.addWidget(self.spinBox_29)

        self.label_29 = QLabel(Form)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.label_29)

        self.spinBox_30 = QSpinBox(Form)
        self.spinBox_30.setObjectName(u"spinBox_30")
        sizePolicy.setHeightForWidth(self.spinBox_30.sizePolicy().hasHeightForWidth())
        self.spinBox_30.setSizePolicy(sizePolicy)
        self.spinBox_30.setReadOnly(True)
        self.spinBox_30.setMinimum(-99)

        self.horizontalLayout_9.addWidget(self.spinBox_30)

        self.label_30 = QLabel(Form)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.label_30)

        self.spinBox_31 = QSpinBox(Form)
        self.spinBox_31.setObjectName(u"spinBox_31")
        sizePolicy.setHeightForWidth(self.spinBox_31.sizePolicy().hasHeightForWidth())
        self.spinBox_31.setSizePolicy(sizePolicy)
        self.spinBox_31.setReadOnly(True)
        self.spinBox_31.setMinimum(-99)

        self.horizontalLayout_9.addWidget(self.spinBox_31)

        self.label_31 = QLabel(Form)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.label_31)

        self.spinBox_32 = QSpinBox(Form)
        self.spinBox_32.setObjectName(u"spinBox_32")
        sizePolicy.setHeightForWidth(self.spinBox_32.sizePolicy().hasHeightForWidth())
        self.spinBox_32.setSizePolicy(sizePolicy)
        self.spinBox_32.setReadOnly(True)
        self.spinBox_32.setMinimum(-99)

        self.horizontalLayout_9.addWidget(self.spinBox_32)

        self.label_32 = QLabel(Form)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.label_32)

        self.spinBox_33 = QSpinBox(Form)
        self.spinBox_33.setObjectName(u"spinBox_33")
        sizePolicy.setHeightForWidth(self.spinBox_33.sizePolicy().hasHeightForWidth())
        self.spinBox_33.setSizePolicy(sizePolicy)
        self.spinBox_33.setReadOnly(True)
        self.spinBox_33.setMinimum(-99)

        self.horizontalLayout_9.addWidget(self.spinBox_33)

        self.label_33 = QLabel(Form)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.label_33)

        self.spinBox_34 = QSpinBox(Form)
        self.spinBox_34.setObjectName(u"spinBox_34")
        sizePolicy.setHeightForWidth(self.spinBox_34.sizePolicy().hasHeightForWidth())
        self.spinBox_34.setSizePolicy(sizePolicy)
        self.spinBox_34.setReadOnly(True)
        self.spinBox_34.setMinimum(-99)

        self.horizontalLayout_9.addWidget(self.spinBox_34)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.spinBox_35 = QSpinBox(Form)
        self.spinBox_35.setObjectName(u"spinBox_35")
        sizePolicy.setHeightForWidth(self.spinBox_35.sizePolicy().hasHeightForWidth())
        self.spinBox_35.setSizePolicy(sizePolicy)
        self.spinBox_35.setReadOnly(True)
        self.spinBox_35.setMinimum(-99)

        self.horizontalLayout_10.addWidget(self.spinBox_35)

        self.label_34 = QLabel(Form)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.label_34)

        self.spinBox_36 = QSpinBox(Form)
        self.spinBox_36.setObjectName(u"spinBox_36")
        sizePolicy.setHeightForWidth(self.spinBox_36.sizePolicy().hasHeightForWidth())
        self.spinBox_36.setSizePolicy(sizePolicy)
        self.spinBox_36.setReadOnly(True)
        self.spinBox_36.setMinimum(-99)

        self.horizontalLayout_10.addWidget(self.spinBox_36)

        self.label_35 = QLabel(Form)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.label_35)

        self.spinBox_37 = QSpinBox(Form)
        self.spinBox_37.setObjectName(u"spinBox_37")
        sizePolicy.setHeightForWidth(self.spinBox_37.sizePolicy().hasHeightForWidth())
        self.spinBox_37.setSizePolicy(sizePolicy)
        self.spinBox_37.setReadOnly(True)
        self.spinBox_37.setMinimum(-99)

        self.horizontalLayout_10.addWidget(self.spinBox_37)

        self.label_36 = QLabel(Form)
        self.label_36.setObjectName(u"label_36")
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.label_36)

        self.spinBox_38 = QSpinBox(Form)
        self.spinBox_38.setObjectName(u"spinBox_38")
        sizePolicy.setHeightForWidth(self.spinBox_38.sizePolicy().hasHeightForWidth())
        self.spinBox_38.setSizePolicy(sizePolicy)
        self.spinBox_38.setReadOnly(True)
        self.spinBox_38.setMinimum(-99)

        self.horizontalLayout_10.addWidget(self.spinBox_38)

        self.label_37 = QLabel(Form)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.label_37)

        self.spinBox_39 = QSpinBox(Form)
        self.spinBox_39.setObjectName(u"spinBox_39")
        sizePolicy.setHeightForWidth(self.spinBox_39.sizePolicy().hasHeightForWidth())
        self.spinBox_39.setSizePolicy(sizePolicy)
        self.spinBox_39.setReadOnly(True)
        self.spinBox_39.setMinimum(-99)

        self.horizontalLayout_10.addWidget(self.spinBox_39)

        self.label_38 = QLabel(Form)
        self.label_38.setObjectName(u"label_38")
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.label_38)

        self.spinBox_40 = QSpinBox(Form)
        self.spinBox_40.setObjectName(u"spinBox_40")
        sizePolicy.setHeightForWidth(self.spinBox_40.sizePolicy().hasHeightForWidth())
        self.spinBox_40.setSizePolicy(sizePolicy)
        self.spinBox_40.setReadOnly(True)
        self.spinBox_40.setMinimum(-99)

        self.horizontalLayout_10.addWidget(self.spinBox_40)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.spinBox_41 = QSpinBox(Form)
        self.spinBox_41.setObjectName(u"spinBox_41")
        sizePolicy.setHeightForWidth(self.spinBox_41.sizePolicy().hasHeightForWidth())
        self.spinBox_41.setSizePolicy(sizePolicy)
        self.spinBox_41.setReadOnly(True)
        self.spinBox_41.setMinimum(-99)

        self.horizontalLayout_11.addWidget(self.spinBox_41)

        self.label_39 = QLabel(Form)
        self.label_39.setObjectName(u"label_39")
        sizePolicy.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy)
        self.label_39.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_11.addWidget(self.label_39)

        self.spinBox_42 = QSpinBox(Form)
        self.spinBox_42.setObjectName(u"spinBox_42")
        sizePolicy.setHeightForWidth(self.spinBox_42.sizePolicy().hasHeightForWidth())
        self.spinBox_42.setSizePolicy(sizePolicy)
        self.spinBox_42.setReadOnly(True)
        self.spinBox_42.setMinimum(-99)

        self.horizontalLayout_11.addWidget(self.spinBox_42)

        self.label_40 = QLabel(Form)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_11.addWidget(self.label_40)

        self.spinBox_43 = QSpinBox(Form)
        self.spinBox_43.setObjectName(u"spinBox_43")
        sizePolicy.setHeightForWidth(self.spinBox_43.sizePolicy().hasHeightForWidth())
        self.spinBox_43.setSizePolicy(sizePolicy)
        self.spinBox_43.setReadOnly(True)
        self.spinBox_43.setMinimum(-99)

        self.horizontalLayout_11.addWidget(self.spinBox_43)

        self.label_41 = QLabel(Form)
        self.label_41.setObjectName(u"label_41")
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_11.addWidget(self.label_41)

        self.spinBox_44 = QSpinBox(Form)
        self.spinBox_44.setObjectName(u"spinBox_44")
        sizePolicy.setHeightForWidth(self.spinBox_44.sizePolicy().hasHeightForWidth())
        self.spinBox_44.setSizePolicy(sizePolicy)
        self.spinBox_44.setReadOnly(True)
        self.spinBox_44.setMinimum(-99)

        self.horizontalLayout_11.addWidget(self.spinBox_44)

        self.label_42 = QLabel(Form)
        self.label_42.setObjectName(u"label_42")
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        self.label_42.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_11.addWidget(self.label_42)

        self.spinBox_45 = QSpinBox(Form)
        self.spinBox_45.setObjectName(u"spinBox_45")
        sizePolicy.setHeightForWidth(self.spinBox_45.sizePolicy().hasHeightForWidth())
        self.spinBox_45.setSizePolicy(sizePolicy)
        self.spinBox_45.setReadOnly(True)
        self.spinBox_45.setMinimum(-99)

        self.horizontalLayout_11.addWidget(self.spinBox_45)

        self.label_43 = QLabel(Form)
        self.label_43.setObjectName(u"label_43")
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        self.label_43.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_11.addWidget(self.label_43)

        self.spinBox_46 = QSpinBox(Form)
        self.spinBox_46.setObjectName(u"spinBox_46")
        sizePolicy.setHeightForWidth(self.spinBox_46.sizePolicy().hasHeightForWidth())
        self.spinBox_46.setSizePolicy(sizePolicy)
        self.spinBox_46.setReadOnly(True)
        self.spinBox_46.setMinimum(-99)

        self.horizontalLayout_11.addWidget(self.spinBox_46)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.spinBox_47 = QSpinBox(Form)
        self.spinBox_47.setObjectName(u"spinBox_47")
        sizePolicy.setHeightForWidth(self.spinBox_47.sizePolicy().hasHeightForWidth())
        self.spinBox_47.setSizePolicy(sizePolicy)
        self.spinBox_47.setReadOnly(True)
        self.spinBox_47.setMinimum(-99)

        self.horizontalLayout_12.addWidget(self.spinBox_47)

        self.label_44 = QLabel(Form)
        self.label_44.setObjectName(u"label_44")
        sizePolicy.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy)
        self.label_44.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_12.addWidget(self.label_44)

        self.spinBox_48 = QSpinBox(Form)
        self.spinBox_48.setObjectName(u"spinBox_48")
        sizePolicy.setHeightForWidth(self.spinBox_48.sizePolicy().hasHeightForWidth())
        self.spinBox_48.setSizePolicy(sizePolicy)
        self.spinBox_48.setReadOnly(True)
        self.spinBox_48.setMinimum(-99)

        self.horizontalLayout_12.addWidget(self.spinBox_48)

        self.label_45 = QLabel(Form)
        self.label_45.setObjectName(u"label_45")
        sizePolicy.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy)
        self.label_45.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_12.addWidget(self.label_45)

        self.spinBox_49 = QSpinBox(Form)
        self.spinBox_49.setObjectName(u"spinBox_49")
        sizePolicy.setHeightForWidth(self.spinBox_49.sizePolicy().hasHeightForWidth())
        self.spinBox_49.setSizePolicy(sizePolicy)
        self.spinBox_49.setReadOnly(True)
        self.spinBox_49.setMinimum(-99)

        self.horizontalLayout_12.addWidget(self.spinBox_49)

        self.label_46 = QLabel(Form)
        self.label_46.setObjectName(u"label_46")
        sizePolicy.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        self.label_46.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_12.addWidget(self.label_46)

        self.spinBox_50 = QSpinBox(Form)
        self.spinBox_50.setObjectName(u"spinBox_50")
        sizePolicy.setHeightForWidth(self.spinBox_50.sizePolicy().hasHeightForWidth())
        self.spinBox_50.setSizePolicy(sizePolicy)
        self.spinBox_50.setReadOnly(True)
        self.spinBox_50.setMinimum(-99)

        self.horizontalLayout_12.addWidget(self.spinBox_50)

        self.label_47 = QLabel(Form)
        self.label_47.setObjectName(u"label_47")
        sizePolicy.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy)
        self.label_47.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_12.addWidget(self.label_47)

        self.spinBox_51 = QSpinBox(Form)
        self.spinBox_51.setObjectName(u"spinBox_51")
        sizePolicy.setHeightForWidth(self.spinBox_51.sizePolicy().hasHeightForWidth())
        self.spinBox_51.setSizePolicy(sizePolicy)
        self.spinBox_51.setReadOnly(True)
        self.spinBox_51.setMinimum(-99)

        self.horizontalLayout_12.addWidget(self.spinBox_51)

        self.label_48 = QLabel(Form)
        self.label_48.setObjectName(u"label_48")
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        self.label_48.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_12.addWidget(self.label_48)

        self.spinBox_52 = QSpinBox(Form)
        self.spinBox_52.setObjectName(u"spinBox_52")
        sizePolicy.setHeightForWidth(self.spinBox_52.sizePolicy().hasHeightForWidth())
        self.spinBox_52.setSizePolicy(sizePolicy)
        self.spinBox_52.setReadOnly(True)
        self.spinBox_52.setMinimum(-99)

        self.horizontalLayout_12.addWidget(self.spinBox_52)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.radioButton_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(395, 80))
        font = QFont()
        font.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font.setPointSize(13)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)


        self.horizontalLayout_13.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u51fd\u5f0f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"a+", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"b+", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"c+", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"d+", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"e  =  M", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u9650\u5236 ( a, b, c, d ,e >= 0 )", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"a+", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"b+", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"c+", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"d+", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"e <=", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"a+", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"b+", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"c+", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"d+", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"e <=", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"a+", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"b+", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"c+", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"d+", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"e <=", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"a+", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"b+", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"c+", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"d+", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"e <=", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"a+", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"b+", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"c+", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"d+", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"e <=", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"a+", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"b+", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"c+", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"d+", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"e <=", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"a+", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"b+", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"c+", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"d+", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"e <=", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u6c42\u6700\u5927\u503c", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u6c42\u6700\u5c0f\u503c", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u57f7\u884c", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u76f4\u63a5\u5448\u73fe\u7d50\u679c", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u9019\u88e1\u662f\u8a0a\u606f\u6846", None))
    # retranslateUi

