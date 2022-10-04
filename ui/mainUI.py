# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UnoGenerator.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QWidget)
import ui.img_src_root_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(875, 625)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/img/pngwing.com.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setAutoFillBackground(False)
        self.actionQuit = QAction(mainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionGenerate = QAction(mainWindow)
        self.actionGenerate.setObjectName(u"actionGenerate")
        self.actionQuit_2 = QAction(mainWindow)
        self.actionQuit_2.setObjectName(u"actionQuit_2")
        self.actionOpthion = QAction(mainWindow)
        self.actionOpthion.setObjectName(u"actionOpthion")
        self.actionOpthion.setCheckable(False)
        self.actionOpthion.setEnabled(False)
        self.actionQuit_3 = QAction(mainWindow)
        self.actionQuit_3.setObjectName(u"actionQuit_3")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Extra_Config = QGroupBox(self.centralwidget)
        self.Extra_Config.setObjectName(u"Extra_Config")
        self.Extra_Config.setGeometry(QRect(17, 404, 489, 180))
        self.Extra_Config.setFlat(False)
        self.gridLayoutWidget = QWidget(self.Extra_Config)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(3, 19, 480, 152))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.CB_I2C_Enable = QCheckBox(self.gridLayoutWidget)
        self.CB_I2C_Enable.setObjectName(u"CB_I2C_Enable")

        self.gridLayout.addWidget(self.CB_I2C_Enable, 0, 3, 1, 1)

        self.CB_UART_Enable = QCheckBox(self.gridLayoutWidget)
        self.CB_UART_Enable.setObjectName(u"CB_UART_Enable")

        self.gridLayout.addWidget(self.CB_UART_Enable, 0, 4, 1, 1)

        self.CB_SPI_Enable = QCheckBox(self.gridLayoutWidget)
        self.CB_SPI_Enable.setObjectName(u"CB_SPI_Enable")

        self.gridLayout.addWidget(self.CB_SPI_Enable, 0, 0, 1, 1)

        self.Arduino_frame = QFrame(self.centralwidget)
        self.Arduino_frame.setObjectName(u"Arduino_frame")
        self.Arduino_frame.setGeometry(QRect(15, 20, 493, 369))
        self.Arduino_frame.setFrameShape(QFrame.NoFrame)
        self.Arduino_frame.setFrameShadow(QFrame.Raised)
        self.DIGITAL_PIN_9 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_9.setObjectName(u"DIGITAL_PIN_9")
        self.DIGITAL_PIN_9.setGeometry(QRect(281, 10, 14, 14))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_9.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_9.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_9.setMinimumSize(QSize(14, 0))
        self.DIGITAL_PIN_9.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_9.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_9.setIconSize(QSize(14, 14))
        self.DIGITAL_PIN_9.setCheckable(True)
        self.DIGITAL_PIN_9.setTristate(False)
        self.DIGITAL_PIN_13 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_13.setObjectName(u"DIGITAL_PIN_13")
        self.DIGITAL_PIN_13.setGeometry(QRect(218, 10, 14, 14))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_13.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_13.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_13.setMinimumSize(QSize(14, 0))
        self.DIGITAL_PIN_13.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_13.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_13.setIconSize(QSize(14, 14))
        self.DIGITAL_PIN_13.setCheckable(True)
        self.DIGITAL_PIN_13.setTristate(False)
        self.arduino_2 = QLabel(self.Arduino_frame)
        self.arduino_2.setObjectName(u"arduino_2")
        self.arduino_2.setGeometry(QRect(0, 0, 475, 336))
        self.arduino_2.setMinimumSize(QSize(475, 0))
        self.arduino_2.setTextFormat(Qt.PlainText)
        self.arduino_2.setPixmap(QPixmap(u":/img/arduino_uno.png"))
        self.arduino_2.setScaledContents(True)
        self.DIGITAL_PIN_10 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_10.setObjectName(u"DIGITAL_PIN_10")
        self.DIGITAL_PIN_10.setGeometry(QRect(266, 10, 14, 14))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_10.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_10.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_10.setMinimumSize(QSize(14, 0))
        self.DIGITAL_PIN_10.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_10.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_10.setIconSize(QSize(14, 14))
        self.DIGITAL_PIN_10.setCheckable(True)
        self.DIGITAL_PIN_10.setTristate(False)
        self.DIGITAL_PIN_2 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_2.setObjectName(u"DIGITAL_PIN_2")
        self.DIGITAL_PIN_2.setGeometry(QRect(404, 9, 16, 16))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_2.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_2.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_2.setMinimumSize(QSize(16, 0))
        self.DIGITAL_PIN_2.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_2.setCheckable(True)
        self.DIGITAL_PIN_2.setTristate(False)
        self.ANALOG_PIN_A3 = QCheckBox(self.Arduino_frame)
        self.ANALOG_PIN_A3.setObjectName(u"ANALOG_PIN_A3")
        self.ANALOG_PIN_A3.setGeometry(QRect(403, 313, 16, 16))
        sizePolicy1.setHeightForWidth(self.ANALOG_PIN_A3.sizePolicy().hasHeightForWidth())
        self.ANALOG_PIN_A3.setSizePolicy(sizePolicy1)
        self.ANALOG_PIN_A3.setMinimumSize(QSize(16, 0))
        self.ANALOG_PIN_A3.setFocusPolicy(Qt.StrongFocus)
        self.ANALOG_PIN_A3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ANALOG_PIN_A3.setCheckable(True)
        self.ANALOG_PIN_A3.setTristate(False)
        self.DIGITAL_PIN_1 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_1.setObjectName(u"DIGITAL_PIN_1")
        self.DIGITAL_PIN_1.setGeometry(QRect(419, 9, 16, 16))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_1.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_1.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_1.setMinimumSize(QSize(16, 0))
        self.DIGITAL_PIN_1.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_1.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_1.setCheckable(True)
        self.DIGITAL_PIN_1.setTristate(False)
        self.DIGITAL_PIN_8 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_8.setObjectName(u"DIGITAL_PIN_8")
        self.DIGITAL_PIN_8.setGeometry(QRect(297, 10, 14, 14))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_8.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_8.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_8.setMinimumSize(QSize(14, 0))
        self.DIGITAL_PIN_8.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_8.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_8.setIconSize(QSize(14, 14))
        self.DIGITAL_PIN_8.setCheckable(True)
        self.DIGITAL_PIN_8.setTristate(False)
        self.ANALOG_PIN_A0 = QCheckBox(self.Arduino_frame)
        self.ANALOG_PIN_A0.setObjectName(u"ANALOG_PIN_A0")
        self.ANALOG_PIN_A0.setGeometry(QRect(355, 313, 16, 16))
        sizePolicy1.setHeightForWidth(self.ANALOG_PIN_A0.sizePolicy().hasHeightForWidth())
        self.ANALOG_PIN_A0.setSizePolicy(sizePolicy1)
        self.ANALOG_PIN_A0.setMinimumSize(QSize(16, 0))
        self.ANALOG_PIN_A0.setFocusPolicy(Qt.StrongFocus)
        self.ANALOG_PIN_A0.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ANALOG_PIN_A0.setCheckable(True)
        self.ANALOG_PIN_A0.setTristate(False)
        self.DIGITAL_PIN_4 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_4.setObjectName(u"DIGITAL_PIN_4")
        self.DIGITAL_PIN_4.setGeometry(QRect(372, 9, 16, 16))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_4.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_4.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_4.setMinimumSize(QSize(16, 0))
        self.DIGITAL_PIN_4.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_4.setCheckable(True)
        self.DIGITAL_PIN_4.setTristate(False)
        self.ANALOG_PIN_A2 = QCheckBox(self.Arduino_frame)
        self.ANALOG_PIN_A2.setObjectName(u"ANALOG_PIN_A2")
        self.ANALOG_PIN_A2.setGeometry(QRect(387, 313, 16, 16))
        sizePolicy1.setHeightForWidth(self.ANALOG_PIN_A2.sizePolicy().hasHeightForWidth())
        self.ANALOG_PIN_A2.setSizePolicy(sizePolicy1)
        self.ANALOG_PIN_A2.setMinimumSize(QSize(16, 0))
        self.ANALOG_PIN_A2.setFocusPolicy(Qt.StrongFocus)
        self.ANALOG_PIN_A2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ANALOG_PIN_A2.setCheckable(True)
        self.ANALOG_PIN_A2.setTristate(False)
        self.DIGITAL_PIN_6 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_6.setObjectName(u"DIGITAL_PIN_6")
        self.DIGITAL_PIN_6.setGeometry(QRect(341, 9, 16, 16))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_6.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_6.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_6.setMinimumSize(QSize(16, 0))
        self.DIGITAL_PIN_6.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_6.setCheckable(True)
        self.DIGITAL_PIN_6.setTristate(False)
        self.DIGITAL_PIN_0 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_0.setObjectName(u"DIGITAL_PIN_0")
        self.DIGITAL_PIN_0.setGeometry(QRect(435, 9, 16, 16))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_0.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_0.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_0.setMinimumSize(QSize(16, 0))
        self.DIGITAL_PIN_0.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_0.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_0.setCheckable(True)
        self.DIGITAL_PIN_0.setTristate(False)
        self.ANALOG_PIN_A5 = QCheckBox(self.Arduino_frame)
        self.ANALOG_PIN_A5.setObjectName(u"ANALOG_PIN_A5")
        self.ANALOG_PIN_A5.setGeometry(QRect(435, 314, 14, 14))
        sizePolicy1.setHeightForWidth(self.ANALOG_PIN_A5.sizePolicy().hasHeightForWidth())
        self.ANALOG_PIN_A5.setSizePolicy(sizePolicy1)
        self.ANALOG_PIN_A5.setMinimumSize(QSize(14, 0))
        self.ANALOG_PIN_A5.setFocusPolicy(Qt.StrongFocus)
        self.ANALOG_PIN_A5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ANALOG_PIN_A5.setCheckable(True)
        self.ANALOG_PIN_A5.setTristate(False)
        self.DIGITAL_PIN_11 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_11.setObjectName(u"DIGITAL_PIN_11")
        self.DIGITAL_PIN_11.setGeometry(QRect(250, 10, 14, 14))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_11.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_11.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_11.setMinimumSize(QSize(14, 0))
        self.DIGITAL_PIN_11.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_11.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_11.setIconSize(QSize(14, 14))
        self.DIGITAL_PIN_11.setCheckable(True)
        self.DIGITAL_PIN_11.setTristate(False)
        self.DIGITAL_PIN_7 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_7.setObjectName(u"DIGITAL_PIN_7")
        self.DIGITAL_PIN_7.setGeometry(QRect(325, 9, 16, 16))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_7.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_7.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_7.setMinimumSize(QSize(16, 0))
        self.DIGITAL_PIN_7.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_7.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_7.setCheckable(True)
        self.DIGITAL_PIN_7.setTristate(False)
        self.ANALOG_PIN_A4 = QCheckBox(self.Arduino_frame)
        self.ANALOG_PIN_A4.setObjectName(u"ANALOG_PIN_A4")
        self.ANALOG_PIN_A4.setGeometry(QRect(419, 314, 14, 14))
        sizePolicy1.setHeightForWidth(self.ANALOG_PIN_A4.sizePolicy().hasHeightForWidth())
        self.ANALOG_PIN_A4.setSizePolicy(sizePolicy1)
        self.ANALOG_PIN_A4.setMinimumSize(QSize(14, 0))
        self.ANALOG_PIN_A4.setFocusPolicy(Qt.StrongFocus)
        self.ANALOG_PIN_A4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ANALOG_PIN_A4.setCheckable(True)
        self.ANALOG_PIN_A4.setTristate(False)
        self.DIGITAL_PIN_12 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_12.setObjectName(u"DIGITAL_PIN_12")
        self.DIGITAL_PIN_12.setGeometry(QRect(234, 10, 14, 14))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_12.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_12.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_12.setMinimumSize(QSize(14, 0))
        self.DIGITAL_PIN_12.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_12.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_12.setIconSize(QSize(14, 14))
        self.DIGITAL_PIN_12.setCheckable(True)
        self.DIGITAL_PIN_12.setTristate(False)
        self.DIGITAL_PIN_5 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_5.setObjectName(u"DIGITAL_PIN_5")
        self.DIGITAL_PIN_5.setGeometry(QRect(356, 9, 16, 16))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_5.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_5.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_5.setMinimumSize(QSize(16, 0))
        self.DIGITAL_PIN_5.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_5.setCheckable(True)
        self.DIGITAL_PIN_5.setTristate(False)
        self.DIGITAL_PIN_3 = QCheckBox(self.Arduino_frame)
        self.DIGITAL_PIN_3.setObjectName(u"DIGITAL_PIN_3")
        self.DIGITAL_PIN_3.setGeometry(QRect(388, 9, 16, 16))
        sizePolicy1.setHeightForWidth(self.DIGITAL_PIN_3.sizePolicy().hasHeightForWidth())
        self.DIGITAL_PIN_3.setSizePolicy(sizePolicy1)
        self.DIGITAL_PIN_3.setMinimumSize(QSize(16, 0))
        self.DIGITAL_PIN_3.setFocusPolicy(Qt.StrongFocus)
        self.DIGITAL_PIN_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.DIGITAL_PIN_3.setCheckable(True)
        self.DIGITAL_PIN_3.setTristate(False)
        self.ANALOG_PIN_A1 = QCheckBox(self.Arduino_frame)
        self.ANALOG_PIN_A1.setObjectName(u"ANALOG_PIN_A1")
        self.ANALOG_PIN_A1.setGeometry(QRect(371, 313, 16, 16))
        sizePolicy1.setHeightForWidth(self.ANALOG_PIN_A1.sizePolicy().hasHeightForWidth())
        self.ANALOG_PIN_A1.setSizePolicy(sizePolicy1)
        self.ANALOG_PIN_A1.setMinimumSize(QSize(16, 0))
        self.ANALOG_PIN_A1.setFocusPolicy(Qt.StrongFocus)
        self.ANALOG_PIN_A1.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ANALOG_PIN_A1.setCheckable(True)
        self.ANALOG_PIN_A1.setTristate(False)
        self.arduino_2.raise_()
        self.DIGITAL_PIN_9.raise_()
        self.DIGITAL_PIN_13.raise_()
        self.DIGITAL_PIN_10.raise_()
        self.DIGITAL_PIN_2.raise_()
        self.ANALOG_PIN_A3.raise_()
        self.DIGITAL_PIN_1.raise_()
        self.DIGITAL_PIN_8.raise_()
        self.ANALOG_PIN_A0.raise_()
        self.DIGITAL_PIN_4.raise_()
        self.ANALOG_PIN_A2.raise_()
        self.DIGITAL_PIN_6.raise_()
        self.DIGITAL_PIN_0.raise_()
        self.ANALOG_PIN_A5.raise_()
        self.DIGITAL_PIN_11.raise_()
        self.DIGITAL_PIN_7.raise_()
        self.ANALOG_PIN_A4.raise_()
        self.DIGITAL_PIN_12.raise_()
        self.DIGITAL_PIN_5.raise_()
        self.DIGITAL_PIN_3.raise_()
        self.ANALOG_PIN_A1.raise_()
        self.Config = QGroupBox(self.centralwidget)
        self.Config.setObjectName(u"Config")
        self.Config.setGeometry(QRect(632, 17, 227, 567))
        self.Config.setStyleSheet(u"")
        self.horizontalLayoutWidget_2 = QWidget(self.Config)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(7, 75, 213, 29))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.RADIO_INPUT = QRadioButton(self.horizontalLayoutWidget_2)
        self.RADIO_INPUT.setObjectName(u"RADIO_INPUT")

        self.horizontalLayout_2.addWidget(self.RADIO_INPUT)

        self.RADIO_OUTPUT = QRadioButton(self.horizontalLayoutWidget_2)
        self.RADIO_OUTPUT.setObjectName(u"RADIO_OUTPUT")

        self.horizontalLayout_2.addWidget(self.RADIO_OUTPUT)

        self.horizontalLayoutWidget_3 = QWidget(self.Config)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(7, 103, 213, 29))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.COMBO_INPUT_AD = QComboBox(self.horizontalLayoutWidget_3)
        self.COMBO_INPUT_AD.addItem("")
        self.COMBO_INPUT_AD.addItem("")
        self.COMBO_INPUT_AD.setObjectName(u"COMBO_INPUT_AD")

        self.horizontalLayout_3.addWidget(self.COMBO_INPUT_AD)

        self.COMBO_OUTPUT_AD = QComboBox(self.horizontalLayoutWidget_3)
        self.COMBO_OUTPUT_AD.addItem("")
        self.COMBO_OUTPUT_AD.addItem("")
        self.COMBO_OUTPUT_AD.setObjectName(u"COMBO_OUTPUT_AD")

        self.horizontalLayout_3.addWidget(self.COMBO_OUTPUT_AD)

        self.horizontalLayoutWidget_4 = QWidget(self.Config)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(7, 44, 213, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.LE_PINNAME = QLineEdit(self.horizontalLayoutWidget_4)
        self.LE_PINNAME.setObjectName(u"LE_PINNAME")

        self.horizontalLayout_4.addWidget(self.LE_PINNAME)

        self.horizontalLayoutWidget_5 = QWidget(self.Config)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(7, 16, 213, 28))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.LABEL_OBJECT = QLabel(self.horizontalLayoutWidget_5)
        self.LABEL_OBJECT.setObjectName(u"LABEL_OBJECT")
        self.LABEL_OBJECT.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.LABEL_OBJECT.setMargin(2)

        self.horizontalLayout_5.addWidget(self.LABEL_OBJECT)

        self.BUTTON_SAVE = QPushButton(self.Config)
        self.BUTTON_SAVE.setObjectName(u"BUTTON_SAVE")
        self.BUTTON_SAVE.setGeometry(QRect(148, 540, 75, 23))
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(514, 22, 111, 560))
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.setProperty("showDropIndicator", False)
        self.listView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listView.setLayoutMode(QListView.Batched)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 875, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        mainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionGenerate)
        self.menuFile.addAction(self.actionOpthion)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_3)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("mainWindow", u"Quit", None))
        self.actionGenerate.setText(QCoreApplication.translate("mainWindow", u"Generate", None))
        self.actionQuit_2.setText(QCoreApplication.translate("mainWindow", u"Quit", None))
        self.actionOpthion.setText(QCoreApplication.translate("mainWindow", u"Opthion", None))
        self.actionQuit_3.setText(QCoreApplication.translate("mainWindow", u"Quit", None))
        self.Extra_Config.setTitle(QCoreApplication.translate("mainWindow", u"Extra Config", None))
        self.CB_I2C_Enable.setText(QCoreApplication.translate("mainWindow", u"I2C Enable", None))
        self.CB_UART_Enable.setText(QCoreApplication.translate("mainWindow", u"UART Enable", None))
        self.CB_SPI_Enable.setText(QCoreApplication.translate("mainWindow", u"SPI Enable", None))
        self.DIGITAL_PIN_9.setText("")
        self.DIGITAL_PIN_13.setText("")
        self.arduino_2.setText("")
        self.DIGITAL_PIN_10.setText("")
        self.DIGITAL_PIN_2.setText("")
        self.ANALOG_PIN_A3.setText("")
        self.DIGITAL_PIN_1.setText("")
        self.DIGITAL_PIN_8.setText("")
        self.ANALOG_PIN_A0.setText("")
        self.DIGITAL_PIN_4.setText("")
        self.ANALOG_PIN_A2.setText("")
        self.DIGITAL_PIN_6.setText("")
        self.DIGITAL_PIN_0.setText("")
        self.ANALOG_PIN_A5.setText("")
        self.DIGITAL_PIN_11.setText("")
        self.DIGITAL_PIN_7.setText("")
        self.ANALOG_PIN_A4.setText("")
        self.DIGITAL_PIN_12.setText("")
        self.DIGITAL_PIN_5.setText("")
        self.DIGITAL_PIN_3.setText("")
        self.ANALOG_PIN_A1.setText("")
        self.Config.setTitle(QCoreApplication.translate("mainWindow", u"Pin Config", None))
        self.RADIO_INPUT.setText(QCoreApplication.translate("mainWindow", u"Input", None))
        self.RADIO_OUTPUT.setText(QCoreApplication.translate("mainWindow", u"Output", None))
        self.COMBO_INPUT_AD.setItemText(0, QCoreApplication.translate("mainWindow", u"Digital", None))
        self.COMBO_INPUT_AD.setItemText(1, QCoreApplication.translate("mainWindow", u"Analog", None))

        self.COMBO_OUTPUT_AD.setItemText(0, QCoreApplication.translate("mainWindow", u"Digital", None))
        self.COMBO_OUTPUT_AD.setItemText(1, QCoreApplication.translate("mainWindow", u"Analog", None))

        self.label.setText(QCoreApplication.translate("mainWindow", u"Pin Name :", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Object Name : ", None))
        self.LABEL_OBJECT.setText("")
        self.BUTTON_SAVE.setText(QCoreApplication.translate("mainWindow", u"Save", None))
        self.menuFile.setTitle(QCoreApplication.translate("mainWindow", u"File", None))
    # retranslateUi

