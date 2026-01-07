import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    id: counterView
    width: 200
    height: 150
    color: "#f0f0f0"
    radius: 10
    border.color: "#cccccc"
    border.width: 1

    Column {
        anchors.centerIn: parent
        spacing: 10

        Text {
            id: counterLabel
            text: counterController.counter
            font.pixelSize: 32
            horizontalAlignment: Text.AlignHCenter
            width: parent.width
        }

        Row {
            spacing: 10
            anchors.horizontalCenter: parent.horizontalCenter

            Button {
                text: "-"
                onClicked: counterController.decrement()
            }
            Button {
                text: "Reset"
                onClicked: counterController.reset()
            }
            Button {
                text: "+"
                onClicked: counterController.increment()
            }
        }
    }

    // Expose controller property
    property var counterController
}
