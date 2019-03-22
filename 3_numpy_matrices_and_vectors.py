import numpy as np

image = np.matrix('0,0,1,0,0; 0,0,1,0,0; 1,1,1,1,1; 0,0,1,0,0; 0,0,1,0,0')
print(image)

#[[0 0 1 0 0]
# [0 0 1 0 0]
# [1 1 1 1 1]
# [0 0 1 0 0]
# [0 0 1 0 0]]

print(" ")

rows = image.shape[0] # 5
columns = image.shape[1] # 5
print("Matrix shape", rows, columns, "\n") # 5 5

#range(value) => go up from 0 to value

# Nested Loop through matrix using range()
for row in range(rows):
    for column in range(columns):
        if image[row,column]==0:
            image[row,column] = 1
        else:
            image[row,column] = 0

print("Reversed image\n", image)
print()
print("Rotated image\n", image.T, "\n")
print(image.flatten())


#[[1 1 0 1 1]
# [1 1 0 1 1]
# [0 0 0 0 0]
# [1 1 0 1 1]
# [1 1 0 1 1]]

###########################################################################
###########################################################################

                        # NUMPY ARRAYS #
                        
###########################################################################
###########################################################################
    

#Numpy Basic Functions:
    # import numpy as np
        # np.array()
        # np.zeros()
        # np.ones()
        # np.arange()
        # np.linspace()

# Numpy Select specified values
    # array[startIndex:EndIndex:Step)
    # Negative values show the reversed array e. g.
        # array = np.arange(10)
        # array[10::-1]
        # [10 9 8 7 6 5 4 3 2 1 0]

    # np.amin(array)
    # np.amax(array)
    # np.average(array)

# Modify arrays wihth Numpy
    # np.append(array, newElement(s))
    # np.insert(array, insertIndex, element(s))
    # np.delete(array, deleteIndex)
    # You can mutiply, substract, add arrays!
        # array * 2
        # [0 2 4 6 8 10 12 14 16 18 20]
    # np.add(array, arrayOfValuestToAdd)
        # np.add(array, [5, 6, 8, 9, 2, 0, 2,3,4,5,1])

#Sort arrays in Numpy ascending and descending
    # np.sort(array)
    # Reverse sort (Descending)
        # -np.sort(array)

# Index of Max and Min value in an array
    # np.argmax(array)
    # np.argmin(array)

###########################################################################
###########################################################################

                        # NUMPY MATRICES #
                        
###########################################################################
###########################################################################

# Create a matrix in Numpy
    # np.matrix([arrays]) e.g.
        # np.matrix([[1,2,3,4], [3,4,5,6], [6,20,18,73], [106,24,63,88]]) or
        # np.matrix('1,2,3,4; 3,4,5,6; 6,20,18,73; 106,24,63,88')
        # [[  1   2   3   4]
        #  [  3   4   5   6]
        #  [  6  20  18  73]
        #  [106  24  63  88]]
    # np.zeros([amountOfRows, amountOfColumns])
    # np.ones([amountOfRows, amountOfColumns])
        # [[1. 1. 1. 1. 1. 1.]
        #  [1. 1. 1. 1. 1. 1.]
        #  [1. 1. 1. 1. 1. 1.]
        #  [1. 1. 1. 1. 1. 1.]
        #  [1. 1. 1. 1. 1. 1.]]

# Select specific values in matrix
    # Instead of matrix[0][3] type
    # matrix[0, 3]
    # Use : to select more than one value
        # matrix = np.matrix('1,2,3,4; 5,6,7,8; 9,10,11,12; 13,14,15,16')
        # # matrix[0, 1:3] => [2 3]

# matrix.size => Length
# matrix.shape => Dimension e. g. 4x4, 5x5 etc.
# np.amax(matrix) == matrix.amax()
# np.amin(matrix) == matrix.amin()
# np.average(matrix) == matrix.mean()

# Modify matrices
    # matrix[0] = [1, 2, 3, 4]
    # matrix[0, 2] = 10
    # np.sort(matrix) & -np.sort(-matrix)
    # Switch rows and colums
        # matrix.T
    # Make a flat matrix
        # matrix.flatten() => [[ 3  4  9 20  5  6  7  8  9  3 11 12 13 14 15 16]]
    # np.add(matrix1, matrix2)
    # Multiply two matrices
        # np.matmul(matrix1, matrix2)
