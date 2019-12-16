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
    def transponse(matrix):
        pom=[]
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                pom[x].append(matrix[y][x])
        return pom

matr = matrix.create(3,5)
n = matrix.fill_random(matr,5,9)
z = matrix.transponse(matr)
matrix.print(z)





