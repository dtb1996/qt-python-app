# Qt Python App

A minimal Qt 6 application using Python (PySide6) and QML to demonstrate clean architecture, signal/slot communication, and property binding.

This project is intended as a **baseline app** to get familiar with Python Qt workflows and patterns for interviews or small demos.

## Features

- Counter application with increment, decrement, and reset
- Python `QObject` backend exposed to QML
- Signal and property binding
- Clean separation of UI (QML) and logic (Python)
- Unit tests for backend logic

## Project Structure

```bash
qt-python-app/
├── app/
│   ├── main.py                 # Application entry point
│   ├── app_controller.py       # Python QObject backend
│   └── ui/
│       ├── Main.qml            # Root QML
│       └── components/
│       └── CounterView.qml
├── tests/
│   └── test_app_controller.py
├── pyproject.toml              # Python project metadata (optional)
├── README.md
└── .gitignore
```

## Requirements

- Python 3.10+  
- PySide6

Install dependencies:

```bash
pip install PySide6
```

## Running the App

```bash
python -m app.main
```

## Running Tests

```bash
python -m unittest discover tests
```
