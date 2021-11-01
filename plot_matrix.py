
import numpy as np
import imageio


def generate_random_matrix(m, n):
    random_matrix = np.random.randint(0, 2, (m, n))
    return random_matrix

def save_matrix(matrix, file_name):
    imageio.imsave(file_name, matrix)   

if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")
