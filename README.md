# Euclidean Distance Calculator

This Python script calculates the minimum Euclidean distance between pairs of points in a 2D space.

### Description

The script includes:
1. **Point Definition**: A list of points in 2D space, each represented by a tuple (x, y).
2. **Euclidean Distance Function**: A function `euclideanDistance` that calculates the Euclidean distance between two points using the formula:

   \[
   d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
   \]

3. **Distance Calculation**: Using a nested loop, the script calculates the Euclidean distance between each unique pair of points and stores these distances in a list.
4. **Minimum Distance**: Finally, the script finds and prints the minimum distance from the list of calculated distances.

### How to Run

1. Ensure Python is installed on your system.
2. Clone the repository or download the `euclidean_distance.py` file.
3. Run the script from the command line with:

   ```bash
   python euclidean_distance.py
