"""
Created on Mon Jul 15 2:25:30 2023
Function-Plotter_test-version4
@author: bassamsobhykhalafallah
"""


# Import necessary lib.

import pytest
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtCore import Qt
from Function_Plotter import MainWindow


@pytest.fixture(scope="session")
def qapp():
    app = QApplication.instance()
    if not app:
        app = QApplication([])
    yield app
    app.exit()


@pytest.fixture
def app(qtbot, qapp):
    main_window = MainWindow()
    qtbot.addWidget(main_window)
    return main_window


def test_plot_function(app, qtbot):
    # Test invalid input
    app.func_edit.setText("")
    app.x_min_edit.setText("-2")
    app.x_max_edit.setText("2")
    qtbot.mouseClick(app.findChild(QPushButton, "Plot"), Qt.LeftButton)
    error_label = app.centralWidget().findChild("QLabel")
    assert error_label is not None
    assert error_label.text() == "Please enter a function of x."

    app.func_edit.setText("x^2")
    app.x_min_edit.setText("a")
    app.x_max_edit.setText("2")
    qtbot.mouseClick(app.findChild(QPushButton, "Plot"), Qt.LeftButton)
    error_label = app.centralWidget().findChild("QLabel")
    assert error_label is not None
    assert error_label.text() == "Please enter valid values for the min and max values of x."

    # Test valid input
    app.func_edit.setText("x^2")
    app.x_min_edit.setText("-2")
    app.x_max_edit.setText("2")
    qtbot.mouseClick(app.findChild(QPushButton, "Plot"), Qt.LeftButton)
    error_label = app.centralWidget().findChild("QLabel")
    assert error_label is None
    canvas = app.findChild(type(app).FigureCanvas)
    assert canvas is not None
    assert len(canvas.figure.axes) == 1
