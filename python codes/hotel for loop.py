
d = {
    'idly': 5,
    'dosa': 20,
    'pongal': 40,
    'upma': 30,
    'puri': 15,
    'meals': 80,
    'fried rice': 120,
    'biriyani': 150,
    'lemon rice': 40,
    'tomato rice': 40
}

print("Welcome to QSpider Restaurant\n")
print(d)

total = 0
orders = []

print("\nChoose the food type:")
print("1. breakfast\n2. lunch\n3. dinner\n")

food_type1 = input("Enter your type: ").lower()

if food_type1 == 'breakfast':
    print("\nBreakfast menu")
    print("1. idly\n2. dosa\n3. pongal\n4. upma\n5. puri")

elif food_type1 == 'lunch':
    print("\nLunch menu")
    print("1. meals\n2. fried rice\n3. biriyani\n4. lemon rice\n5. tomato rice")

elif food_type1 == 'dinner':
    print("\nDinner menu")
    print("1. idly\n2. dosa\n3. pongal\n4. upma\n5. puri")

items1 = input("Item: ").lower()
quantity1 = int(input("Enter the quantity: "))

amt = d[items1] * quantity1
total = total + amt

orders.append((items1, quantity1, d[items1]))

# Additional orders

while True:

    item2 = input("\nStill you think you want to order y/n: ").lower()

    if item2 == 'y':

        print("\n----------- FULL MENU -----------")

        for i in d:
            print(i, "-", d[i])

        items2 = input("\nItem: ").lower()
        quantity2 = int(input("Enter the quantity: "))

        amt2 = d[items2] * quantity2
        total = total + amt2

        orders.append((items2, quantity2, d[items2]))

    elif item2 == 'n':
        break

# Final Bill

print("\n========== BILL ==========")

for i in orders:

    print("\nOrder:", i[0])
    print("Quantity:", i[1])
    print("Single item price:", i[2], "rupees")
    print("Total item price:", i[1] * i[2], "rupees")

print("\n--------------------------")
print("Grand total:", total, "rupees")
print("--------------------------")

print("Thank you for visiting our restaurant!")
