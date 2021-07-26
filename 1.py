a = [[3,5,4,1],[3,5,2,6],[6,3,5,2]]
b =[[1,2,3,4],[2,3,4,5],[3,4,5,6]]

class Matrix:

    def __init__(self,lists):
        self.lists = lists

    def __str__(self):
        return  '\n'.join(map(str,self.lists))
    
    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists)):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str,c))
matrix1 = Matrix(a)
matrix2 = Matrix(b)

print(matrix1, '\n')
print(matrix2, '\n')
print(matrix1 + matrix2)