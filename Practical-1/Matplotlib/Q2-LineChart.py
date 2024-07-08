import matplotlib.pyplot as plt

# Import necessary modules from Matplotlib for plotting
# Configure plot elements like labels, titles, and grid lines
plt.figure(figsize=(10, 6))
plt.title('Line Chart for Numerical Variable Over Time')
plt.xlabel('Time')
plt.ylabel('Numerical Value')
plt.grid(True)

# Plot some sample data
time = [1, 2, 3, 4, 5]
values = [10, 20, 25, 320, 40]
plt.plot(time, values, label='Numerical Variable Over Time')

# Display the legend
plt.legend()

# Show the plot
plt.show()
