import math

# Euclidean Distance
def euclidean(x, y):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(x, y)))

# Manhattan Distance
def manhattan(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))

# Supremum Distance (Chebyshev Distance)
def supremum(x, y):
    return max(abs(a - b) for a, b in zip(x, y))

# Cosine Similarity
def cosine_similarity(x, y):
    dot_product = sum(a * b for a, b in zip(x, y))
    magnitude_x = math.sqrt(sum(a ** 2 for a in x))
    magnitude_y = math.sqrt(sum(b ** 2 for b in y))
    return dot_product / (magnitude_x * magnitude_y)

# Jaccard Similarity
def jaccard(x, y):
    set_x, set_y = set(x), set(y)
    return len(set_x & set_y) / len(set_x | set_y)

# Example usage
if __name__ == "__main__":
    x = [1, 3, 5]
    y = [2, 4, 6]

    print("Euclidean Distance:", euclidean(x, y))       # Output: ~1.732
    print("Manhattan Distance:", manhattan(x, y))       # Output: 3
    print("Supremum Distance:", supremum(x, y))         # Output: 1
    print("Cosine Similarity:", cosine_similarity(x, y)) # Output: ~0.999
    print("Jaccard Similarity:", jaccard(x, y))         # Output: 0.0
