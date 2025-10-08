import json

from PySide6.QtCore import QTime, QTimer
from PySide6.QtWidgets import QMessageBox

# import resources_rc
from uifile import Ui_Form


class SettingUI(Ui_Form):
    def __init__(self, Form):
        super().setupUi(Form)
        """
        current_dir = pathlib.Path(__file__).parent
        config_path = current_dir / "setting.json"
        """
        with open("setting.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.lineEdit_3.setText(str(data["CaptionText"]))
        self.lineEdit_4.setText(str(data["RemindText"]))
        self.lineEdit_6.setText(str(data["ExtensionText"]))
        self.lineEdit_7.setText(str(data["DismissText"]))
        self.lineEdit_8.setText(str(data["InfoTextCaption"]))
        self.lineEdit_9.setText(str(data["FuckText"]))
        self.lineEdit_10.setText(str(data["ThanksText"]))
        self.checkBox.setChecked(data["CI"])
        self.load_times(data.get("Time", []))
        if int(data["ForceCutdown"]) >= 9999999:
            self.checkBox_9.setChecked(False)
            self.lineEdit.setText("")
        else:
            self.lineEdit.setText(str(data["ForceCutdown"]))
        self.TextEditWindow.hide()
        self.frame_5.hide()
        self.frame_6.hide()
        self.toast.hide()
        self.pushButton_4.clicked.connect(self.save_config)
        self.Setting.clicked.connect(lambda: self.TextEditWindow.hide())
        self.TextSetting.clicked.connect(lambda: self.TextEditWindow.show())
        self.pushButton_3.clicked.connect(lambda: self.frame_5.show())
        self.TextSetting_2.clicked.connect(lambda: self.frame_5.hide())
        self.TextSetting_3.clicked.connect(lambda: self.frame_6.hide())
        self.pushButton_2.clicked.connect(lambda: self.frame_6.show())
        self.pushButton.clicked.connect(
            lambda: QMessageBox.warning(
                None,
                "手动设置欲查杀的程序",
                "该功能仅限高级用户，请在实验性选项中编辑JSON",  # type: ignore
            )
        )

    def load_times(self, time_list):
        # 然后逐个设置时间
        for i, time_str in enumerate(time_list, 1):
            if i > 12:  # 最多显示12个时间
                break

            # 获取对应的 timeEdit 控件
            if i == 1:
                time_edit = getattr(self, "timeEdit", None)
            else:
                time_edit = getattr(self, f"timeEdit_{i}", None)

            if time_edit and time_str:
                try:
                    # 将字符串时间转换为 QTime 并设置
                    time_obj = QTime.fromString(time_str, "HH:mm:ss")
                    if time_obj.isValid():
                        time_edit.setTime(time_obj)
                except Exception as e:
                    print(f"设置时间控件 {i} 失败: {e}")

    def save_config(self):
        """
        current_dir = pathlib.Path(__file__).parent
        config_path = current_dir / "setting.json"
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        """
        with open("setting.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        data["cutdown"] = int(self.lineEdit_2.text())
        data["CaptionText"] = str(self.lineEdit_3.text())
        data["RemindText"] = str(self.lineEdit_4.text())
        data["ExtensionText"] = str(self.lineEdit_6.text())
        data["DismissText"] = str(self.lineEdit_7.text())
        data["InfoTextCaption"] = str(self.lineEdit_8.text())
        data["FuckText"] = str(self.lineEdit_9.text())
        data["ThanksText"] = str(self.lineEdit_10.text())
        time_list = []
        for i in range(1, 13):
            if i == 1:
                time_edit = getattr(self, "timeEdit", None)
            else:
                time_edit = getattr(self, f"timeEdit_{i}", None)
            if time_edit:
                time_str = time_edit.time().toString("HH:mm:ss")
                if time_str != "00:00:00":
                    time_list.append(time_str)
        data["Time"] = time_list
        if not self.checkBox_9.isChecked():
            data["ForceCutdown"] = 10000000
        else:
            data["ForceCutdown"] = int(self.lineEdit.text())
        data["CI"] = self.checkBox.isChecked()
        with open("setting.json", "w") as file:
            json.dump(data, file)
        self.toast.show()
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.toast.hide())
        self.timer.start(1000)
