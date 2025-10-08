import json
import multiprocessing
import sys
import time
from datetime import datetime, timedelta

from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QMessageBox,
    QSystemTrayIcon,
)

from main import main as show_overlay
from setting_ui import SettingUI


class UltraLightLauncher:
    def __init__(self, times):
        self.times = times
        self.next_ring_time = None
        self.calculate_next_ring()

    def calculate_next_ring(self):
        if not self.times:
            self.next_ring_time = None
            return

        now = datetime.now()

        for ring_time_str in self.times:
            if ":" in ring_time_str:
                parts = ring_time_str.split(":")
                if len(parts) == 2:
                    ring_time = datetime.strptime(
                        ring_time_str + ":00", "%H:%M:%S"
                    ).time()
                else:
                    ring_time = datetime.strptime(ring_time_str, "%H:%M:%S").time()

                ring_datetime = datetime.combine(now.date(), ring_time)

                if ring_datetime <= now:
                    ring_datetime += timedelta(days=1)

                if self.next_ring_time is None or ring_datetime < self.next_ring_time:
                    self.next_ring_time = ring_datetime

    def get_time_until_next_ring(self):
        if self.next_ring_time is None:
            return "无时间设置"

        now = datetime.now()
        time_diff = self.next_ring_time - now

        # 修复递归问题：直接返回0秒而不是递归调用
        if time_diff.total_seconds() <= 0:
            self.calculate_next_ring()
            # 如果重新计算后仍然没有有效时间，返回0秒
            if self.next_ring_time is None:
                return "0秒"
            # 重新计算时间差
            time_diff = self.next_ring_time - now

        total_seconds = int(time_diff.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        if hours > 0:
            return f"{hours}时{minutes}分{seconds}秒"
        elif minutes > 0:
            return f"{minutes}分{seconds}秒"
        else:
            return f"{seconds}秒"

    def should_launch(self):
        if not self.times:
            return False

        current_time_str = datetime.now().strftime("%H:%M:%S")

        for dismiss_time in self.times:
            if dismiss_time.count(":") == 1:
                dismiss_time += ":00"

            if current_time_str == dismiss_time:
                return True

        return False

    def monitor_loop(self):
        while True:
            if self.should_launch():
                multiprocessing.Process(target=show_overlay, daemon=True).start()
                self.calculate_next_ring()
                time.sleep(1)
            time.sleep(0.1)


class SystemTrayApp:
    def __init__(self, times):
        self.app = QApplication([])
        self.app.setQuitOnLastWindowClosed(False)

        self.launcher = UltraLightLauncher(times)

        self.tray_icon = QSystemTrayIcon()
        self.setup_tray_icon()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_tooltip)
        self.timer.start(100)

        self.setting_window = QMainWindow()
        self.setting_window.setFixedSize(690, 427)
        self.setting_ui = SettingUI(self.setting_window)
        self.setting_window.setWindowIcon(QIcon("assets/tray_icon.ico"))

        import threading

        self.monitor_thread = threading.Thread(
            target=self.launcher.monitor_loop, daemon=True
        )
        self.monitor_thread.start()

    def setup_tray_icon(self):
        self.tray_icon.setIcon(QIcon(str("assets/tray_icon.ico")))

        self.update_tooltip()

        tray_menu = QMenu()

        status_action = QAction("状态信息", self.app)
        status_action.triggered.connect(self.show_status)
        tray_menu.addAction(status_action)

        times_action = QAction("时间表", self.app)
        times_action.triggered.connect(self.show_times)
        tray_menu.addAction(times_action)

        tray_menu.addSeparator()

        quit_action = QAction("设置", self.app)
        quit_action.triggered.connect(self.show_settings)
        tray_menu.addAction(quit_action)

        quit_action = QAction("退出", self.app)
        quit_action.triggered.connect(self.quit_application)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.on_tray_activated)
        self.tray_icon.show()

    def update_tooltip(self):
        time_until = self.launcher.get_time_until_next_ring()
        tooltip = f"360拖堂卫士 - 下次打铃: {time_until}"
        self.tray_icon.setToolTip(tooltip)

    def on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.show_status()

    def show_status(self):
        time_until = self.launcher.get_time_until_next_ring()

        if self.launcher.next_ring_time:
            next_time = self.launcher.next_ring_time.strftime("%H:%M:%S")
            status_msg = f"距离下次打铃: {time_until}\n打铃时间: {next_time}"
        else:
            status_msg = "无打铃时间设置"

        QMessageBox.information(None, "监控状态", status_msg)

    def show_times(self):
        if not self.launcher.times:
            QMessageBox.information(None, "时间表", "没有配置打铃时间")
            return

        times_list = "\n".join([f"• {time}" for time in self.launcher.times])
        QMessageBox.information(None, "打铃时间表", f"监控时间:\n{times_list}")

    def show_settings(self):
        self.setting_window.show()

    def quit_application(self):
        self.tray_icon.hide()
        self.app.quit()

    def run(self):
        sys.exit(self.app.exec())


# 嗯造屎山这块。抽象？哪里有抽象
# TODO: 优化CI集成的触发方式
class SystemTrayAppCI:
    def __init__(self):
        self.app = QApplication([])
        self.app.setQuitOnLastWindowClosed(False)

        self.app.setWindowIcon(QIcon("assets/tray_icon.ico"))
        self.tray_icon = QSystemTrayIcon()
        self.setup_tray_icon()

        self.setting_window = QMainWindow()
        self.setting_window.setFixedSize(690, 427)
        self.setting_ui = SettingUI(self.setting_window)
        self.setting_window.setWindowIcon(QIcon("assets/tray_icon.ico"))

    def setup_tray_icon(self):
        self.tray_icon.setIcon(QIcon(str("assets/tray_icon.ico")))

        self.update_tooltip()

        tray_menu = QMenu()

        status_action = QAction("状态信息", self.app)
        # status_action.triggered.connect(self.show_status)
        tray_menu.addAction(status_action)
        status_action.setEnabled(False)

        times_action = QAction("时间表", self.app)
        # times_action.triggered.connect(self.show_times)
        tray_menu.addAction(times_action)
        times_action.setEnabled(False)

        hint_action = QAction("时间表已由 CI 接管", self.app)
        tray_menu.addAction(hint_action)

        tray_menu.addSeparator()

        quit_action = QAction("设置", self.app)
        quit_action.triggered.connect(self.show_settings)
        tray_menu.addAction(quit_action)

        quit_action = QAction("退出", self.app)
        quit_action.triggered.connect(self.quit_application)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def update_tooltip(self):
        tooltip = "360拖堂卫士 - 时间表已由 CI 接管"
        self.tray_icon.setToolTip(tooltip)

    def show_settings(self):
        self.setting_window.show()

    def quit_application(self):
        self.tray_icon.hide()
        self.app.quit()

    def run(self):
        sys.exit(self.app.exec())


def main():
    with open("setting.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    if data["CI"]:
        tray_app = SystemTrayAppCI()
    else:
        times = data.get("Time", [])
        tray_app = SystemTrayApp(times)

    tray_app.run()


if __name__ == "__main__":
    main()
