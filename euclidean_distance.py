
# Define points in a 2D space
points = [(2, 3), (4, 5), (7, 8), (1, 1)]  # You can add more points to this list if needed

# Euclidean Distance Function
def euclideanDistance(point1, point2):
    # Unpack coordinates from the points
    x1, y1 = point1
    x2, y2 = point2
    # Calculate the Euclidean distance between two points
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

# Calculate distances between each pair of points
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        # Calculate the distance between two points and add it to the distances list
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Find the minimum distance from the distances list
min_distance = min(distances)

# Print the minimum distance
print("Minimum distance:", min_distance)
