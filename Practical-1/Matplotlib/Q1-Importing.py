import matplotlib.pyplot as plt

# Import necessary modules from Matplotlib for plotting
# Configure plot elements like labels, titles, and grid lines
plt.figure(figsize=(10, 6))
plt.title('Sample Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

# Plot some sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 320, 40]
plt.plot(x, y, label='Sample Line')

# Display the legend
plt.legend()

# Show the plot
plt.show()
