'''Requirements:
1. Create a dictionary containing 5 products and their prices.
2. Ask the customer to enter a product name.
3. Ask for the quantity.
4. Calculate the product total.
5. Add it to the overall bill.
6. Ask whether the customer wants to add another product.
7. If the product is invalid, ask again.
8. Finally, display the total shopping bill.'''


products={'apple':10,'tomato':5,'banana':6,'orange':10,'carrot':5}
grand_total=0
cart=[]

while True:
    product_name=input("enter the product name: ")

    if product_name in products:
        p_n=products.get(product_name)
        quantity=int(input("enter the quantity: "))
        total=p_n*quantity

        i=0
        found=False

        while i<len(cart):
            if cart[i][0]==product_name:
                found=True
                cart[i][1]=cart[i][1]+quantity
                cart[i][2]=cart[i][1]*p_n
                break
            i=i+1

        if found==False:
            cart.append([product_name,quantity,total])

        repeat=input("do you want to add any other (yes/no): ")

        if repeat=='yes':
            continue
        else:
            break
    else:
        print("invalid products")
        continue

i=0

print("--------- SHOPPING BILL ---------")
print("Product      Quantity      Total")

while i<len(cart):
    print(cart[i][0],"       ",cart[i][1],"       ",cart[i][2])
    grand_total=grand_total+cart[i][2]
    i=i+1

print("--------------------------------")
print("Grand Total:",grand_total)