import QtQuick 2.15
import QtQuick.Controls 2.15
import "components"

ApplicationWindow {
    id: mainWindow
    width: 400
    height: 300
    visible: true
    title: "Qt Python Baseline App"

    CounterView {
        anchors.centerIn: parent
        counterController: appController
    }

    Shortcut {
        sequence: "Escape"
        onActivated: Qt.quit()
    }

    Shortcut {
        sequence: "Alt+Return"
        onActivated: mainWindow.visibility = mainWindow.visibility === Window.FullScreen ? Window.Windowed : Window.FullScreen
    }
}
