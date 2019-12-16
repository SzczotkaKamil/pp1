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


n = matrix.create_unit(5)
matrix.print(n)
