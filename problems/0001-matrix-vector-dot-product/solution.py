import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	m = len(a[0])
	n = len(a)
	m1 = len(b)

	if m != m1:
		return -1
	else:
		return [np.dot(a[i], b) for i in range(n)]