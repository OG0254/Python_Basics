# Print all the laptop names in uppercase if they contain the letter ‘o’ (case insensitive). Also display their position number like you’ve been doing.

laptops = ['Lenovo', 'ASUS', 'Dell', 'Acer', 'Huawei', 'HP', 'Toshiba']
for index, laptop in enumerate(laptops, start=1):
    if 'o' in laptop.lower():
        print(f'{index} . {laptop.upper()}')
