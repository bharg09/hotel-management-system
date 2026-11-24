# The Sapphire Retreat - Hotel Management System

A console-based hotel management system built in Python, using text files for data storage.

Built as my Class 12 Computer Science project.

## Features
- Display available rooms and view all rooms
- Book a room
- Restaurant service
- Sports facility booking
- Gaming zone
- Checkout and bill generation (includes 12% GST and 5% service charge)
- Search bookings
- View all bills

## Main Menu
1. Display Available Rooms
2. Display All Rooms
3. Book a Room
4. Restaurant Service
5. Sports Facility
6. Gaming Zone
7. Checkout & Generate Bill
8. Search Booking
9. View All Bills
10. Exit

## How to Run
1. Install Python 3
2. Download `class_12_project.py`
3. Open a terminal in the folder containing the file
4. Run: `python class_12_project.py`

The program creates its own data files (rooms, bookings, menus, bills) the first time it runs.

## Data Storage
Data is stored in text files using `|` as a separator, for example:
- `rooms.txt`
- `bookings.txt`
- `restaurant_menu.txt`
- `sports_menu.txt`
- `gaming_menu.txt`
- `bills.txt`

## Technologies
- Python 3
- File handling (text files)
- `datetime` module
