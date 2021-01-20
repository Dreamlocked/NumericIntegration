"""
Class to calculate the integral...
"""


# Importing the solve equations...
import numpy as np
from sympy import *
from sympy.abc import x
import pandas as pd


class Calculator:

    # Define the constructor...
    def __init__(self, equation, inferior, superior, points):
        self.equation = equation
        self.inferior = inferior
        self.superior = superior
        self.points = points

    # Firs methode, value of the integral
    def integral(self):
        return integrate(self.equation, (x, self.inferior, self.superior))

    # Second, do a table with values
    def table(self):
        # Steps...
        step = (self.inferior + self.superior) / self.points
        # X, Y columns
        x_column = [self.inferior + step*i for i in range(self.points+1)]
        y_column = [sympify(self.equation).subs(x, x_column[i]) for i in range(len(x_column))]
        data = {"X": x_column, "Y": y_column}
        # Table
        df = pd.DataFrame(data=data)
        return df

    def trapezium_values(self):
        pass

    def rectangle_values(self):
        pass

    def simpson_values(self):
        pass

