import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Use Matplotlib native MathText rendering to avoid external LaTeX dependency errors
plt.rcParams.update({
    "text.usetex": False,
    "mathtext.fontset": "cm",  # Use Computer Modern academic math font
    "font.family": "serif",
    "font.size": 11
})

def generate_figure_1():
    """Draw Figure 1: Orbital Configuration and Motional EMF."""
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    # Earth Representation
    earth_radius = 2.0
    earth = patches.Circle((0, 0), earth_radius, color='#AADDFF', ec='#5588AA', lw=2, label='Earth')
    ax.add_patch(earth)
    ax.text(0, 0, r'Earth ($M_E$)', ha='center', va='center', fontsize=12, fontweight='bold')

    # Orbit Path
    orbit_r = 5.0
    orbit_arc = patches.Arc((0, 0), 2*orbit_r, 2*orbit_r, theta1=20, theta2=70, ls='--', color='gray', alpha=0.6)
    ax.add_patch(orbit_arc)

    # Tether System at theta = 45 degrees
    angle = np.deg2rad(45)
    r1 = orbit_r - 0.6
    r2 = orbit_r + 0.6
    x1, y1 = r1 * np.cos(angle), r1 * np.sin(angle)
    x2, y2 = r2 * np.cos(angle), r2 * np.sin(angle)
    
    # Satellites
    ax.plot([x1, x2], [y1, y2], color='black', lw=2, zorder=3)
    ax.scatter([x1, x2], [y1, y2], color='#444444', s=80, zorder=4)
    ax.text(x1-0.2, y1-0.4, r'$m$', ha='center')
    ax.text(x2+0.2, y2+0.3, r'$m$', ha='center')
    
    # Labels for geometry
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='<->', color='black'))
    ax.text((x1+x2)/2 + 0.3, (y1+y2)/2, r'$L$', fontsize=12)
    
    # Radius vector
    ax.annotate('', xy=(x1, y1), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='black', ls=':'))
    ax.text(1.2, 2.2, r'$r$', fontsize=12)

    # Velocity Vector
    v_dir = np.array([-np.sin(angle), np.cos(angle)])
    v_start = np.array([(x1+x2)/2, (y1+y2)/2])
    ax.quiver(v_start[0], v_start[1], v_dir[0], v_dir[1], color='blue', scale=4, width=0.015, zorder=5)
    ax.text(v_start[0]-0.8, v_start[1]+0.5, r'$\vec{v}$', color='blue', fontsize=14)

    # B-field (Out of page)
    for i in range(3):
        for j in range(3):
            bx, by = 3.5 + i*0.8, 0.5 + j*0.8
            ax.text(bx, by, r'$\odot$', color='forestgreen', fontsize=15, ha='center', va='center')
    ax.text(5.5, 1.5, r'$\vec{B}$', color='forestgreen', fontsize=14)

    plt.title("Fig 1: EDT Orbital Configuration in Equatorial Plane", pad=20)
    plt.tight_layout()
    plt.savefig("Figure_1.png", dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("Figure_1.png generated successfully.")

def generate_figure_2():
    """Draw Figure 2: Electrodynamic Forces and Circuit Model."""
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_aspect('equal')
    ax.axis('off')

    # The Tether
    tether_y = np.linspace(-2, 2, 100)
    tether_x = np.zeros_like(tether_y)
    ax.plot(tether_x, tether_y, color='black', lw=3, zorder=3)
    
    # Satellites (Anode and Cathode)
    ax.scatter([0, 0], [-2, 2], color='#444444', s=150, zorder=4)
    ax.text(0.3, 2, 'Upper Sat (Anode)', va='center')
    ax.text(0.3, -2, 'Lower Sat (Cathode)', va='center')

    # Current I
    ax.annotate('', xy=(0, 0.5), xytext=(0, -0.5), arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(-0.4, 0, r'$I$', color='red', fontsize=14, fontweight='bold')

    # Lorentz Force F_L
    ax.quiver(0, 0, -1.5, 0, color='orangered', scale=5, width=0.02, zorder=5)
    ax.text(-1.2, 0.3, r"$\vec{F}_L$", color='orangered', fontsize=14)
    
    # Velocity v
    ax.quiver(0, 0, 1.5, 0, color='blue', scale=5, width=0.01, alpha=0.5)
    ax.text(1.0, 0.3, r"$\vec{v}$", color='blue', fontsize=14)

    # Plasma Return Path
    arc_theta = np.linspace(-np.pi/2, np.pi/2, 50)
    arc_x = 1.5 * np.cos(arc_theta)
    arc_y = 2.0 * np.sin(arc_theta)
    ax.plot(arc_x, arc_y, color='skyblue', ls='--', lw=2, alpha=0.7)
    ax.text(1.6, 0, 'Ionospheric\nPlasma Path', color='skyblue', ha='left', fontsize=10)

    # Thermal Radiation (Part C context)
    for y_pos in [-1.2, 0, 1.2]:
        for direction in [-1, 1]:
            dx = 0.3 * direction
            ax.annotate('', xy=(dx*2, y_pos+0.2), xytext=(dx, y_pos),
                         arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.3", color='purple', alpha=0.6))
    ax.text(-1.2, -1.8, r'$P_{rad} \propto T^4$', color='purple', fontsize=10)

    # B field symbol
    ax.text(-1.5, 2, r'$\vec{B} = \odot$', color='forestgreen', fontsize=14)

    plt.title("Fig 2: Electrodynamic Forces and Plasma Return Circuit", pad=20)
    plt.tight_layout()
    plt.savefig("Figure_2.png", dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("Figure_2.png generated successfully.")

if __name__ == "__main__":
    generate_figure_1()
    generate_figure_2()
    print("All figures generated for IPhO Problem 1.")
