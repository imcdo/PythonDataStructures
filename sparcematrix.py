from datastructures import *
# import datastructures

class MissMatchingBoundsException (Exception):
    pass

class Matrix:
    def __init__(self, r=0, c=0):
        self.r = r
        self.c = c
        self.matrix = [[0 for __ in range(c)] for _ in range(r)]

    def __add__(self, rhs):
        if self.r != rhs.r or self.c != rhs.c: 
            raise MissMatchingBoundsException()

        mat = Matrix(self.r, self.c)

        for r in range(self.r):
            for c in range(self.c):
                mat.matrix[r][c] = self.matrix[r][c] + rhs.matrix[r][c]

        return mat

    def __mul__(self, rhs):
        if self.c != rhs.r:
            raise MissMatchingBoundsException()

        mat = Matrix(self.r, rhs.c)

        for r1, row1 in enumerate(self.matrix):
            for r2, row2 in enumerate(rhs.matrix):
                for c in range(rhs.c):
                    mat[r1][c] += row1[r2] * row2[c]
        return mat
    def __getitem__(self, idx):
        return self.matrix[idx]


    # def __hash__(self):
    #     hash = 0
    #     for r in self.matrix:
    #         hash += hash((*r,))




class SparceMatrix: 
    class data:
        def __init__(self, col, data):
            self.col = col
            self.data = data


    def __init__(self, r=0, c=0):
        self.matrix = LinkedList()

    def __add__(self, rhs):
        raise NotImplementedError()

    def __mul__(self, rhs):
        raise NotImplementedError()

