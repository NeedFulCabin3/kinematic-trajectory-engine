import math
import numpy as np

# Optional graphical plotting support
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


def get_user_inputs() -> tuple:
    """Prompts the user in the terminal for simulation parameters with validation."""
    print("\n" + "="*50)
    print(" 2D KINEMATIC FLIGHT SIMULATOR - CONFIGURATION")
    print("="*50)
    
    # Initial Velocity
    while True:
        try:
            v0 = float(input("Enter initial velocity (m/s, e.g., 50.0): "))
            if v0 <= 0:
                print("Error: Initial velocity must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Launch Angle
    while True:
        try:
            angle = float(input("Enter launch angle (degrees, 0 to 90): "))
            if not (0 <= angle <= 90):
                print("Error: Launch angle must be between 0 and 90 degrees.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Projectile Mass
    while True:
        try:
            mass = float(input("Enter projectile mass (kg, e.g., 1.2): "))
            if mass <= 0:
                print("Error: Mass must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Drag Coefficient
    while True:
        try:
            drag_coeff = float(input("Enter drag coefficient (e.g., 0.015, type 0 for no drag): "))
            if drag_coeff < 0:
                print("Error: Drag coefficient cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    return v0, angle, mass, drag_coeff


def simulate_flight(v0: float, angle_deg: float, mass: float = 1.0, 
                    drag_coeff: float = 0.02, dt: float = 0.01, max_time: int = 60) -> dict:
    """
    Simulates 2D projectile trajectory with quadratic air resistance.
    Returns a dictionary of vectorized numpy.ndarray objects containing flight data.
    """
    theta = math.radians(angle_deg)
    
    vx = v0 * math.cos(theta)
    vy = v0 * math.sin(theta)
    
    x, y = 0.0, 0.0
    g = 9.81
    
    t_list, x_list, y_list, vx_list, vy_list = [0.0], [0.0], [0.0], [vx], [vy]
    t = 0.0
    
    while y >= 0.0 and t < max_time:
        v = math.hypot(vx, vy)
        
        ax = -drag_coeff * v * vx / mass
        ay = -g - (drag_coeff * v * vy / mass)
        
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        t += dt
        
        if y < 0:
            break
            
        t_list.append(t)
        x_list.append(x)
        y_list.append(y)
        vx_list.append(vx)
        vy_list.append(vy)
        
    return {
        "time": np.array(t_list),
        "x": np.array(x_list),
        "y": np.array(y_list),
        "vx": np.array(vx_list),
        "vy": np.array(vy_list)
    }


def analyze_trajectory(traj: dict) -> None:
    """Computes and prints key flight metrics using vectorized NumPy operations."""
    t = traj["time"]
    x = traj["x"]
    y = traj["y"]
    vx = traj["vx"]
    vy = traj["vy"]
    
    speeds = np.sqrt(vx**2 + vy**2)
    max_height_idx = np.argmax(y)
    
    print("\n" + "="*40)
    print(" FLIGHT SIMULATION SUMMARY")
    print("="*40)
    print(f"Total Flight Time   : {t[-1]:.2f} s")
    print(f"Maximum Range (X)   : {x[-1]:.2f} m")
    print(f"Maximum Height (Y)  : {y[max_height_idx]:.2f} m (at t = {t[max_height_idx]:.2f} s)")
    print(f"Maximum Speed       : {np.max(speeds):.2f} m/s")
    print(f"Impact Speed        : {speeds[-1]:.2f} m/s")
    print("="*40 + "\n")


def plot_trajectory(traj: dict) -> None:
    """Plots the trajectory if matplotlib is available."""
    if not HAS_MATPLOTLIB:
        print("Note: 'matplotlib' is not installed. Skipping graphical plot.")
        return
        
    plt.figure(figsize=(10, 5))
    plt.plot(traj["x"], traj["y"], label="Trajectory (with drag)", color="tab:blue", lw=2)
    plt.title("2D Kinematic Trajectory & Parabolic Flight Simulator")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Height (m)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.axhline(0, color="black", linewidth=1)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    try:
        # Collect configuration parameters interactively from terminal
        v0, angle, mass, drag = get_user_inputs()
        
        print(f"\nRunning simulation for v0={v0}m/s, angle={angle}°, mass={mass}kg, drag={drag}...")
        
        # Run simulation and analyze
        trajectory_data = simulate_flight(
            v0=v0, 
            angle_deg=angle, 
            mass=mass, 
            drag_coeff=drag, 
            dt=0.01
        )
        
        analyze_trajectory(trajectory_data)
        plot_trajectory(trajectory_data)
        
    except Exception as e:
        print(f"\nError during simulation execution: {e}")