import matplotlib.pyplot as plt

# Data
epochs = [1, 2, 3, 4, 5, 6, 7, 8]
or_errors = [1, 2, 1, 1, 0, 0, 0, 0]
and_errors = [1, 3, 2, 2, 1, 0, 0, 0]
nand_errors = [3, 3, 2, 3, 2, 1, 0, 0]
xor_errors = [3, 3, 3, 4, 4, 4, 4, 4]

# Plotting
plt.figure(figsize=(10, 6))

# OR gate errors
plt.plot(epochs, or_errors, label="OR", marker='o')
# AND gate errors
plt.plot(epochs, and_errors, label="AND", marker='o')
# NAND gate errors
plt.plot(epochs, nand_errors, label="NAND", marker='o')
# XOR gate errors
plt.plot(epochs, xor_errors, label="XOR", marker='o')

# Labels and title
plt.xlabel("Epochs")
plt.ylabel("Errors")
plt.title("Training Errors for Logical Gates over Epochs")
plt.legend()

# Display plot
plt.grid(True)
plt.show()
