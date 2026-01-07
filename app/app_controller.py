from PySide6.QtCore import QObject, Property, Signal, Slot


class AppController(QObject):
    """
    Python QObject exposed to QML.
    Holds counter state and exposes slots for UI interactions.
    """
    counterChanged = Signal(int)

    def __init__(self):
        super().__init__()
        self._counter = 0

    # Property
    def get_counter(self):
        return self._counter

    def set_counter(self, value):
        if self._counter != value:
            self._counter = value
            self.counterChanged.emit(self._counter)

    counter = Property(int, get_counter, set_counter, notify=counterChanged)

    # Slots
    @Slot()
    def increment(self):
        self.counter += 1

    @Slot()
    def decrement(self):
        self.counter -= 1

    @Slot()
    def reset(self):
        self.counter = 0
