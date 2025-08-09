brands = ['Oppo', 'Apple', 'Asus', 'Intel',
          'HP', 'Acer', 'Uber', 'Oracle', 'IBM']

for index, brand in enumerate(brands, start=1):
    if brand[0].lower() in 'aeiou':
        if len(brand) == 5:
            print(f'{index}. {brand}')
