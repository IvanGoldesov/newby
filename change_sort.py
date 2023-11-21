matrix = [0, -1, -15, 13, 100, 123, 32, -23, 2, 0, 2, 2, 3, 112]

def change_sort(matrix):
    length = len(matrix)
    for i in range(length-1):
        minim = matrix[i]
        ind = i
        for j in range(i+1, length):
            if minim > matrix[j]:
                minim = matrix[j]
                ind = j

        if ind != i:
            k = matrix[i]
            matrix[i] = minim
            matrix[ind] = k

#change_sort(matrix)
#print(matrix)
