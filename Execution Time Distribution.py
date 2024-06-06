import matplotlib.pyplot as plt

before_execution_times = []
after_execution_times = []

# Read the txt file
with open('C:/Users/carlo/Downloads/before_ekf_execution_time.txt', 'r') as file1:
    lines1 = file1.readlines()

# Extract execution times
for line in lines1:
    # Find the part between the colon and 'ms' in the line and convert it to a float
    time_str = line.split(':')[1].strip().split()[0]
    before_execution_times.append(float(time_str))

# Read the txt file
with open('C:/Users/carlo/Downloads/3ekf_execution_time.txt', 'r') as file2:
    lines2 = file2.readlines()

# Extract execution times
for line in lines2:
    # Find the part between the colon and 'ms' in the line and convert it to a float
    time_str = line.split(':')[1].strip().split()[0]
    after_execution_times.append(float(time_str))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the distribution before the outlier filter
ax.hist(before_execution_times, bins=50, color='blue', alpha=0.5, label='Before')

# Plot the distribution after the outlier filter
ax.hist(after_execution_times, bins=50, color='green', alpha=0.5, label='After')

# Set title and labels
ax.set_title('Execution Time Distribution Before and After Eigen Parallelization (2 threads)')
ax.set_xlabel('Execution Time (ms)')
ax.set_ylabel('Frequency')

# Add legend
ax.legend()

# Show the plot
plt.tight_layout()
plt.savefig('C:/Users/carlo/Downloads/ekf_distribution_execution_time.pdf', bbox_inches='tight')
plt.show()
