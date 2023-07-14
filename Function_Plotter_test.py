#!/usr/bin/env python3
"""
Created on Mon Jul 10 16:19:15 2023
fp_v4_test_v1
@author: bassamsobhy
"""
import pytest
from PySide2.QtWidgets import QApplication
from fp_v4 import MainWindow


@pytest.fixture
def app(qtbot):
    test_app = QApplication([])
    qtbot.addWidget(MainWindow())
    return test_app


def test_plot_function(app, qtbot):
    main_window = MainWindow()
    qtbot.addWidget(main_window)

    # Test invalid input
    main_window.func_edit.setText("")
    main_window.x_min_edit.setText("0")
    main_window.x_max_edit.setText("10")
    qtbot.mouseClick(main_window.findChild(QPushButton, "Plot"), Qt.LeftButton)
    error_label = main_window.centralWidget().findChild(QLabel)
    assert error_label is not None
    assert error_label.text() == "Please enter a function of x."

    main_window.func_edit.setText("sin(x)")
    main_window.x_min_edit.setText("a")
    main_window.x_max_edit.setText("b")
    qtbot.mouseClick(main_window.findChild(QPushButton, "Plot"), Qt.LeftButton)
    error_label = main_window.centralWidget().findChild(QLabel)
    assert error_label is not None
    assert error_label.text() == "Please enter valid values for the min and max values of x."

    # Test valid input
    main_window.func_edit.setText("sin(x)")
    main_window.x_min_edit.setText("0")
    main_window.x_max_edit.setText("10")
    qtbot.mouseClick(main_window.findChild(QPushButton, "Plot"), Qt.LeftButton)
    error_label = main_window.centralWidget().findChild(QLabel)
    assert error_label is None
    canvas = main_window.findChild(FigureCanvas)
    assert canvas is not None
    assert len(canvas.figure.axes) == 1
