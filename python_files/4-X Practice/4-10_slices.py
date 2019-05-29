pizzas = ["pepperoni", "sausage", "cheese", "bacon", "veggie"]
print("The first three items in the list are:")
for pizza in pizzas[:]:
    print(pizza)

print("The three items in the middle of the list are:")
for pizza in pizzas[1:4]:
    print(pizza)

print("The last three items in the list are:")
for pizza in pizzas[-3:]:
    print(pizza)