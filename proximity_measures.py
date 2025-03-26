import math

# Manhattan Distance
def manhattan(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))

# Euclidean Distance
def euclidean(x, y):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(x, y)))

# Jaccard Similarity (for sets)
def jaccard(x, y):
    return len(set(x) & set(y)) / len(set(x) | set(y))

# Cosine Similarity
def cosine_similarity(x, y):
    dot = sum(a * b for a, b in zip(x, y))
    mag_x = math.sqrt(sum(a ** 2 for a in x))
    mag_y = math.sqrt(sum(b ** 2 for b in y))
    return dot / (mag_x * mag_y)

# Supremum Distance (Chebyshev Distance)
def supremum(x, y):
    return max(abs(a - b) for a, b in zip(x, y))

# Example usage
if __name__ == "__main__":
    x = [1, 3, 5]
    y = [2, 4, 6]

    print("Manhattan Distance:", manhattan(x, y))       # Output: 3
    print("Euclidean Distance:", euclidean(x, y))       # Output: ~1.732
    print("Jaccard Similarity:", jaccard(x, y))         # Output: 0.0
    print("Cosine Similarity:", cosine_similarity(x, y)) # Output: ~1.0
    print("Supremum Distance:", supremum(x, y))         # Output: 1
