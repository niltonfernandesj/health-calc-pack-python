from mimetypes import init

class Person:
    def __init__(self, weight:float = 0.0, height: float = 0.0) -> None:
        self.weight = weight
        self.height = height
        pass

    def calculateBMI(self) -> float:
        '''
        Calculates person`s BMI
        '''

        return self.weight / (self.height * self.height)
        