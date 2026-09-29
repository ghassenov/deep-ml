import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.shape != v2.shape or v1.size == 0 or v2.size == 0:
		raise ValueError('error')
	else:
		n1 = np.linalg.norm(v1,ord=2)
		n2 = np.linalg.norm(v2,ord=2)
		dt = np.dot(v1,v2)
		return float(dt/(n1*n2))
