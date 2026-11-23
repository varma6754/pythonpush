'''A bus has only 10 available seats. Customers can book tickets until all seats are booked or they choose to exit.
Requirements
1. Initially, available seats = 10.
2. Ask the customer how many seats they want to book.
3. If requested seats are greater than available seats, display Not enough seats available.
4. Otherwise, confirm booking and reduce available seats.
5. Ask whether another customer wants to book.
6. If yes, repeat.
7. If no, stop the booking process.
8. Finally, display booked seats and remaining seats.'''    

available_seats=10
total_seats=0
while True:
    print("available seats: ",available_seats)
    seat=int(input("enter the how many seats you want: "))
    if seat>0:
        if seat > available_seats:
            print(" Not enough seats available") 
        else:
            available_seats = available_seats - seat
            total_seats=total_seats+seat
        repeat=input("do you want to book seat again(yes/no): ")
        if repeat=='yes':
            continue
        else:
            break
    else:
        print("Invalid seat count! Please enter a number greater than zero")
print("available seats: ",available_seats)
print("seats booked: ",total_seats)