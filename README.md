# 🎢 Triple Pendulum Simulation

This project simulates the chaotic motion of a **triple pendulum** using Python.  
It numerically integrates the equations of motion and generates a dynamic animation showing the complex behavior of the system.

---

## 🎯 Overview

The **triple pendulum** is a classic example of a deterministic but chaotic physical system — small changes in initial conditions can lead to vastly different outcomes.

This Python script:
- Defines physical parameters (mass, length, gravity) directly in the code.
- Solves the nonlinear differential equations of motion.
- Produces an **animated visualization** of the three pendulums in motion using `matplotlib`.

---

## 🧮 Features

- 🧩 Hardcoded system parameters for simplicity  
- ⚙️ Numerical integration using `scipy.integrate.odeint`  
- 🎥 Real-time animation using `matplotlib.animation`  
- 🌈 Adjustable number of frames and simulation time  

---

## 🧠 Dependencies

Make sure you have the following Python packages installed:

```bash
pip install numpy matplotlib scipy
