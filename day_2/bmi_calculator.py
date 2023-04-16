class BMICalculator:
    def __init__(self,w,h):
        self.w = w
        self.h = h

    def calculate_bmi(self):
        return self.w // (self.h ** 2)
        

weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in m: '))

manisha_bmi = BMICalculator(weight, height)
bmi = manisha_bmi.calculate_bmi()
print(f"Your Body Mass Index is: {bmi}")
