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

ftn = int(input("""Input the approximate that you want:
 -> Trapezium (1)
 -> Rectangle (2)
 -> Simpson   (3)
 """))

if ftn == 1:
    print(eqt.trapezium_values())
elif ftn == 2:
    print(eqt.rectangle_values())
elif ftn == 3:
    print(eqt.simpson_values())
else:
    print("Invalid Key...")

# Plotting with graphs class...

# End
