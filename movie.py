# # 4. Movie Ticket Booking System
# # Check showtimes, book tickets, select seats, and print confirmation.
# def book_ticket():
#     movie=input("enter movie name:")
#     showtime=input("enter showtime:")
#     seats=input("enter seats:")
#     print("ticket booked")

# def select_seats():
#     seats=input("enter seats:")
#     print("seats selected")

# def print_confirmation():
#     print("ticket confirmation")

# while True:
#     print("\n1.Book Ticket 2.Select Seats 3.Print Confirmation 4.Exit")
#     choice=int(input("enter choice:"))
#     if choice==1:
#         book_ticket()
#     elif choice==2:
#         select_seats()
#     elif choice==3:
#         print_confirmation()
#     else:
#         break

seats = 10
price = 120

while True:
    print("\nAvailable seats:", seats)
    choice = int(input("Enter number of tickets (0 to exit): "))

    if choice == 0:
        break

    if choice <= seats:
        total = choice * price
        seats -= choice
        print("Tickets booked")
        print("Total price:", total)
    else:
        print("Not enough seats")


