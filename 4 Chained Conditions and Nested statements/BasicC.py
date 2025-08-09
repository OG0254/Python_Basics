print('--- Weather Outfit Advisor ---\n')
temp = float(input("Ask user to enter temperature in celsius: "))
season = str(input("Is it raining? (yes/no): ")).strip().lower()

if season == 'no':
    if temp >= 25:
        if temp <= 35:
            print('suggest wearing shorts and a t-shirt')
    else:
        if temp >= 15:
            if temp <= 24:
                print('suggest wearing a light jacket')
        else:
            if temp >= 0:
                print('suggest a warm coat')
if season == 'yes':
    if temp >= 25:
        print('suggest light clothes and an umbrella')
    else:
        if temp <= 15 and temp >= 0:
            print('suggest a warm coat')
            print('suggest carrying an umbrella')
