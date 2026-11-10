# kinematic-trajectory-engine
Numerical simulation of 2D projectile motion under quadratic air resistance.

## Overview / Value Proposition
Manual physics calculations and basic kinematic formulas often fail to capture real-world environmental factors like aerodynamic drag, leading to inaccurate flight path estimations. This utility solves that friction by providing a reliable, terminal-configurable simulation engine that computes discrete time-step trajectories, velocity vectors, and peak flight metrics using vectorized array operations.

## Under the Hood / How It Works
The execution pipeline operates on iterative numerical integration using a fixed time step ($\Delta t = 0.01\text{ s}$). 
1. **Parameter Initialization:** Collects initial velocity ($v_0$), launch angle ($\theta$), projectile mass ($m$), and drag coefficient ($c_d$) with input validation.
2. **Velocity & Drag Resolution:** Decomposes initial velocity into horizontal and vertical vector components using `math.cos()` and `math.sin()`. At each time step, quadratic drag force is computed dynamically based on instantaneous speed magnitude:
   $$F_{\text{drag}} = c_d \cdot v \cdot v_i$$
3. **State Iteration:** Updates accelerations ($a_x, a_y$), velocities, and spatial coordinates until the projectile impacts the ground ($y \le 0$).
4. **Vectorized Analytics:** Stores temporal states in pre-allocated structures and converts them into NumPy arrays to evaluate peak height, total flight duration, and impact velocities efficiently.

## Key Features
* **Terminal Parameter Configuration:** Guided input prompts with robust exception handling and numeric boundary checks.
* **Quadratic Air Resistance Modeling:** Realistic drag calculations accounting for mass and velocity magnitude across flight time.
* **Vectorized NumPy Analytics:** Post-processing summaries utilizing NumPy array operations for maximum computational efficiency.
* **Optional Graphical Rendering:** Graceful fallback visualization via Matplotlib when installed, or plain-text summaries if absent.

## Tech Stack & Core Dependencies Breakdown
* **Python 3.10+:** Core runtime environment utilizing type hints (`tuple`, `dict`) and robust exception handling.
* **NumPy:** Handles high-performance array storage, indexing, and statistical evaluations (`np.argmax`, `np.sqrt`, `np.max`).
* **Math Module:** Provides trigonometric calculations (`math.sin`, `math.cos`) and hypotenuse evaluation (`math.hypot`).
* **Matplotlib (Optional):** Generates 2D trajectory plots comparing spatial coordinates against time.

## Environment & Web-Based Quick Start

### Running via GitHub Codespaces (Browser-Only)
1. Open your repository on GitHub, click the **Code** dropdown, and select the **Codespaces** tab.
2. Launch a new codespace environment. Once the terminal loads, verify your Python version:
   ```bash
   python3 --version
   ```
3. Install project dependencies:
    ```bash
   pip install numpy matplotlib
   ```
4. Execute the simulation script:
    ```bash
    python3 main.py
   ```

### Local Virtual Environment Setup (venv)
```bash
# Clone the repository
git clone [https://github.com/username/kinematic-trajectory-engine.git](https://github.com/username/kinematic-trajectory-engine.git)
cd kinematic-trajectory-engine

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies and run
pip install numpy matplotlib
python main.py
```

## Repository Structure
```bash
kinematic-trajectory-engine/
├── .github/
│   └── workflows/
│       └── ci.yml             # Automated code health and syntax checks
├── .gitignore                 # Optimized Python ignore rules
├── README.md                  # Comprehensive technical documentation
└── main.py                    # Core simulation engine and entry point
```

## Roadmap

**[ ]Type Stubs & Strict Typing:** Introduce comprehensive type annotations and mypy configuration for strict static analysis compliance.

**[ ]Async Batch Simulations:** Implement asynchronous worker tasks using asyncio to process multiple trajectory parameter sets concurrently.

**[ ]Structured Logging:** Replace terminal print statements with Python's standard logging module configured for JSON output formatting.