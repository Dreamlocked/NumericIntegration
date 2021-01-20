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
        self.step = (self.inferior + self.superior) / self.points

    # Firs methode, value of the integral
    def integral(self):
        return integrate(self.equation, (x, self.inferior, self.superior))

    # Second, do a table with values
    def table(self):
        # X, Y columns
        x_column = [self.inferior + self.step * i for i in range(self.points+1)]
        y_column = [sympify(self.equation).subs(x, x_column[i]) for i in range(len(x_column))]
        data = {"X": x_column, "Y": y_column}
        # Table
        df = pd.DataFrame(data=data)
        return df

    def trapezium_values(self):
        y_column = self.table()["Y"].tolist()
        return [(y_column[i] + y_column[i+1]) * self.step / 2 for i in range(len(y_column)-1)]

    def rectangle_values(self):
        y_column = self.table()["Y"].tolist()
        return [(y_column[i]) * self.step for i in range(len(y_column))]

    def simpson_values(self):
        y_column = self.table()["Y"].tolist()
        return [(self.step / 2) * (y_column[i] + 4 * y_column[i+1] + y_column[i+2]) for i in range(0, len(y_column)-2, 2)]

