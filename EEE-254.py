A function is important in programming because it helps organize, reuse, and manage codes more effectively.   

An example of a simple function is this:


def euclidean_distance(x1, y1, x2, y2):
 try:
  # Type casting inputs(strings) as floats
 x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
 except ValueError:
 return "Invalid input: coordinates must be numbers."
 # Calculate and return the Euclidean distance
 return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

