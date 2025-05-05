# -*- coding: utf-8 -*-
"""
Problem Statement:

You are required to calculate the definite integral of the function f(t) = t^2 * cos(t)
over the interval from t = 1 second to t = 4 seconds. This integral represents the total 
quantity of the signal processed within this time range.

Additionally, you need to plot the graph of the function f(t) for t ranging from 0 seconds 
to 5 seconds. On the graph, you should mark the boundaries at t = 1 second and t = 4 seconds 
with vertical dashed lines. These lines will help identify the limits of integration.

Furthermore, the area under the curve between t = 1 second and t = 4 seconds should be shaded 
with a light gray color to highlight the region corresponding to the integral.
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols('t')

# Defining the function
f_t = t**2 * sp.cos(t)

integral_result = sp.integrate(f_t, (t, 1, 4))
integral_result.evalf()

# Def of the function
def f(t):
    return t**2 * np.cos(t)

# Interval for the graph
t_values = np.linspace(0, 5, 400)
f_values = f(t_values)


plt.figure(figsize=(8, 6))
plt.plot(t_values, f_values, label=r'$f(t) = t^2 \cos(t)$', color='hotpink')

# Filling the area between t = 1 and t = 4
t_fill = np.linspace(1, 4, 200)
f_fill = f(t_fill)
plt.fill_between(t_fill, f_fill, color='lightgray', alpha=0.5)

# Adding vertical lines between t=1 and t=4
plt.axvline(x=1, color='orange', linestyle='--', label=r'$t=1$')
plt.axvline(x=4, color='orange', linestyle='--', label=r'$t=4$')

# Highlighting the points
for t_val in [1, 2, 3, 4]:
    plt.scatter(t_val, f(t_val), color='black', zorder=5)
    plt.text(t_val, f(t_val), f'  t={t_val}', color='black', fontsize=10)

plt.title('$f(t) = t^2 \\cos(t)$ with integral shaded area')
plt.xlabel('t')
plt.ylabel('$f(t)$')
plt.legend(loc='upper right')

plt.grid(True)
plt.show()

integral_result.evalf()