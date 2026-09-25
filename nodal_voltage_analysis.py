# Python Program to Calculate Nodal Voltages
# Using Nodal Analysis
#
# Basic equation:
# [Y] [V] = [I]
# Therefore:
# [V] = inverse([Y]) * [I]

import numpy as np

print("========================================")
print("       NODAL VOLTAGE CALCULATOR")
print("========================================")

# Number of unknown nodes
n = int(input("Enter number of unknown nodes: "))

# Create admittance matrix and current vector
Y = np.zeros((n, n), dtype=float)
I = np.zeros(n, dtype=float)

print("\nEnter the nodal admittance matrix:")

for i in range(n):
    for j in range(n):
        Y[i][j] = float(
            input(f"Enter Y[{i+1},{j+1}] (Siemens): ")
        )

print("\nEnter the current injection at each node:")

for i in range(n):
    I[i] = float(
        input(f"Enter current I{i+1} (A): ")
    )

# Solve the nodal equations
try:
    V = np.linalg.solve(Y, I)

    print("\n------------- RESULTS ----------------")

    for i in range(n):
        print(f"Node {i+1} Voltage = {V[i]:.4f} V")

    print("--------------------------------------")

except np.linalg.LinAlgError:
    print("\nError: The admittance matrix is singular.")
    print("Check the network and input values.")
