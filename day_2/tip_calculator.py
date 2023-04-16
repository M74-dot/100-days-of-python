class TipCalculaor:
    def __init__(self, total_bill, per_tip, total_people):
        self.total_bill = total_bill
        self.per_tip = per_tip
        self.total_people = total_people

    def calculate_tip(self):
        tip = (total_bill * (per_tip / 100) + total_bill) / total_people
        print(f"Each person should pay: ${tip:.2f}")


print('-- Welcome to the tip calculator --\n')
total_bill = float(input('What was the total bill.? $'))
per_tip = int(input('What percentage tip would you like to give.? 10, 12, or 15? '))
total_people = int(input('How many people to split the bill.? '))

group1 = TipCalculaor(total_bill, per_tip, total_people)
group1.calculate_tip()
