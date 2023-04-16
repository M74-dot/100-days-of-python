class AddDigits:
    def __init__(self,num):
        self.num = num

    def add_digits(self):
        new_num = str(self.num)
        first_digit = new_num[0]
        second_digit = new_num[1]
        return int(first_digit) + int(second_digit)


number = int(input("Enter any 2 digit number: \n"))

obj = AddDigits(number)
result = obj.add_digits()
print(result)
