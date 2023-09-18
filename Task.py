#Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.

#семинар 13 задача 1

import logging

logging.basicConfig(level=logging.DEBUG)

class MatrixComparisonError(Exception):
    def __init__(self, message):
        super().__init__(message)

class MatrixAdditionError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Matrix:
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix
        self.logger = logging.getLogger(__name__)

    def print(self):
        matrixString = ""
        for i in range(len(self.matrix)):
            matrixString = matrixString + '  '.join(map(str, self.matrix[i])) + "\n"
        return matrixString
    
    def comparison(self, other):
        if not isinstance(other, Matrix):
            error_message = "Второй операнд должен быть матрицей"
            self.logger.error(error_message)
            raise MatrixComparisonError(error_message)
            
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            error_message = "Матрицы должны быть одинакового размера"
            self.logger.error(error_message)
            raise MatrixComparisonError(error_message)
    
        if self.matrix > other.matrix:
            self.logger.info("Первая матрица больше второй")
            return "Первая матрица больше второй"
        elif self.matrix < other.matrix:
            self.logger.info("Вторая матрица больше первой")
            return "Вторая матрица больше первой"
        else:
            self.logger.info("Матрицы равны")
            return "Матрицы равны"
    
    def __add__(self, other):
        if not isinstance(other, Matrix):
            error_message = "Второй операнд должен быть матрицей"
            self.logger.error(error_message)
            raise MatrixAdditionError(error_message)

        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            error_message = "Матрицы должны быть одинакового размера"
            self.logger.error(error_message)
            raise MatrixAdditionError(error_message)
    
        result = []
        numbers = []

        for i in range(len(self.matrix)): 
            for j in range(len(self.matrix[i])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                numbers.append(summa)
                
                if len(numbers) == len(self.matrix[i]):
                    result.append(numbers)
                    numbers = []

        return result
    
matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(matrix1.print())
matrix2 = Matrix([[7, 8, 9], [1, 2, 3]])
print(matrix2.print())

try:
    print(matrix1 + matrix2)
except MatrixAdditionError as e:
    print(f"Ошибка сложения матриц: {str(e)}")

try:
    print(matrix1.comparison(matrix2))
except MatrixComparisonError as e:
    print(f"Ошибка сравнения матриц: {str(e)}")