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

print("welcome to qspider restaurant\n")
print(d)

total = 0

print("choose the food type:\n")
print("1. breakfast\n2. lunch\n3. dinner\n")

food_type1 = input("enter your type: ")

if food_type1 == 'breakfast':
    print("\nbreakfast menu")
    print("1. idly\n2. dosa\n3. pongal\n4. upma\n5. puri")

    items1 = input("item: ").lower()
    quantity1 = int(input("enter the quantity: "))
    amt = d[items1] * quantity1

elif food_type1 == 'lunch':
    print("\nlunch menu")
    print("1. meals\n2. fried rice\n3. biriyani\n4. lemon rice\n5. tomato rice")

    items1 = input("item: ").lower()
    quantity1 = int(input("enter the quantity: "))
    amt = d[items1] * quantity1

elif food_type1 == 'dinner':
    print("\ndinner menu")
    print("1. idly\n2. dosa\n3. pongal\n4. upma\n5. puri")

    items1 = input("item: ").lower()
    quantity1 = int(input("enter the quantity: "))
    amt = d[items1] * quantity1


total = amt

# second order in loop
items2 = ""
quantity2 = 0


while True:

    item2 = input("\nstill you think you want to order y/n: ")

    if item2 == 'y':

        print("\nchoose the food type:")
        print("1. breakfast\n2. lunch\n3. dinner")

        food_type2 = input("enter your type: ")

        if food_type2 == 'breakfast':

            print("\nbreakfast menu")
            print("1. idly\n2. dosa\n3. pongal\n4. upma\n5. puri")

            items2 = input("item2: ").lower()
            quantity2 = int(input("enter the quantity: "))
            amt2 = d[items2] * quantity2

        elif food_type2 == 'lunch':

            print("\nlunch menu")
            print("1. meals\n2. fried rice\n3. biriyani\n4. lemon rice\n5. tomato rice")

            items2 = input("item2: ").lower()
            quantity2 = int(input("enter the quantity: "))
            amt2 = d[items2] * quantity2

        elif food_type2 == 'dinner':

            print("\ndinner menu")
            print("1. idly\n2. dosa\n3. pongal\n4. upma\n5. puri")

            items2 = input("item2: ").lower()
            quantity2 = int(input("enter the quantity: "))
            amt2 = d[items2] * quantity2

        total = total + amt2

    elif item2 == 'n':
        break

print("\n----- BILL -----")

print(f"order: {items1}-{quantity1}")

if items2 != "":
    print(f"order: {items2}-{quantity2}")
print(f"total price: {total} rupees")
print("Thank you for visiting our restaurant!")