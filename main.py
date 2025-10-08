import json
import os
import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QCommandLinkButton,
    QDialog,
    QLabel,
    QMessageBox,
    QVBoxLayout,
    QWidget,
)


class OverlayWindow(QWidget):
    """全屏半透明白色遮罩"""

    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )
        self.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.showFullScreen()


class DialogWindow(QDialog):
    """提示对话框"""

    def __init__(self, overlay_window):
        super().__init__()
        self.overlay = overlay_window  # 保存遮罩窗口引用

        with open("setting.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

        self.setWindowTitle(self.data["CaptionText"])
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.WindowTitleHint
            | Qt.WindowType.WindowCloseButtonHint
        )
        self.setFixedSize(380, 200)
        self.center()

        # 提示文字
        self.label = QLabel(self.data["RemindText"], self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font = QFont("Microsoft YaHei", 13, QFont.Weight.Bold)
        self.label.setFont(font)

        # 倒计时
        self.countdown = int(self.data["cutdown"])
        self.timer_label = QLabel(f"倒计时: {self.countdown}s", self)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 按钮
        self.btn_continue = QCommandLinkButton(
            self.data["ExtensionText"], "继续上课，不关闭PPT", self
        )
        self.btn_finish = QCommandLinkButton(
            self.data["DismissText"], "关闭PPT并结束课程", self
        )

        # 布局
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label)
        vbox.addSpacing(20)
        vbox.addWidget(self.timer_label)
        vbox.addSpacing(20)
        vbox.addWidget(self.btn_continue)
        vbox.addWidget(self.btn_finish)

        # 连接按钮
        self.btn_continue.clicked.connect(self.accept_delay)  # 拖堂
        self.btn_finish.clicked.connect(self.reject)  # 下课

        # 倒计时
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start(1000)

        # 强制关闭计时器
        self.force_timer_active = True
        self.force_close_timer = QTimer()
        self.force_close_timer.timeout.connect(self.dismiss)
        self.force_close_timer.setSingleShot(True)
        self.force_close_timer.start(int(self.data["ForceCutdown"]) * 1000)

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def update_countdown(self):
        self.countdown -= 1
        self.timer_label.setText(f"倒计时: {self.countdown}s")
        if self.countdown <= 0:
            self.timer.stop()
            self.accept_delay()  # 超时自动拖堂

    def closeEvent(self, event):
        # 阻止关闭窗口
        event.ignore()
        QMessageBox.warning(self, "提示", "请做出选择，不能直接关闭窗口！")

    def accept_delay(self):
        """拖堂按钮点击 - 关闭所有窗口，程序后台运行"""
        # 停止所有计时器
        self.timer.stop()

        # 使用 accept() 来正确关闭对话框
        self.accept()

        # 关闭遮罩
        if self.overlay:
            self.overlay.close()

    def dismiss(self):
        """强制关闭希沃进程"""
        if not self.force_timer_active:
            return

        self.force_timer_active = False
        self.timer.stop()
        self.force_close_timer.stop()

        print("强制关闭时间到，正在关闭希沃进程...")

        for task in self.data["KillList"]:
            try:
                os.system(f"taskkill /f /im {task}")
                print(f"已关闭进程: {task}")
            except Exception as e:
                print(f"关闭进程 {task} 时出错: {e}")
        os._exit(0)


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("assets/tray_icon.ico"))
    # 创建并显示遮罩窗口
    overlay = OverlayWindow()

    # 创建并显示对话框（传入遮罩窗口引用）
    dialog = DialogWindow(overlay)
    result = dialog.exec()

    # 关闭遮罩（确保无论如何都关闭）
    overlay.close()

    if result == QDialog.DialogCode.Rejected:
        # 下课按钮 - 立即关闭所有进程
        dialog.dismiss()
    else:
        # 拖堂按钮 - 程序继续在后台运行，等待force_close_timer
        # 使用 QTimer 单次触发来保持程序运行但不阻塞
        keep_alive_timer = QTimer()
        keep_alive_timer.timeout.connect(lambda: None)  # 空函数，只是保持事件循环
        keep_alive_timer.start(1000)  # 每秒触发一次

        print("程序在后台运行，等待强制关闭时间...")
        sys.exit(app.exec())


if __name__ == "__main__":
    main()
