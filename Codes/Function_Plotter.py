
"""
Created on Mon Jul 10 16:19:15 2023
Function-Plotter-version4
@author: bassamsobhykhalafallah
"""

# Import necessary lib.
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

# Define a custom MainWindow class that inherits from QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window properties
        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and a vertical layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        vbox = QVBoxLayout(central_widget)

        # Create a label and a line edit for the function of x
        func_label = QLabel("Function of x:")
        self.func_edit = QLineEdit()
        vbox.addWidget(func_label)
        vbox.addWidget(self.func_edit)

        # Create labels and line edits for the min and max values of x
        x_min_label = QLabel("Min value of x:")
        self.x_min_edit = QLineEdit()
        x_max_label = QLabel("Max value of x:")
        self.x_max_edit = QLineEdit()
        vbox.addWidget(x_min_label)
        vbox.addWidget(self.x_min_edit)
        vbox.addWidget(x_max_label)
        vbox.addWidget(self.x_max_edit)

        # Create a button to plot the function
        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(self.plot_function)
        vbox.addWidget(plot_button)

        # Create a figure canvas to display the plot
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        vbox.addWidget(self.canvas)

    def plot_function(self):
        # Get the user input for the function of x and the min and max values of x
        func_str = self.func_edit.text()
        x_min_str = self.x_min_edit.text()
        x_max_str = self.x_max_edit.text()

        # Validate the user input
        if not func_str:
            # If the function edit box is empty, clear the canvas and display an error message
            self.canvas.figure.clear()
            self.canvas.draw()
            self.display_error_message(
                "Please enter a Plynomial function of x.")
            return
        try:
            # Try to convert the min and max x values to floats and generate an array of x values
            # Then, evaluate the function for each x value and plot the result
            x_min = float(x_min_str)
            x_max = float(x_max_str)
            x = np.linspace(x_min, x_max, 1000)
            y = eval(func_str.replace('^', '**'))
        except:
            # If there was an error in the user input, clear the canvas and display an error message
            self.canvas.figure.clear()
            self.canvas.draw()
            self.display_error_message(
                "Please enter valid values for the min and max values of x. or check the function")
            return

        # Plot the function using Matplotlib
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel("x")
        ax.set_ylabel("F(x)")
        self.canvas.draw()

    def display_error_message(self, message):
        # Create a label to display the error message in red text
        error_label = QLabel(message)
        error_label.setStyleSheet("color: red")

        # Clear the canvas and display the error message
        self.canvas.figure.clear()
        self.canvas.draw()
        vbox = self.centralWidget().layout()
        vbox.addWidget(error_label)


if __name__ == '__main__':
    # Create a Qt application instance and a main window object
    app = QApplication(sys.argv)
    main_window = MainWindow()

    # Show the main window and start the Qt event loop
    main_window.show()
    sys.exit(app.exec_())
