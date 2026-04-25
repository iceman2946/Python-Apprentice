from tkinter import simpledialog, messagebox, Tk
from xmlrpc.client import boolean
from guizero import App, Button
"""Hotel Management"""
class Hotel:
    def __init__(self, rooms, nights):
        self.rooms = rooms
        self.nights = nights
        self.inHotel = False
    def check_in(self):
        if self.rooms > 0:
            self.rooms -= 1
            self.inHotel = True
            return "Checked in successfully!"
        else:
            return "Sorry, no rooms available."

    def check_out(self):
        self.rooms += 1
        return "Checked out successfully!"
        self.inHotel = False;
    def charge(self,nights):
        return nights * 100
    

while True:
    rooms = input("How many rooms do you want to book in the hotel?")
    nights = input("How many nights do you want to stay in the hotel?")
    if Hotel.inHotel == False:
        rooms = input("How many rooms do you want to book in the hotel?")
        nights = input("How many nights do you want to stay in the hotel?")
        hotel = Hotel(int(rooms), int(nights))
        hotel.check_in()
    elif Hotel.inHotel == True:
        action = input("Do you want to check out? (yes/no)")
        if action == "yes":
            print(hotel.check_out())
            print(f"Total charge: ${hotel.charge(int(nights))}")
            break 
        else:
            print()
