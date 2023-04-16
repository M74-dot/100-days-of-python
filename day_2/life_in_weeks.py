# 1 year = 52 weeks

class RemainingWeeks:
    def __init__(self, age):
        self.age = age

    def calculate_weeks(self):
        remaining_years = 90 - self.age
        remaining_days = remaining_years * 365
        remaining_weeks = remaining_years * 52
        remaining_months = remaining_years * 12
        print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")


age = int(input('Ener your age: '))
manisha_weeks = RemainingWeeks(age)
manisha_weeks.calculate_weeks()
