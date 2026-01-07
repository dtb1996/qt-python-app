# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from app_controller import AppController


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()

    # Create controller and expose it to QML
    appController = AppController()
    engine.rootContext().setContextProperty("appController", appController)

    qml_file = Path(__file__).resolve().parent / "ui/main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
