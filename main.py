import sys
import itertools

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem

from ui.mainUI import Ui_mainWindow


class MainWindow(QMainWindow, Ui_mainWindow):
    listViewModel = QStandardItemModel(0, 0)

    AllPinDictList = []

    DigitalPinList = []
    AnalogPinList = []

    PinConfigList = []
    ExtraConfigList = []

    selected_dict = {}

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.init()
        self.setEvent()

    def init(self) -> None:
        """
        init 함수
        :return:
        """
        self.DigitalPinList = [
            self.DIGITAL_PIN_0,
            self.DIGITAL_PIN_1,
            self.DIGITAL_PIN_2,
            self.DIGITAL_PIN_3,
            self.DIGITAL_PIN_4,
            self.DIGITAL_PIN_5,
            self.DIGITAL_PIN_6,
            self.DIGITAL_PIN_7,
            self.DIGITAL_PIN_8,
            self.DIGITAL_PIN_9,
            self.DIGITAL_PIN_10,
            self.DIGITAL_PIN_11,
            self.DIGITAL_PIN_12,
            self.DIGITAL_PIN_13,
        ]

        self.AnalogPinList = [
            self.ANALOG_PIN_A0,
            self.ANALOG_PIN_A1,
            self.ANALOG_PIN_A2,
            self.ANALOG_PIN_A3,
            self.ANALOG_PIN_A4,
            self.ANALOG_PIN_A5,
        ]

        self.PinConfigList = [
            self.LE_PINNAME,
            self.RADIO_INPUT,
            self.RADIO_OUTPUT,
            self.COMBO_INPUT_AD,
            self.COMBO_OUTPUT_AD,
            self.BUTTON_SAVE,
            self.LABEL_OBJECT
        ]

        self.ExtraConfigList = [
            self.CB_SPI_Enable,
            self.CB_UART_Enable,
            self.CB_I2C_Enable,
        ]

        default_state = {
            "PinState": 0,
            "PinMode": 0,
            "PinType": 0,
            "PinID": '',
            "PinName": '',
        }

        # dict 형태로 state, mode, type, ID, Name 저장
        cnt = 0
        for i in self.DigitalPinList:
            var_name = "self." + i.objectName() + "_DICT"
            command = var_name + " = dict(itertools.islice(default_state.items(), 3))\n"
            command += var_name + "[\"PinID\"] = \'" + str(cnt) + "\'\n"
            command += var_name + "[\"PinName\"] = \"" + i.objectName() + "\"\n"
            command += "self.AllPinDictList.append(" + var_name + ")"
            exec(command)

            cnt += 1

        cnt = 0
        for i in self.AnalogPinList:
            var_name = "self." + i.objectName() + "_DICT"
            command = var_name + " = dict(itertools.islice(default_state.items(), 3))\n"
            command += var_name + "[\"PinID\"] = \'A" + str(cnt) + "\'\n"
            command += var_name + "[\"PinName\"] = \"" + i.objectName() + "\"\n"
            command += "self.AllPinDictList.append(" + var_name + ")"
            exec(command)

            cnt += 1

        # Test code
        # for i in range(0, 14):
        #     command = "print(self.DIGITAL_PIN_" + str(i) + "_DICT)"
        #     exec(command)
        #
        # for i in range(0, 6):
        #     command = "print(self.ANALOG_PIN_A" + str(i) + "_DICT)"
        #     exec(command)
        # Test code end

        # Config 기본상태: Disable
        self.Config.setEnabled(0)

        for i in self.PinConfigList:
            i.setEnabled(0)

    def setEvent(self) -> None:
        """
        widget에 Event를 할당 해주는 함수
        :return:
        """
        for i in self.DigitalPinList:
            i.toggled.connect(self.PinCheckBoxEventHandler)

        for i in self.AnalogPinList:
            i.toggled.connect(self.PinCheckBoxEventHandler)

        self.RADIO_OUTPUT.toggled.connect(self.PinConfigClickedHandler)
        self.RADIO_INPUT.toggled.connect(self.PinConfigClickedHandler)

        self.listView.clicked.connect(self.ListViewClickEventHandler)
        self.BUTTON_SAVE.clicked.connect(self.PinSaveButtonEventHandler)

        self.actionGenerate.triggered.connect(self.GenerateArduinoCode)
        self.actionQuit_3.triggered.connect(self.ExitApp)

    def ExitApp(self) -> None:
        QCoreApplication.instance().quit()

    def PinCheckBoxEventHandler(self) -> None:
        """
        Pin Check 박스 에빈트 핸들러
        :return:
        """
        self.deleteItemToListView()
        self.PinStateCheck()
        self.listView.setModel(self.listViewModel)

    def PinStateCheck(self) -> None:
        for i in self.DigitalPinList:
            if not i.isChecked():
                command = "self." + i.objectName() + "_DICT[\"PinState\"] = 0\n"
                command += "self." + i.objectName() + "_DICT[\"PinMode\"] = 0\n"
                command += "self." + i.objectName() + "_DICT[\"PinType\"] = 0\n"
                command += "self." + i.objectName() + "_DICT[\"PinName\"] = \"" + i.objectName() + "\"\n"
                exec(command)

        for i in self.AnalogPinList:
            if not i.isChecked():
                command = "self." + i.objectName() + "_DICT[\"PinState\"] = 0\n"
                command += "self." + i.objectName() + "_DICT[\"PinMode\"] = 0\n"
                command += "self." + i.objectName() + "_DICT[\"PinType\"] = 0\n"
                command += "self." + i.objectName() + "_DICT[\"PinName\"] = \"" + i.objectName() + "\"\n"
                exec(command)

    def appendItemToListView(self) -> None:
        """
        체크한 Pin을 리스트뷰에 올려주는 함수
        :return:
        """
        for i in self.DigitalPinList:
            if i.isChecked():
                self.listViewModel.appendRow(QStandardItem(i.objectName()))

        for i in self.AnalogPinList:
            if i.isChecked():
                self.listViewModel.appendRow(QStandardItem(i.objectName()))

    def deleteItemToListView(self) -> None:
        """
        체크 해제한 Pin을 리스트뷰에서 지우는 함수
        Delete 함수가 없기 때문에, clear (초기화) 후 다시 리스트뷰에 아이템을 올림
        :return:
        """
        self.listViewModel.clear()
        self.appendItemToListView()

    def ListViewClickEventHandler(self) -> None:
        """
        ListView에서 아이템을 클릭했을 때의 헨들러
        :return:
        """
        items = self.listView.selectedIndexes()

        for i in items:
            # Test code
            # print(i.row(), i.data())
            # Test code end
            item = i.data()

        command = "self." + item + "_DICT[\"PinState\"] = 1"
        exec(command)

        command = "self.CheckPinConfig(self." + item + "_DICT)"
        exec(command)

    def CheckPinConfig(self, pin_config: dict, Handler=True) -> None:
        """
        Pin 을 확인
        그 Pin에서 사용할 수 있는
        :return:
        """
        self.selected_dict = pin_config

        if pin_config["PinState"]:
            self.Config.setEnabled(1)
            self.LABEL_OBJECT.setEnabled(1)
            self.LE_PINNAME.setEnabled(1)
            self.RADIO_OUTPUT.setEnabled(1)
            self.RADIO_INPUT.setEnabled(1)
            self.BUTTON_SAVE.setEnabled(1)
        else:
            self.Config.setEnabled(0)
            self.LABEL_OBJECT.setText('')
            self.LE_PINNAME.setText('')
            for i in self.PinConfigList:
                i.setEnabled(0)
            return

        if "A" in pin_config["PinID"] and self.RADIO_INPUT.isChecked():
            obj_name = "ANALOG_PIN_" + pin_config["PinID"]
            self.COMBO_INPUT_AD.setEnabled(1)
        else:
            obj_name = "DIGITAL_PIN_" + pin_config["PinID"]
            self.COMBO_INPUT_AD.setEnabled(0)

        if Handler:
            self.RADIO_INPUT.setChecked(1)
            self.COMBO_OUTPUT_AD.setCurrentIndex(0)
            self.COMBO_INPUT_AD.setCurrentIndex(0)

            if not pin_config["PinMode"]:
                self.RADIO_INPUT.setChecked(1)

                if not pin_config["PinType"]:
                    self.COMBO_INPUT_AD.setCurrentIndex(0)
                else:
                    self.COMBO_INPUT_AD.setCurrentIndex(1)
            else:
                self.RADIO_OUTPUT.setChecked(1)

                if not pin_config["PinType"]:
                    self.COMBO_OUTPUT_AD.setCurrentIndex(0)
                else:
                    self.COMBO_OUTPUT_AD.setCurrentIndex(1)

            self.LABEL_OBJECT.setText(obj_name)
            self.LE_PINNAME.setText(pin_config["PinName"])

        if (
            pin_config["PinID"] == '3' or pin_config["PinID"] == '5' or pin_config["PinID"] == '6' or
            pin_config["PinID"] == '9' or pin_config["PinID"] == '10' or pin_config["PinID"] == '11'
        ) and self.RADIO_OUTPUT.isChecked():
            self.COMBO_OUTPUT_AD.setEnabled(1)
        else:
            self.COMBO_OUTPUT_AD.setEnabled(0)

    def PinConfigClickedHandler(self) -> None:
        self.CheckPinConfig(self.selected_dict, False)

    def PinSaveButtonEventHandler(self) -> None:
        if not self.LE_PINNAME.text().isspace():
            self.selected_dict["PinName"] = self.LE_PINNAME.text()

        if self.RADIO_INPUT.isChecked():
            self.selected_dict["PinMode"] = 0

            if self.COMBO_INPUT_AD.currentText() == "Digital":
                self.selected_dict["PinType"] = 0
            else:
                self.selected_dict["PinType"] = 1

        elif self.RADIO_OUTPUT.isChecked():
            self.selected_dict["PinMode"] = 1

            if self.COMBO_OUTPUT_AD.currentText() == "Digital":
                self.selected_dict["PinType"] = 0
            else:
                self.selected_dict["PinType"] = 1

        print(self.selected_dict)
        self.Config.setEnabled(0)
        self.LABEL_OBJECT.setText('')
        self.LE_PINNAME.setText('')
        for i in self.PinConfigList:
            i.setEnabled(0)

    def GenerateArduinoCode(self) -> None:
        file = open("./arduino_setup_src.c", 'w')

        self.GenerateArduinoCode_Write_Define(file)
        self.GenerateArduinoCode_Write_Setup(file)
        self.GenerateArduinoCode_Write_Loop(file)

        file.close()

    def GenerateArduinoCode_Write_Define(self, file) -> None:
        command = "/* Generated User Define with UnoGenerator */\n"
        file.write(command)

        for i in self.AllPinDictList:
            if i["PinState"]:
                command = "#define " + i["PinName"] + " " + i["PinID"] + "\n"
                file.write(command)

        command = "/* User Define End */\n\n"
        file.write(command)

    def GenerateArduinoCode_Write_Setup(self, file):
        command = "void setup() {\n"
        file.write(command)

        command = "/* Generated User Pin Initialize with UnoGenerator */\n"
        file.write(command)

        for i in self.AllPinDictList:
            if i["PinState"]:
                if not i["PinMode"]:
                    command = "  pinMode(" + i["PinName"] + ", INPUT);\n"
                    file.write(command)

        file.write("\n")

        for i in self.AllPinDictList:
            if i["PinState"]:
                if i["PinMode"]:
                    command = "  pinMode(" + i["PinName"] + ", OUTPUT);\n"
                    file.write(command)

        command = "/* User Pin Initialize End */\n\n}\n\n"
        file.write(command)

    def GenerateArduinoCode_Write_Loop(self, file):
        command = 'void loop() {\n'
        command += "/* Generated Example Code with UnoGenerator */\n"
        file.write(command)

        InputPinCounter = 0
        for i in self.AllPinDictList:
            flag = False
            if i["PinState"]:
                if not i["PinMode"]:
                    if not i["PinType"]:
                        command = "  int val" + str(InputPinCounter) + " = digitalRead(" + i["PinName"] + ");\n"
                    else:
                        command = "  int val" + str(InputPinCounter) + " = analogRead(" + i["PinName"] + ");\n"
                    InputPinCounter += 1
                    file.write(command)

        file.write("\n")

        for i in self.AllPinDictList:
            flag = False
            if i["PinState"]:
                if i["PinMode"]:
                    if not i["PinType"]:
                        command = "  digitalWrite(" + i["PinName"] + ", HIGH);\n"
                    else:
                        command = "  analogWrite(" + i["PinName"] + ", 100);\n"
                    file.write(command)

        command = "/* Example Code End */\n\n}\n"
        file.write(command)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
