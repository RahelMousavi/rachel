import random

class Matrix:
    def __init__(self, c, r, data=None):
        self.row = r
        self.column = c
        self.matrix = data if data else self._make_matrix()

    def _make_matrix(self):
        return [[random.randint(0, 100) for _ in range(self.column)] for _ in range(self.row)]

    def __add__(self, other):
        if self.row != other.row or self.column != other.column:
            raise ValueError("Matrices must have same dimensions")
        return Matrix(self.column, self.row, [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.column)] for i in range(self.row)])

    def __sub__(self, other):
        if self.row != other.row or self.column != other.column:
            raise ValueError("Matrices must have same dimensions")
        return Matrix(self.column, self.row, [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.column)] for i in range(self.row)])

    def mul(self, other):
        if self.column != other.row:
            raise ValueError("Matrices not aligned")
        return Matrix(other.column, self.row, [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.column)) for j in range(other.column)] for i in range(self.row)])

    def split(self):
        mr, mc = self.row // 2, self.column // 2
        return (Matrix(mc, mr, [r[:mc] for r in self.matrix[:mr]]),
                Matrix(self.column - mc, mr, [r[mc:] for r in self.matrix[:mr]]),
                Matrix(mc, self.row - mr, [r[:mc] for r in self.matrix[mr:]]),
                Matrix(self.column - mc, self.row - mr, [r[mc:] for r in self.matrix[mr:]]))

    
    def combine(C11, C12, C21, C22):
        top = [C11.matrix[i] + C12.matrix[i] for i in range(C11.row)]
        bottom = [C21.matrix[i] + C22.matrix[i] for i in range(C21.row)]
        return Matrix(C12.column + C11.column, C11.row + C21.row, top + bottom)

    def strassen_mul(self, other):
        if self.column != other.row:
            raise ValueError("Matrices not aligned")
        if self.row <= 2 or self.column <= 2 or other.row <= 2 or other.column <= 2:
            return self.mul(other)

        A11, A12, A21, A22 = self.split()
        B11, B12, B21, B22 = other.split()

        P1 = (A11 + A22).strassen_mul(B11 + B22)
        P2 = (A21 + A22).strassen_mul(B11)
        P3 = A11.strassen_mul(B12 - B22)
        P4 = A22.strassen_mul(B21 - B11)
        P5 = (A11 + A12).strassen_mul(B22)
        P6 = (A21 - A11).strassen_mul(B11 + B12)
        P7 = (A12 - A22).strassen_mul(B21 + B22)

        C11 = P1 + P4 - P5 + P7
        C12 = P3 + P5
        C21 = P2 + P4
        C22 = P1 - P2 + P3 + P6
        return Matrix.combine(C11, C12, C21, C22)

    def print(self, msg="Matrix:"):
        print(msg)
        for row in self.matrix:
            print(row)
        print("-" * 10)


def main():
    m1 = Matrix(8,8)
    m2 = Matrix(8,8)

    m1.print("M1:")
    m2.print("M2:")

    standard_res = m1.mul(m2)
    standard_res.print("Standard Mul:")

    strassen_res = m1.strassen_mul(m2)
    strassen_res.print("Strassen Mul:")
    
main()
