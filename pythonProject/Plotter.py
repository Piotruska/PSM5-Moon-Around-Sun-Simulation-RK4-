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


def animate_orbits(xs, ys, xm, ym, N, scale_factor=2):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor('black')
    ax.plot(xs, ys, 'b-', label="Earth's Orbit", linewidth=0.5)  # Earth's orbit
    ax.plot([x + scale_factor * (xm[i] - x) for i, x in enumerate(xs)],
            [y + scale_factor * (ym[i] - y) for i, y in enumerate(ys)],
            'w--', label="Moon's Exaggerated Orbit", linewidth=0.5)

    ax.plot(0, 0, 'yo', markersize=20)  # Sun
    earth, = ax.plot([], [], 'o', color='blue', markersize=10)
    moon, = ax.plot([], [], 'o', color='gray', markersize=5)

    def init():
        earth.set_data([], [])
        moon.set_data([], [])
        return earth, moon,

    def update(frame):
        ex, ey = xs[frame], ys[frame]
        mx, my = xs[frame] + scale_factor * (xm[frame] - xs[frame]), ys[frame] + scale_factor * (ym[frame] - ys[frame])

        earth.set_data(ex, ey)
        moon.set_data(mx, my)
        return earth, moon,

    ani = FuncAnimation(fig, update, frames=N, init_func=init, blit=True, repeat=True, interval=5)
    plt.legend()
    plt.axis('equal')
    plt.show()