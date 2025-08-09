# Challenge:
# You have a list of car brands. Print out the brands that:

# Start with a consonant

# Have a length of exactly 5 characters

# And convert them to lowercase in the output

cars = ['Audi', 'BMW', 'Volvo', 'Nissan',
        'Ford', 'Chevy', 'Opel', 'Jeep', 'Saab']

for index, car in enumerate(cars, start=1):
    if car[0].lower() in ('bcdfghjklmnpqrstvwxz'):
        if len(car) == 5:
            print(f'{index}. {car.lower()}')
