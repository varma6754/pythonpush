
from datetime import datetime

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

total = 0
orders = []

# First order

print("Choose the food type:")
print("1. breakfast\n2. lunch\n3. dinner")

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

else:
    print("Invalid food type")
    exit()

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

    else:
        print("Please enter y or n")

# Final Bill

subtotal = total
discount = 0
gst = 0
grand_total = subtotal - discount + gst

print("\n")
print("=" * 48)
print("              QSPIDER RESTAURANT")
print("             Good Food • Good Mood")
print("              Chennai, Tamil Nadu")
print("=" * 48)

print("                 CASH BILL")
print("-" * 48)

print("Bill No :", "QS-001")
print("Date    :", datetime.now().strftime("%d-%m-%Y"))

print("-" * 48)

print(f"{'Item':<15}{'Rate':<10}{'Qty':<6}{'Amount':<10}")
print("-" * 48)

for i in orders:
    print(f"{i[0]:<15}{i[2]:<10}{i[1]:<6}{i[1] * i[2]:<10}")

print("-" * 48)

print(f"{'Subtotal':<30} Rs. {subtotal:.2f}")
print(f"{'Discount':<30} Rs. {discount:.2f}")
print(f"{'GST':<30} Rs. {gst:.2f}")

print("-" * 48)

print(f"{'GRAND TOTAL':<30} Rs. {grand_total:.2f}")

print("=" * 48)
print("\n          Thank You! Visit Again")
print("   Powered by QSpider Restaurant Billing")
print("=" * 48)
