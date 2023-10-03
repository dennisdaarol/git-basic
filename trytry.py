# display the number that has the most instance
x = [1,2,1,4,2,1,1,3]

"""most = max(set(x), key=x.count)
counter = x.count(1)
print(most)
print(counter)"""

# Args and Kwargs
"""def order_pizza(size, *toppings, **details):
    print(f'Ordered a {size} piza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')
    print(details)
    print(f'details of the order:')
    for key, value in details.items():
        print(f'- {key} : {value}')

order_pizza('large', 'cheeze', 'pineapple', 'ham', takeout=True, tip=5)"""

x = int('1234567'[6])
y = -round(2.1)
z = x//y
print(z)
print("origin 1")
