#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 15:38:25 2025

@author: star
"""

import pandas as pd
import os

def save_simulation_results(time, x, x1, y1, x2, y2, x3, y3, theta1_init, theta2_init, theta3_init):
    """
    Save triple pendulum simulation data to a CSV file inside 'results/' folder.
    The filename encodes the initial angles.
    """
    os.makedirs("results", exist_ok=True)
    filename = f"results/results_{theta1_init:.2f}_{theta2_init:.2f}_{theta3_init:.2f}"
    filename = filename.replace('.', 'p').replace('-', 'm')
    filename = filename + ".csv"
    df = pd.DataFrame({
        "time": time,
        "theta1": x[:, 0],
        "theta2": x[:, 1],
        "theta3": x[:, 2],
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2,
        "x3": x3,
        "y3": y3
    })

    df.to_csv(filename, index=False)
    print(f"✅ Saved simulation results to {filename}")
