

import matplotlib.pyplot as plt

# Data
depth = ["Easy", "Medium", "Hard"]
minimax_time = [0.087922, 0.569178, 4.059735]
alpha_beta_time = [0.016000, 0.032009, 0.109383]

# Plotting
plt.plot(depth, minimax_time, marker='o', label='Minimax')
plt.plot(depth, alpha_beta_time, marker='o', label='Alpha-Beta')

# Axis labels and title
plt.xlabel('Depth')
plt.ylabel('Time')
plt.title('Performance of Minimax and Alpha-Beta Algorithms')

# Legend
plt.legend()

# Display the plot
plt.show()

