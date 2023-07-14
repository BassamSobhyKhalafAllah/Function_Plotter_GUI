# Function Plotter

## Introduction
Python GUI program that plots an arbitrary user-entered function using Pyside2 and Matplotlib
and Pytest for automated testing
GUI which is 1.Take a function of x from the user, e.g., 5*x^3 + 2*x.
             2.Take min and max values of x from the user.

<p align="center">
  <img height="300" src="function_plotted.png">
</p>

## Requirments
* App requirments 
```python3
pip install PySide2
pip install numpy
pip install matplotlib
pip install os-sys
```
* Testing Requirments
```python3
pip install pytest
pip install pytest-qt
```

## Usage

* Run [Function_Plotter.py](Function_Plotter.py) file.
```python3
python3 Function_Plotter.py
```
* In case of automated tests, run [Function_Plotter_test.py](Function_Plotter_test.py) file.
```python3
pytest3 Function_Plotter_test.py
```
