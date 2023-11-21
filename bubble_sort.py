matrix = [0, -1, -15, 13, 100, 123, 32, -23, 2, 0, 2, 2, 3, 112]

def bubble_sort(matrix):
    length = len(matrix)
    for i in range(length-1):
        for j in range(length-1):
            if matrix[j] > matrix[j+1]:
                matrix[j], matrix[j+1] = matrix[j+1], matrix[j]


if __name__ == "__main__":
    bubble_sort(matrix=matrix)