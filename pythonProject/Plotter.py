from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation



def plot_orbits(xs, ys, xm, ym, scale_factor=2):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(xs, ys, label="Earth", color='blue')
    exaggerated_xm = [xs[i] + scale_factor * (xm[i] - xs[i]) for i in range(len(xs))]
    exaggerated_ym = [ys[i] + scale_factor * (ym[i] - ys[i]) for i in range(len(ys))]
    ax.plot(exaggerated_xm, exaggerated_ym, label="Moon", color='gray', linestyle='--')
    ax.plot(0, 0, 'yo', markersize=10, label="Sun")
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_title('Orbits of Earth and Moon around the Sun (Exaggerated Moon Distance)')
    ax.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

