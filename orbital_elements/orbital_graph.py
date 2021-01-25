from __future__ import division, annotations
# from mpl_toolkits.mplot3d import Axes3D
from .tle import Tle
import numpy as np
import matplotlib.pyplot as plt

_EARTH_RADIUS = 6371  # Kilometers
_2PI = 2 * np.pi
_RAD = float(np.pi / 180)
_DEG = float(180 / np.pi)

max_radius = 0

fig = plt.figure()  # Square figure
ax = fig.add_subplot(111, projection='3d', aspect='auto')


def plot_earth() -> None:
    global max_radius
    max_radius = max(max_radius, _EARTH_RADIUS)

    coefficients = (1, 1, 1)
    rx, ry, rz = list(_EARTH_RADIUS / np.sqrt(c) for c in coefficients)
    u = np.linspace(0, _2PI, 100)
    v = np.linspace(0, np.pi, 100)

    x = rx * np.outer(np.cos(u), np.sin(v))
    y = ry * np.outer(np.sin(u), np.sin(v))
    z = rz * np.outer(np.ones_like(u), np.cos(v))

    ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b')


def plot_orbit(label: str, tle: Tle) -> None:
    # Rotation matrix for inclination
    inclination = tle.inclination * _RAD
    R = np.matrix([[1, 0, 0],
                   [0, np.cos(inclination), -1 * np.sin(inclination)],
                   [0, np.sin(inclination), np.cos(inclination)]])

    # Rotation matrix for right of ascension
    rotation = (tle.right_of_ascension + tle.perigee) * _RAD
    R2 = np.matrix([[np.cos(rotation), -1 * np.sin(rotation), 0],
                    [np.sin(rotation), np.cos(rotation), 0],
                    [0, 0, 1]])

    # Calculate orbit
    theta = np.linspace(0, _2PI, 360)
    r = (tle.semi_major_axis * (1 - tle.eccentricity**2)) \
        / (1 + tle.eccentricity * np.cos(theta))

    xr = (r * np.cos(theta))
    yr = r * np.sin(theta)
    zr = 0 * theta

    pts = np.matrix([xr, yr, zr])  # Rotate by inclination
    pts = (R * R2 * pts.T).T  # Rotate by ascension

    # Convert to vectors
    xr, yr, zr = pts[:, 0].A.flatten(), \
        pts[:, 1].A.flatten(), \
        pts[:, 2].A.flatten()

    # Calculate satellite position

    # Draw stuff
    plot_earth()  # Draw Earth
    ax.plot(xr, yr, zr, '-', color='r')  # Draw orbit
    plt.show()  # Show everything
