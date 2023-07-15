import pytest
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest
from PySide2.QtWidgets import QApplication
from Function_Plotter import MainWindow

# Create a fixture to initialize the QApplication instance


@pytest.fixture(scope="session")
def qapp():
    # Check if QApplication instance already exists
    app = QApplication.instance()
    if not app:
        # If not, create a new QApplication
        app = QApplication([])
    yield app
    # After the test session, exit the application
    app.exit()


# Create a fixture to set up the application and the main window for testing
@pytest.fixture
def app(qtbot, qapp):
    # Create a new QApplication instance for each test
    test_app = QApplication([])
    # Add the main window widget to the qtbot for testing
    qtbot.addWidget(MainWindow())
    return test_app


# Test case for valid input
def test_plot_function_valid_input(app, qtbot):
    # Obtain references to the main window and its widgets
    main_window = app.topLevelWidgets()[0]
    func_edit = main_window.func_edit
    x_min_edit = main_window.x_min_edit
    x_max_edit = main_window.x_max_edit
    plot_button = main_window.findChild(QPushButton, "Plot")
    canvas = main_window.canvas

    # Enter valid input
    qtbot.keyClicks(func_edit, "5*x^3 + 2*x")
    qtbot.keyClicks(x_min_edit, "-5")
    qtbot.keyClicks(x_max_edit, "5")

    # Click the plot button
    qtbot.mouseClick(plot_button, Qt.LeftButton)

    # Assert that the canvas has been updated
    assert not canvas.figure.empty
    assert len(canvas.figure.axes) == 1


# Test case for invalid input
def test_plot_function_invalid_input(app, qtbot):
    # Obtain references to the main window and its widgets
    main_window = app.topLevelWidgets()[0]
    func_edit = main_window.func_edit
    x_min_edit = main_window.x_min_edit
    x_max_edit = main_window.x_max_edit
    plot_button = main_window.findChild(QPushButton, "Plot")
    canvas = main_window.canvas

    # Enter invalid input (empty function)
    qtbot.keyClicks(func_edit, "")

    # Click the plot button
    qtbot.mouseClick(plot_button, Qt.LeftButton)

    # Assert that the canvas is empty and error message is displayed
    assert canvas.figure.empty
    assert len(canvas.figure.axes) == 0
    assert main_window.centralWidget().findChildren(
        QLabel)[0].text() == "Please enter a Polynomial function of x."

    # Clear error message
    main_window.display_error_message("")

    # Enter invalid input (invalid function)
    qtbot.keyClicks(func_edit, "5*x^3 + a*x")

    # Click the plot button
    qtbot.mouseClick(plot_button, Qt.LeftButton)

    # Assert that the canvas is empty and error message is displayed
    assert canvas.figure.empty
    assert len(canvas.figure.axes) == 0
    assert main_window.centralWidget().findChildren(QLabel)[0].text(
    ) == "Please enter valid values for the min and max values of x. or check the function."


# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()
