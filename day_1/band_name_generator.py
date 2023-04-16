class BandNameGenerator:
    def __init__(self, city_name, pet_name):
        self.city_name = city_name
        self.pet_name = pet_name

    def generate_band_name(self):
        print("Your band name could be", self.city_name ,self.pet_name)


print('-- Welcome to Band Name Gnerator --')
city_name = input("What's name of the city you grew up in.?\n")
pet_name = input("What's your pet's name.?\n")
manisha = BandNameGenerator(city_name, pet_name)    
manisha.generate_band_name()
