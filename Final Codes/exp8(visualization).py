import matplotlib.pyplot as plt

# Input values for the histogram
hist_data = list(map(float, input("Enter values for histogram, separated by spaces: ").split()))

# Input values for the scatter plot
x_values = list(map(float, input("Enter x-values for scatter plot, separated by spaces: ").split()))
y_values = list(map(float, input("Enter y-values for scatter plot, separated by spaces: ").split()))

# Ensure x and y values have the same length for scatter plot
if len(x_values) != len(y_values):
    print("Error: The number of x-values and y-values must be the same for the scatter plot.")
else:
    # Create the plots
    plt.figure(figsize=(10, 4))

    # Histogram
    plt.subplot(1, 2, 1)
    plt.hist(hist_data, bins=10, color='skyblue', edgecolor='black')
    plt.title("Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    # Scatter Plot
    plt.subplot(1, 2, 2)
    plt.scatter(x_values, y_values, color='salmon')
    plt.title("Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    plt.tight_layout()
    plt.show()
