import re
from person.Person import Person

class TestBMICalculation:
    
    def test1(self):
        #Arrange
        person = Person(90, 1.80)

        #Act
        result = person.calculateBMI()

        #Assert
        assert result == 27.777777777777775

        pass