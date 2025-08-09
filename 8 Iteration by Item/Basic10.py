#  Assignment:

# You have a list of laptop brands.
# Print only the brands whose names have exactly 6 letters in them, and display them with their index

laptops = ['Lenovo', 'ASUS', 'Dell', 'Acer', 'Huawei', 'HP', 'Toshiba']
for index, laptop in enumerate(laptops, start=1):
    if len(laptop) == 6:
        print(f'{index} . {laptop}')
