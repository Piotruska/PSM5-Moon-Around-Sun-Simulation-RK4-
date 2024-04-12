import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from Plotter import plot_orbits, animate_orbits

# Constants
G = 6.67430e-11  # gravitational constant [N*m^2/kg^2]
Ms = 1.989e30  # mass of the Sun [kg]
Me = 5.972e24  # mass of the Earth [kg]
Mm = 7.34767309e22  # mass of the Moon [kg]
Res = 1.5e11  # distance Earth-Sun [m]
Rem = 384400e3  # distance Earth-Moon [m]

v_earth_orbital = np.sqrt(G * Ms / Res)  # Earth's orbital speed around the Sun
v_moon_orbital = np.sqrt(G * Me / Rem) + v_earth_orbital  # Moon's orbital speed (around Earth + Earth around Sun)

x0 = np.array([
    Res, 0, 0, v_earth_orbital,  # Earth's initial position and velocity
    Res + Rem, 0, 0, v_moon_orbital  # Moon's initial position and velocity
])

t0 = 0
tf = 365.25 * 24 * 3600  # year in sec
N = 10000
h = (tf - t0) / N

# Simulation
t = t0
x = x0
xs, ys, xm, ym = [], [], [], []

# CALCULATION FUNCTIONS (RK4 Method)

def rk4_step(t, x, h):
    k1 = f(t, x)
    k2 = f(t + 0.5 * h, x + 0.5 * h * k1)
    k3 = f(t + 0.5 * h, x + 0.5 * h * k2)
    k4 = f(t + h, x + h * k3)
    return x + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

def f(t, x):
    xE, yE, vxE, vyE, xM, yM, vxM, vyM = x
    rES = np.sqrt(xE ** 2 + yE ** 2)
    rMS = np.sqrt(xM ** 2 + yM ** 2)
    rEM = np.sqrt((xM - xE) ** 2 + (yM - yE) ** 2)

    # Earth's acceleration due to the Sun's gravity
    axE = -G * Ms * xE / (rES ** 3)
    ayE = -G * Ms * yE / (rES ** 3)
    # Moon's acceleration due to the Sun's and Earth's gravity
    axM = -G * Ms * xM / (rMS ** 3) + G * Me * (xE - xM) / (rEM ** 3)
    ayM = -G * Ms * yM / (rMS ** 3) + G * Me * (yE - yM) / (rEM ** 3)

    return np.array([vxE, vyE, axE, ayE, vxM, vyM, axM, ayM])


