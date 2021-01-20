"""
This script going to calculate a numeric integral of a function with
techniques as rectangle, trapezium and simpson.., tra, for this
we need 3 class:
main -> principal class...
calculator -> to resolver the integral...
graphs -> to plot the integral ...
"""
from calculator import Calculator
import graphs

# Asking for variables...
f = input("Input the function...: ")
inf = int(input("Input the inferior limit...: "))
sup = int(input("Input the superior limit...: "))
p = int(input("Input the point numbers...: "))

# Define a function object...
eqt = Calculator(f, inf, sup, p)
print("The value of the integral is: ", eqt.integral())
print(eqt.table())

# Plotting with graphs class...

# End
