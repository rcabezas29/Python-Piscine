class   Vector:
    def __init__(self, vec) -> None:
        if type(vec) == int:
            self.shape = (vec, 1)
            self.values = []
            for i in range(vec):
                self.values.append([float(i)])
        elif type(vec) == list:
            self.values = vec
            self.shape = (len(vec), len(vec[0]))
            assert self.shape[0] == 1 or self.shape[1] == 1, 'Invalid vector'
        elif type(vec) == tuple:
            assert vec[1] > vec[0], 'Invalid tuple to create vector'
            self.shape = (vec[1] - vec[0], 1)
            self.values = []
            for i in range(vec[0], vec[1]):
                self.values.append([float(i)])

    def dot(self, other):
        '''Returns the dot product of two veectors of the same shape'''
        assert self.shape == other.shape, 'Not able to dot product between vectors with different shapes'
        dot_product = 0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                dot_product += self.values[i][j] * other.values[i][j]
        return dot_product

    def T(self):
        '''Transposes the vector from a column vector to a row vector and viceversa'''
        transposed_matrix = [[0 for _ in range(self.shape[0])] for _ in range(self.shape[1])]

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                transposed_matrix[j][i] = self.values[i][j]
        return Vector(transposed_matrix)

    def __add__(self, other):
        assert self.shape == other.shape, 'Not able to dot product between vectors with different shapes'

        m = [[0 for _ in range(self.shape[1])] for _ in range(self.shape[0])]

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                m[i][j] = self.values[i][j] + other.values[i][j]
        return Vector(m)


    def __radd__(self, other):
        assert self.shape == other.shape, 'Not able to dot product between vectors with different shapes'

        m = [[0 for _ in range(self.shape[1])] for _ in range(self.shape[0])]

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                m[i][j] = self.values[i][j] + other.values[i][j]
        return Vector(m)

    def __sub__(self, other):
        assert self.shape == other.shape, 'Not able to dot product between vectors with different shapes'

        m = [[0 for _ in range(self.shape[1])] for _ in range(self.shape[0])]

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                m[i][j] = self.values[i][j] - other.values[i][j]
        return Vector(m)

    def __rsub__(self, other):
        assert self.shape == other.shape, 'Not able to dot product between vectors with different shapes'

        m = [[0 for _ in range(self.shape[1])] for _ in range(self.shape[0])]

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                m[i][j] = self.values[i][j] - other.values[i][j]
        return Vector(m)


    def __truediv__(self, n):
        ''''''
        if n == 0:
            raise ZeroDivisionError("division by zero.")
        m = [[0 for _ in range(self.shape[1])] for _ in range(self.shape[0])]

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                m[i][j] = self.values[i][j] / n
        return Vector(m)

    def __rtruediv__(self, n):
        ''''''
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __mul__(self, n):
        ''''''
        m = [[0 for _ in range(self.shape[1])] for _ in range(self.shape[0])]

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                m[i][j] = self.values[i][j] * n
        return Vector(m)

    def __rmul__(self, n):
        ''''''
        m = [[0 for _ in range(self.shape[1])] for _ in range(self.shape[0])]

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                m[i][j] = self.values[i][j] * n
        return Vector(m)

    def __str__(self) -> str:
        return f'Vector({self.values})'
    def __repr__(self) -> str:
        return f'Vector({self.values})'

