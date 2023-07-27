import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Generate data for visualization
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Line plot
plt.figure()
plt.plot(x, y1, label="sin(x)", color='b', linestyle='-', linewidth=2)
plt.plot(x, y2, label="cos(x)", color='r', linestyle='--', linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine and Cosine Functions")
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot
x_data = np.random.rand(50)
y_data = np.random.rand(50)
sizes = np.random.randint(30, 100, size=50)
colors = np.random.rand(50)
plt.figure()
plt.scatter(x_data, y_data, s=sizes, c=colors, alpha=0.7)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Random Scatter Plot")
plt.colorbar(label="Color Intensity")
plt.grid(True)
plt.show()

# Bar chart
x_categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 50, 75, 100]
plt.figure()
plt.bar(x_categories, values, color='g')
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart Example")
plt.grid(axis='y')
plt.show()

# Histogram
data = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(data, bins=30, edgecolor='black', color='c', alpha=0.7)
plt.xlabel("Data")
plt.ylabel("Frequency")
plt.title("Histogram of Random Data")
plt.grid(True)
plt.show()

# Pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title("Pie Chart Example")
plt.show()
