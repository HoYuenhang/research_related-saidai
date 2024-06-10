import matplotlib.pyplot as plt
import seaborn as sns

execution_times_1 = []
execution_times_2 = []
execution_times_3 = []
execution_times_4 = []

# Read the txt file
with open('C:/Users/12578/Downloads/1ekf_execution_time.txt', 'r') as file1:
    lines1 = file1.readlines()

# Extract execution times
for line in lines1:
    # Find the part between the colon and 'ms' in the line and convert it to a float
    time_str = line.split(':')[1].strip().split()[0]
    execution_times_1.append(float(time_str))

# Read the txt file
with open('C:/Users/12578/Downloads/dynamic_ekf_execution_time.txt', 'r') as file2:
    lines2 = file2.readlines()

# Extract execution times
for line in lines2:
    # Find the part between the colon and 'ms' in the line and convert it to a float
    time_str = line.split(':')[1].strip().split()[0]
    execution_times_2.append(float(time_str))

# Read the txt file
with open('C:/Users/12578/Downloads/2ekf_execution_time.txt', 'r') as file3:
    lines3 = file3.readlines()

# Extract execution times
for line in lines3:
    # Find the part between the colon and 'ms' in the line and convert it to a float
    time_str = line.split(':')[1].strip().split()[0]
    execution_times_3.append(float(time_str))

# Read the txt file
with open('C:/Users/12578/Downloads/3ekf_execution_time.txt', 'r') as file4:
    lines4 = file4.readlines()

# Extract execution times
for line in lines4:
    # Find the part between the colon and 'ms' in the line and convert it to a float
    time_str = line.split(':')[1].strip().split()[0]
    execution_times_4.append(float(time_str))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the KDE of all four sets of execution times with more distinct colors
sns.kdeplot(execution_times_1, ax=ax, color='#1f77b4', label='No Parallelization', fill=True)  # 蓝色
sns.kdeplot(execution_times_2, ax=ax, color='#ff7f0e', label='Dynamic', fill=True)            # 橙色
sns.kdeplot(execution_times_3, ax=ax, color='#2ca02c', label='2 Threads', fill=True)         # 绿色
sns.kdeplot(execution_times_4, ax=ax, color='#d62728', label='3 Threads', fill=True)         # 红色

# Set title and labels with larger font size
# ax.set_title('Execution Time Distribution for Four Different Sets', fontsize=16)
ax.set_xlabel('Execution Time (ms)', fontsize=16)
ax.set_ylabel('Density', fontsize=16)

# Increase tick label size
ax.tick_params(axis='both', which='major', labelsize=12)

# Add legend
ax.legend(fontsize=12)

# Show the plot
plt.tight_layout()
plt.savefig('C:/Users/12578/Downloads/ekf_distribution_execution_time_kde_4.pdf', bbox_inches='tight')
plt.show()
