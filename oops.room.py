class RoomManager:
    def __init__(self):
        self.rooms = {
            "101": None,
            "102": None,
            "103": None,
            "104": None
        }

    def allocate_room(self):
        name = input("Enter the student's name: ")

        for room, occupant in self.rooms.items():
            if occupant is None:
                self.rooms[room] = name
                print(f"Room {room} allocated to {name}.")
                return

        print("Sorry! No rooms available.")

    def vacate_room(self):
        room = input("Enter the room number to vacate: ")

        if room in self.rooms:
            if self.rooms[room] is not None:
                print(f"Room {room} vacated successfully.")
                self.rooms[room] = None
            else:
                print(f"Room {room} is already vacant.")
        else:
            print("Invalid room number.")

    def show_room_info(self):
        print("\nRoom Status:")
        for room, occupant in self.rooms.items():
            if occupant:
                print(f"Room {room} : Occupied by {occupant}")
            else:
                print(f"Room {room} : Vacant")


def main():
    manager = RoomManager()

    while True:
        print("\n===== Room Management System =====")
        print("1. Allocate Room")
        print("2. Vacate Room")
        print("3. Show Room Information")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.allocate_room()
        elif choice == "2":
            manager.vacate_room()
        elif choice == "3":
            manager.show_room_info()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()