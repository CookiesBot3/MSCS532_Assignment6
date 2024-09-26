class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    # Insert an element at the specified index
    def insert(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            print("Index out of bounds")

    # Delete an element at the specified index
    def delete(self, index):
        if 0 <= index < self.size:
            self.array[index] = None
        else:
            print("Index out of bounds")

    # Access an element at the specified index
    def access(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            print("Index out of bounds")

class Matrix:
    def __init__(self, rows, cols):
        self.matrix = [[None for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def insert(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[row][col] = value
        else:
            print("Index out of bounds")

    def access(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.matrix[row][col]
        else:
            print("Index out of bounds")

if __name__ == '__main__':
    # Example usage
    arr = Array(5)
    arr.insert(0, 10)
    arr.insert(1, 20)
    print(arr.access(0))  # Output: 10
    arr.delete(1)

    # Example usage
    mat = Matrix(3, 3)
    mat.insert(1, 1, 5)
    print(mat.access(1, 1))  # Output: 5
