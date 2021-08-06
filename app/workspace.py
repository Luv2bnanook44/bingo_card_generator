from itertools import product

coordinates = list(product('01234', '01234'))

for x, y in coordinates:
    print(x,y)