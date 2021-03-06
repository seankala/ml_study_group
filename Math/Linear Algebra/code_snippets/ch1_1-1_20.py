'''
An Introduction to Linear Algebra (4e) - Gilbert Strang

Chapter 1
Problem Set 1-1
#20
'''

import matplotlib.pyplot as plt


# v
plt.quiver(0, 0, 3, 1, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}$')

# w
plt.quiver(0, 0, 1, 3, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$\vec{w}$')

# u
plt.quiver(0, 0, 2.5, 3.5, color='C2', angles='xy', scale_units='xy', scale=1, label=r'$\vec{u}$')

# Dotted lines.
plt.plot([1, 2.5], [3, 3.5], 'k--')
plt.plot([2.5, 3], [3.5, 1], 'k--')
plt.plot([1, 3], [3, 1], 'k--')

# (1/3)u + (1/3)v + (1/3)w
plt.plot(2.1, 2.6, 'ro', label=r'$\frac{1}{3}\vec{u} + \frac{1}{3}\vec{v} + \frac{1}{3}\vec{w}$')

# (1/2)u + (1/2)w
plt.plot(1.75, 3.25, 'bo', label=r'$\frac{1}{2}\vec{u} + \frac{1}{2}\vec{v}$')

# (1/2)u
plt.quiver(0.5, 1.5, 1.25, 1.75, color='C3', angles='xy', scale_units='xy', scale=1, label=r'$\frac{1}{2}\vec{u}$')

# (1/2)w
plt.quiver(0, 0, 0.5, 1.6, color='C4', angles='xy', scale_units='xy', scale=1, label=r'$\frac{1}{2}\vec{w}$')

# (1/3)u
plt.quiver(0, 0, 0.8333, 1.1666, color='C5', angles='xy', scale_units='xy', scale=1, label=r'$\frac{1}{3}\vec{u}$')

# (1/3)v
plt.quiver(0.8333, 1.1666, 0.9167, 0.4333, color='C6', angles='xy', scale_units='xy', scale=1, label=r'$\frac{1}{3}\vec{v}$')

# (1/3)w
plt.quiver(1.75, 1.6, 0.3999, 1.1, color='C7', angles='xy', scale_units='xy', scale=1, label=r'$\frac{1}{3}\vec{w}$')

# Miscellaneous.
plt.xlim(-1, 8)
plt.ylim(-1, 8)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel(r'$x$', fontsize='large')
plt.ylabel(r'$y$', fontsize='large')
plt.grid()
plt.legend()
plt.show()