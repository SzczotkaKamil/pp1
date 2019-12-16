import random
class matrix():

    @staticmethod
    def create(x,y):
        matrix = []
        value = 0
        for i in range(x):
            row = [value]*y
            matrix.append(row)
        return matrix
    @staticmethod
    def create_unit(x):
        value = 0
        matrix=[]
        for i in range(x):
            row = [value]*x
            matrix.append(row)
        return matrix


    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
    def fill_random(matrix,m,n):

        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                wartosc = random.randrange(m,n)
                matrix[x][y]=wartosc
        return matrix


matr = matrix.create(3,5)
n = matrix.fill_random(matr,5,9)
matrix.print(n)




