"""Hotel Management"""
class Hotel:
    def __init__(self):
        # List of rooms: each room is a dictionary
        self.rooms = [
            {'number': 101, 'type': 'single', 'occupied': False, 'guest': None},
            {'number': 102, 'type': 'single', 'occupied': False, 'guest': None},
            {'number': 103, 'type': 'single', 'occupied': False, 'guest': None},
            {'number': 104, 'type': 'double', 'occupied': False, 'guest': None},
            {'number': 105, 'type': 'double', 'occupied': False, 'guest': None},
            {'number': 106, 'type': 'double', 'occupied': False, 'guest': None},
            {'number': 107, 'type': 'suite', 'occupied': False, 'guest': None},
            {'number': 108, 'type': 'suite', 'occupied': False, 'guest': None},
            # Add more rooms as needed
        ]
        # List of bookings: each booking is a tuple (guest_name, room_numbers, nights)
        self.bookings = []

    def check_available_rooms(self, room_type=None):
        available = [room for room in self.rooms if not room['occupied']]
        if room_type:
            available = [room for room in available if room['type'] == room_type]
        return available

    def check_in(self, guest_name, room_count, nights, room_type=None):
        available_rooms = self.check_available_rooms(room_type)
        if len(available_rooms) < room_count:
            return "Not enough rooms available."
        
        # Assign rooms
        assigned_rooms = available_rooms[:room_count]
        room_numbers = []
        for room in assigned_rooms:
            room['occupied'] = True
            room['guest'] = guest_name
            room_numbers.append(room['number'])
        
        # Add to bookings
        self.bookings.append((guest_name, tuple(room_numbers), nights))
        return f"Checked in {guest_name} to rooms {room_numbers} for {nights} nights."

    def check_out(self, guest_name):
        checked_out_rooms = []
        for room in self.rooms:
            if room['guest'] == guest_name:
                room['occupied'] = False
                room['guest'] = None
                checked_out_rooms.append(room['number'])
        
        if not checked_out_rooms:
            return "No rooms found for that guest."
        
        # Remove from bookings
        self.bookings = [b for b in self.bookings if b[0] != guest_name]
        return f"Checked out rooms {checked_out_rooms}."

    def charge(self, guest_name):
        booking = next((b for b in self.bookings if b[0] == guest_name), None)
        if not booking:
            return 0
        _, room_numbers, nights = booking
        base_rate = 100  # per night per room
        return len(room_numbers) * nights * base_rate

    def list_occupied_rooms(self):
        occupied = [room for room in self.rooms if room['occupied']]
        return occupied

    def list_bookings(self):
        return self.bookings


# Example usage
hotel = Hotel()

while True:
    action = input("What would you like to do? (checkin/checkout/status/quit): ").lower()
    if action == 'checkin':
        guest_name = input("Guest name: ")
        room_count = int(input("Number of rooms: "))
        nights = int(input("Number of nights: "))
        room_type = input("Room type (optional, press enter for any): ").strip() or None
        result = hotel.check_in(guest_name, room_count, nights, room_type)
        print(result)
    elif action == 'checkout':
        guest_name = input("Guest name: ")
        result = hotel.check_out(guest_name)
        charge = hotel.charge(guest_name)  # Charge before removing booking
        print(result)
        if charge > 0:
            print(f"Total charge: ${charge}")
    elif action == 'status':
        occupied = hotel.list_occupied_rooms()
        print("Occupied rooms:")
        for room in occupied:
            print(f"Room {room['number']} ({room['type']}): {room['guest']}")
        print("Bookings:")
        for booking in hotel.list_bookings():
            print(f"{booking[0]}: rooms {list(booking[1])}, {booking[2]} nights")
    elif action == 'quit':
        break
    else:
        print("Invalid action.")
