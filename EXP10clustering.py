# Import necessary librarie such as numpy pandas
import numpy as np
# Get the number of datapoints from the user
a = int(input("Enter number of datapoints: "))
# Create an empty list to store the datapoints
l = []
# Get each datapoint from the user and store it in the list
for i in range(a):
    b = int(input(f"Enter {i+1}: "))
    l.append(b)
# Print the datapoints
print("Datapoints:", l)
# Set the number of clusters 'k'
K = 2
# Initialize the centroids randomly
c1 = np.random.choice(l)
print("Random 1:", c1)

# Initialize the second centroid to be different from the first
c2 = np.random.choice(l)
while c1 == c2:
    c2 = np.random.choice(l)
print("Random 2:", c2)
# Create empty lists to store the clusters
clus1 = []
clus2 = []
# Assign each datapoint to the closest centroid
for i in range(a):
    # Calculate the distance to each centroid
    d1 = abs(l[i] - c1)
    d2 = abs(l[i] - c2)
    # Assign the datapoint to the closest centroid
    if d1 < d2:
        clus1.append(l[i])
    else:
        clus2.append(l[i])
# Print the clusters
print("Cluster 1:", clus1)
print("Cluster 2:", clus2)