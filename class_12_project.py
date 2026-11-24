# ============================================================================
# HOTEL MANAGEMENT SYSTEM - THE SAPPHIRE RETREAT
# CBSE CLASS 12 PROJECT
# ============================================================================
# This project demonstrates:
# - Text File Handling (Read/Write operations)
# - Data Structures (Lists, Dictionaries)
# - Functions and Modular Programming
# - Exception Handling
# - String Formatting and Manipulation
# ============================================================================

import os
from datetime import datetime

# ==================== GLOBAL FILE NAMES ====================
ROOMS_FILE = "rooms.txt"
BOOKINGS_FILE = "bookings.txt"
RESTAURANT_FILE = "restaurant_menu.txt"
SPORTS_FILE = "sports_menu.txt"
GAMING_FILE = "gaming_menu.txt"
BILLS_FILE = "bills.txt"

# ==================== INITIALIZATION FUNCTIONS ====================

def initialize_rooms():
    """Initialize room data in text file"""
    if not os.path.exists(ROOMS_FILE):
        with open(ROOMS_FILE, "w") as f:
            f.write("RoomNo|Type|Price|Status\n")
            # Normal Rooms
            f.write("101|Normal Single|1200|Available\n")
            f.write("102|Normal Single|1200|Available\n")
            f.write("103|Normal Double|2000|Available\n")
            f.write("104|Normal Double|2000|Available\n")
            f.write("105|Normal Suite|3500|Available\n")
            # Elite Rooms
            f.write("201|Elite Single|2500|Available\n")
            f.write("202|Elite Single|2500|Available\n")
            f.write("203|Elite Double|4000|Available\n")
            f.write("204|Elite Double|4000|Available\n")
            f.write("205|Elite Suite|6500|Available\n")
            # Royal Rooms
            f.write("301|Royal Deluxe|8000|Available\n")
            f.write("302|Royal Deluxe|8000|Available\n")
            f.write("303|Royal Suite|12000|Available\n")
            f.write("304|Royal Presidential|20000|Available\n")

def initialize_restaurant():
    """Initialize restaurant menu in text file"""
    if not os.path.exists(RESTAURANT_FILE):
        with open(RESTAURANT_FILE, "w") as f:
            f.write("Category|ItemNo|ItemName|Price\n")
            # Breakfast
            f.write("Breakfast|1|Idli Sambar|80\n")
            f.write("Breakfast|2|Dosa|100\n")
            f.write("Breakfast|3|Paratha with Curd|120\n")
            f.write("Breakfast|4|Poha|70\n")
            f.write("Breakfast|5|Upma|70\n")
            f.write("Breakfast|6|Bread Omelet|90\n")
            f.write("Breakfast|7|Sandwich|110\n")
            # Lunch/Dinner
            f.write("Lunch|1|Veg Thali|250\n")
            f.write("Lunch|2|Non-Veg Thali|350\n")
            f.write("Lunch|3|Paneer Butter Masala|220\n")
            f.write("Lunch|4|Chicken Curry|300\n")
            f.write("Lunch|5|Fish Fry|320\n")
            f.write("Lunch|6|Biryani (Veg)|200\n")
            f.write("Lunch|7|Biryani (Chicken)|280\n")
            f.write("Lunch|8|Dal Tadka|150\n")
            f.write("Lunch|9|Fried Rice|180\n")
            f.write("Lunch|10|Noodles|180\n")
            # Beverages
            f.write("Beverages|1|Tea|30\n")
            f.write("Beverages|2|Coffee|40\n")
            f.write("Beverages|3|Cold Coffee|80\n")
            f.write("Beverages|4|Fresh Juice|100\n")
            f.write("Beverages|5|Soft Drink|50\n")
            f.write("Beverages|6|Lassi|70\n")
            f.write("Beverages|7|Milkshake|120\n")
            # Desserts
            f.write("Desserts|1|Ice Cream|80\n")
            f.write("Desserts|2|Gulab Jamun|60\n")
            f.write("Desserts|3|Rasgulla|60\n")
            f.write("Desserts|4|Pastry|100\n")
            f.write("Desserts|5|Brownie|120\n")

def initialize_sports():
    """Initialize sports facilities in text file"""
    if not os.path.exists(SPORTS_FILE):
        with open(SPORTS_FILE, "w") as f:
            f.write("ActivityNo|Activity|Price\n")
            f.write("1|Swimming Pool (1 hour)|300\n")
            f.write("2|Badminton Court (1 hour)|200\n")
            f.write("3|Table Tennis (1 hour)|150\n")
            f.write("4|Gym Access (Per Day)|400\n")
            f.write("5|Tennis Court (1 hour)|350\n")
            f.write("6|Squash Court (1 hour)|250\n")
            f.write("7|Yoga Session (1 hour)|300\n")
            f.write("8|Personal Trainer (1 hour)|800\n")

def initialize_gaming():
    """Initialize gaming zone in text file"""
    if not os.path.exists(GAMING_FILE):
        with open(GAMING_FILE, "w") as f:
            f.write("GameNo|Game|Price\n")
            f.write("1|Video Game Zone (1 hour)|250\n")
            f.write("2|Pool Table (1 hour)|200\n")
            f.write("3|Snooker (1 hour)|300\n")
            f.write("4|Air Hockey (1 hour)|150\n")
            f.write("5|Bowling (1 game)|180\n")
            f.write("6|VR Gaming (30 minutes)|400\n")
            f.write("7|PlayStation Zone (1 hour)|300\n")
            f.write("8|Arcade Games (1 hour)|200\n")

def initialize_bookings():
    """Initialize bookings file"""
    if not os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, "w") as f:
            f.write("BookingID|RoomNo|Name|Phone|Email|Address|IDProof|Days|RoomRent|RestaurantCharges|SportsCharges|GamingCharges|CheckInDate\n")

def initialize_bills():
    """Initialize bills file"""
    if not os.path.exists(BILLS_FILE):
        with open(BILLS_FILE, "w") as f:
            f.write("BillNo|BookingID|CustomerName|RoomNo|TotalAmount|Date\n")

def initialize_all():
    """Initialize all files"""
    initialize_rooms()
    initialize_restaurant()
    initialize_sports()
    initialize_gaming()
    initialize_bookings()
    initialize_bills()
    print("✅ System initialized successfully!")

# ==================== ROOM MANAGEMENT FUNCTIONS ====================

def read_rooms():
    """Read room data from text file"""
    rooms = {}
    try:
        with open(ROOMS_FILE, "r") as f:
            lines = f.readlines()[1:]  # Skip header
            for line in lines:
                data = line.strip().split("|")
                rooms[int(data[0])] = {
                    "type": data[1],
                    "price": int(data[2]),
                    "status": data[3]
                }
    except:
        pass
    return rooms

def write_rooms(rooms):
    """Write room data to text file"""
    with open(ROOMS_FILE, "w") as f:
        f.write("RoomNo|Type|Price|Status\n")
        for room_no, details in sorted(rooms.items()):
            f.write(f"{room_no}|{details['type']}|{details['price']}|{details['status']}\n")

def display_available_rooms():
    """Display all available rooms categorized by type"""
    rooms = read_rooms()
    print("\n" + "="*80)
    print("AVAILABLE ROOMS".center(80))
    print("="*80)
    
    normal = [(k, v) for k, v in rooms.items() if v["status"] == "Available" and "Normal" in v["type"]]
    elite = [(k, v) for k, v in rooms.items() if v["status"] == "Available" and "Elite" in v["type"]]
    royal = [(k, v) for k, v in rooms.items() if v["status"] == "Available" and "Royal" in v["type"]]
    
    if normal:
        print("\n--- NORMAL ROOMS ---")
        print(f"{'Room No':<15} {'Type':<30} {'Price/Night':<20}")
        print("-"*80)
        for room_no, details in normal:
            print(f"{room_no:<15} {details['type']:<30} Rs.{details['price']:<15}")
    
    if elite:
        print("\n--- ELITE ROOMS ---")
        print(f"{'Room No':<15} {'Type':<30} {'Price/Night':<20}")
        print("-"*80)
        for room_no, details in elite:
            print(f"{room_no:<15} {details['type']:<30} Rs.{details['price']:<15}")
    
    if royal:
        print("\n--- ROYAL ROOMS ---")
        print(f"{'Room No':<15} {'Type':<30} {'Price/Night':<20}")
        print("-"*80)
        for room_no, details in royal:
            print(f"{room_no:<15} {details['type']:<30} Rs.{details['price']:<15}")
    
    if not normal and not elite and not royal:
        print("No rooms available at the moment.")
    print("="*80)

def display_all_rooms():
    """Display all rooms with their status"""
    rooms = read_rooms()
    print("\n" + "="*90)
    print("ALL ROOMS STATUS".center(90))
    print("="*90)
    print(f"{'Room No':<12} {'Type':<25} {'Price/Night':<15} {'Status':<20}")
    print("-"*90)
    for room_no, details in sorted(rooms.items()):
        print(f"{room_no:<12} {details['type']:<25} Rs.{details['price']:<12} {details['status']:<20}")
    print("="*90)

def book_room():
    """Book a room for a customer"""
    rooms = read_rooms()
    print("\n" + "="*90)
    print("ROOM BOOKING".center(90))
    print("="*90)
    
    display_available_rooms()
    
    try:
        room_no = int(input("\nEnter Room Number to book: "))
        
        if room_no not in rooms:
            print("❌ Invalid Room Number!")
            return
        
        if rooms[room_no]["status"] == "Booked":
            print("❌ Room is already booked!")
            return
        
        print("\n--- Customer Details ---")
        name = input("Enter Customer Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        id_proof = input("Enter ID Proof (Aadhar/PAN/Passport): ")
        days = int(input("Enter number of days: "))
        
        if days <= 0:
            print("❌ Number of days must be positive!")
            return
        
        room_rent = rooms[room_no]["price"] * days
        check_in = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Get booking ID
        booking_id = 1
        try:
            with open(BOOKINGS_FILE, "r") as f:
                booking_id = len(f.readlines())
        except:
            booking_id = 1
        
        # Write booking
        with open(BOOKINGS_FILE, "a") as f:
            f.write(f"{booking_id}|{room_no}|{name}|{phone}|{email}|{address}|{id_proof}|{days}|{room_rent}|0|0|0|{check_in}\n")
        
        # Update room status
        rooms[room_no]["status"] = "Booked"
        write_rooms(rooms)
        
        print("\n" + "="*90)
        print("✅ BOOKING CONFIRMED!".center(90))
        print("="*90)
        print(f"Booking ID: {booking_id}")
        print(f"Customer Name: {name}")
        print(f"Room Number: {room_no}")
        print(f"Room Type: {rooms[room_no]['type']}")
        print(f"Number of Days: {days}")
        print(f"Price per Night: Rs.{rooms[room_no]['price']}")
        print(f"Total Room Rent: Rs.{room_rent}")
        print(f"Check-in: {check_in}")
        print("="*90)
        print(f"\n💡 Remember your Booking ID: {booking_id}")
        print("   You can now use Restaurant, Gaming Zone, and Sports facilities!")
        
    except ValueError:
        print("❌ Invalid input!")
    except Exception as e:
        print(f"❌ Error: {e}")

# ==================== RESTAURANT FUNCTIONS ====================

def display_restaurant_menu():
    """Display restaurant menu"""
    print("\n" + "="*80)
    print("RESTAURANT MENU".center(80))
    print("="*80)
    
    try:
        with open(RESTAURANT_FILE, "r") as f:
            lines = f.readlines()[1:]
            
            current_category = ""
            for line in lines:
                data = line.strip().split("|")
                category = data[0]
                
                if category != current_category:
                    print(f"\n--- {category.upper()} ---")
                    print(f"{'No':<8} {'Item':<45} {'Price':<15}")
                    print("-"*80)
                    current_category = category
                
                print(f"{data[1]:<8} {data[2]:<45} Rs.{data[3]:<12}")
    except:
        print("Error reading menu!")
    
    print("="*80)

def restaurant_billing():
    """Handle restaurant billing"""
    print("\n" + "="*80)
    print("RESTAURANT BILLING".center(80))
    print("="*80)
    
    try:
        booking_id = int(input("\nEnter Booking ID: "))
        
        # Read booking
        booking = None
        bookings = []
        with open(BOOKINGS_FILE, "r") as f:
            header = f.readline()
            lines = f.readlines()
            for line in lines:
                data = line.strip().split("|")
                bookings.append(data)
                if int(data[0]) == booking_id:
                    booking = data
        
        if not booking:
            print("❌ Invalid Booking ID!")
            return
        
        print(f"\nCustomer: {booking[2]}")
        print(f"Room No: {booking[1]}")
        
        display_restaurant_menu()
        
        total = 0
        orders = []
        
        print("\n--- Place Order ---")
        while True:
            cat = input("\nEnter Category (Breakfast/Lunch/Beverages/Desserts) or 'done': ")
            if cat.lower() == 'done':
                break
            
            try:
                item_no = int(input("Enter item number: "))
                qty = int(input("Enter quantity: "))
                
                with open(RESTAURANT_FILE, "r") as f:
                    f.readline()
                    for line in f:
                        data = line.strip().split("|")
                        if data[0].lower() == cat.lower() and int(data[1]) == item_no:
                            cost = int(data[3]) * qty
                            total += cost
                            orders.append(f"{data[2]} x{qty} = Rs.{cost}")
                            print(f"✅ Added: {data[2]} x{qty} = Rs.{cost}")
                            break
            except:
                print("❌ Invalid input!")
        
        if total == 0:
            print("No items ordered.")
            return
        
        print("\n" + "="*80)
        print("RESTAURANT BILL".center(80))
        print("="*80)
        print(f"Booking ID: {booking_id}")
        print(f"Customer: {booking[2]}")
        for order in orders:
            print(order)
        print("-"*80)
        print(f"Total: Rs.{total}")
        print("="*80)
        
        # Update booking
        booking[9] = str(int(booking[9]) + total)
        
        with open(BOOKINGS_FILE, "w") as f:
            f.write("BookingID|RoomNo|Name|Phone|Email|Address|IDProof|Days|RoomRent|RestaurantCharges|SportsCharges|GamingCharges|CheckInDate\n")
            for b in bookings:
                f.write("|".join(b) + "\n")
        
        print("\n✅ Restaurant charges added to your booking!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# ==================== SPORTS FUNCTIONS ====================

def display_sports_menu():
    """Display sports facilities"""
    print("\n" + "="*80)
    print("SPORTS FACILITIES".center(80))
    print("="*80)
    print(f"{'No':<8} {'Activity':<55} {'Price':<15}")
    print("-"*80)
    
    try:
        with open(SPORTS_FILE, "r") as f:
            lines = f.readlines()[1:]
            for line in lines:
                data = line.strip().split("|")
                print(f"{data[0]:<8} {data[1]:<55} Rs.{data[2]:<12}")
    except:
        print("Error reading sports menu!")
    
    print("="*80)

def sports_billing():
    """Handle sports facility billing"""
    print("\n" + "="*80)
    print("SPORTS FACILITY BOOKING".center(80))
    print("="*80)
    
    try:
        booking_id = int(input("\nEnter Booking ID: "))
        
        booking = None
        bookings = []
        with open(BOOKINGS_FILE, "r") as f:
            header = f.readline()
            lines = f.readlines()
            for line in lines:
                data = line.strip().split("|")
                bookings.append(data)
                if int(data[0]) == booking_id:
                    booking = data
        
        if not booking:
            print("❌ Invalid Booking ID!")
            return
        
        print(f"\nCustomer: {booking[2]}")
        print(f"Room No: {booking[1]}")
        
        display_sports_menu()
        
        total = 0
        activities = []
        
        print("\n--- Book Activities ---")
        while True:
            choice = input("\nEnter activity number or 'done': ")
            if choice.lower() == 'done':
                break
            
            try:
                act_no = int(choice)
                hours = int(input("Enter hours/sessions: "))
                
                with open(SPORTS_FILE, "r") as f:
                    f.readline()
                    for line in f:
                        data = line.strip().split("|")
                        if int(data[0]) == act_no:
                            cost = int(data[2]) * hours
                            total += cost
                            activities.append(f"{data[1]} x{hours} = Rs.{cost}")
                            print(f"✅ Booked: {data[1]} x{hours} = Rs.{cost}")
                            break
            except:
                print("❌ Invalid input!")
        
        if total == 0:
            print("No activities booked.")
            return
        
        print("\n" + "="*80)
        print("SPORTS BILL".center(80))
        print("="*80)
        print(f"Booking ID: {booking_id}")
        print(f"Customer: {booking[2]}")
        for activity in activities:
            print(activity)
        print("-"*80)
        print(f"Total: Rs.{total}")
        print("="*80)
        
        booking[10] = str(int(booking[10]) + total)
        
        with open(BOOKINGS_FILE, "w") as f:
            f.write("BookingID|RoomNo|Name|Phone|Email|Address|IDProof|Days|RoomRent|RestaurantCharges|SportsCharges|GamingCharges|CheckInDate\n")
            for b in bookings:
                f.write("|".join(b) + "\n")
        
        print("\n✅ Sports charges added!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# ==================== GAMING FUNCTIONS ====================

def display_gaming_menu():
    """Display gaming zone"""
    print("\n" + "="*80)
    print("GAMING ZONE".center(80))
    print("="*80)
    print(f"{'No':<8} {'Game':<55} {'Price':<15}")
    print("-"*80)
    
    try:
        with open(GAMING_FILE, "r") as f:
            lines = f.readlines()[1:]
            for line in lines:
                data = line.strip().split("|")
                print(f"{data[0]:<8} {data[1]:<55} Rs.{data[2]:<12}")
    except:
        print("Error reading gaming menu!")
    
    print("="*80)

def gaming_billing():
    """Handle gaming zone billing"""
    print("\n" + "="*80)
    print("GAMING ZONE BOOKING".center(80))
    print("="*80)
    
    try:
        booking_id = int(input("\nEnter Booking ID: "))
        
        booking = None
        bookings = []
        with open(BOOKINGS_FILE, "r") as f:
            header = f.readline()
            lines = f.readlines()
            for line in lines:
                data = line.strip().split("|")
                bookings.append(data)
                if int(data[0]) == booking_id:
                    booking = data
        
        if not booking:
            print("❌ Invalid Booking ID!")
            return
        
        print(f"\nCustomer: {booking[2]}")
        print(f"Room No: {booking[1]}")
        
        display_gaming_menu()
        
        total = 0
        games = []
        
        print("\n--- Book Games ---")
        while True:
            choice = input("\nEnter game number or 'done': ")
            if choice.lower() == 'done':
                break
            
            try:
                game_no = int(choice)
                sessions = int(input("Enter hours/games: "))
                
                with open(GAMING_FILE, "r") as f:
                    f.readline()
                    for line in f:
                        data = line.strip().split("|")
                        if int(data[0]) == game_no:
                            cost = int(data[2]) * sessions
                            total += cost
                            games.append(f"{data[1]} x{sessions} = Rs.{cost}")
                            print(f"✅ Booked: {data[1]} x{sessions} = Rs.{cost}")
                            break
            except:
                print("❌ Invalid input!")
        
        if total == 0:
            print("No games booked.")
            return
        
        print("\n" + "="*80)
        print("GAMING BILL".center(80))
        print("="*80)
        print(f"Booking ID: {booking_id}")
        print(f"Customer: {booking[2]}")
        for game in games:
            print(game)
        print("-"*80)
        print(f"Total: Rs.{total}")
        print("="*80)
        
        booking[11] = str(int(booking[11]) + total)
        
        with open(BOOKINGS_FILE, "w") as f:
            f.write("BookingID|RoomNo|Name|Phone|Email|Address|IDProof|Days|RoomRent|RestaurantCharges|SportsCharges|GamingCharges|CheckInDate\n")
            for b in bookings:
                f.write("|".join(b) + "\n")
        
        print("\n✅ Gaming charges added!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# ==================== CHECKOUT & BILLING ====================

def checkout_room():
    """Checkout and generate final bill"""
    print("\n" + "="*90)
    print("CHECKOUT & FINAL BILL".center(90))
    print("="*90)
    
    try:
        booking_id = int(input("\nEnter Booking ID: "))
        
        booking = None
        bookings = []
        with open(BOOKINGS_FILE, "r") as f:
            header = f.readline()
            lines = f.readlines()
            for line in lines:
                data = line.strip().split("|")
                bookings.append(data)
                if int(data[0]) == booking_id:
                    booking = data
        
        if not booking:
            print("❌ Invalid Booking ID!")
            return
        
        room_no = int(booking[1])
        room_rent = int(booking[8])
        restaurant = int(booking[9])
        sports = int(booking[10])
        gaming = int(booking[11])
        
        subtotal = room_rent + restaurant + sports + gaming
        gst = subtotal * 0.12
        service = subtotal * 0.05
        total = subtotal + gst + service
        
        print("\n" + "="*90)
        print("FINAL BILL".center(90))
        print("="*90)
        print(f"Booking ID: {booking_id}")
        print(f"Customer Name: {booking[2]}")
        print(f"Phone: {booking[3]}")
        print(f"Email: {booking[4]}")
        print(f"Room Number: {room_no}")
        print(f"Check-in Date: {booking[12]}")
        print(f"Number of Days: {booking[7]}")
        print("="*90)
        print(f"{'Description':<50} {'Amount':<20}")
        print("-"*90)
        print(f"{'Room Rent':<50} Rs.{room_rent:<17.2f}")
        print(f"{'Restaurant Charges':<50} Rs.{restaurant:<17.2f}")
        print(f"{'Sports Facility Charges':<50} Rs.{sports:<17.2f}")
        print(f"{'Gaming Zone Charges':<50} Rs.{gaming:<17.2f}")
        print("-"*90)
        print(f"{'Subtotal':<50} Rs.{subtotal:<17.2f}")
        print(f"{'GST (12%)':<50} Rs.{gst:<17.2f}")
        print(f"{'Service Charge (5%)':<50} Rs.{service:<17.2f}")
        print("="*90)
        print(f"{'GRAND TOTAL':<50} Rs.{total:<17.2f}")
        print("="*90)
        
        # Save bill
        bill_no = 1
        try:
            with open(BILLS_FILE, "r") as f:
                bill_no = len(f.readlines())
        except:
            pass
        
        with open(BILLS_FILE, "a") as f:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{bill_no}|{booking_id}|{booking[2]}|{room_no}|{total:.2f}|{date}\n")
        
        # Remove booking and free room
        bookings.remove(booking)
        with open(BOOKINGS_FILE, "w") as f:
            f.write("BookingID|RoomNo|Name|Phone|Email|Address|IDProof|Days|RoomRent|RestaurantCharges|SportsCharges|GamingCharges|CheckInDate\n")
            for b in bookings:
                f.write("|".join(b) + "\n")
        
        rooms = read_rooms()
        rooms[room_no]["status"] = "Available"
        write_rooms(rooms)
        
        print("\n✅ Checkout completed! Thank you for staying at The Sapphire Retreat!")
        print("   We hope you enjoyed your stay and look forward to welcoming you again!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# ==================== SEARCH & DISPLAY ====================

def search_booking():
    """Search for a booking by customer name"""
    print("\n" + "="*90)
    print("SEARCH BOOKING".center(90))
    print("="*90)
    
    name = input("\nEnter Customer Name: ")
    
    try:
        found = False
        with open(BOOKINGS_FILE, "r") as f:
            f.readline()
            for line in f:
                data = line.strip().split("|")
                if name.lower() in data[2].lower():
                    print("\n--- Booking Found ---")
                    print(f"Booking ID: {data[0]}")
                    print(f"Name: {data[2]}")
                    print(f"Phone: {data[3]}")
                    print(f"Room No: {data[1]}")
                    print(f"Days: {data[7]}")
                    print(f"Room Rent: Rs.{data[8]}")
                    print(f"Restaurant: Rs.{data[9]}")
                    print(f"Sports: Rs.{data[10]}")
                    print(f"Gaming: Rs.{data[11]}")
                    print("-"*90)
                    found = True
        
        if not found:
            print("❌ No booking found!")
    except:
        print("❌ Error reading bookings!")

def display_all_bookings():
    """Display all current bookings"""
    print("\n" + "="*90)
    print("ALL BOOKINGS".center(90))
    print("="*90)
    
    try:
        with open(BOOKINGS_FILE, "r") as f:
            f.readline()
            lines = f.readlines()
            
            if not lines:
                print("No bookings found.")
                return
            
            for line in lines:
                data = line.strip().split("|")
                print(f"\nBooking ID: {data[0]}")
                print(f"Customer: {data[2]}")
                print(f"Room No: {data[1]}")
                print(f"Phone: {data[3]}")
                print(f"Days: {data[7]}")
                total = int(data[8]) + int(data[9]) + int(data[10]) + int(data[11])
                print(f"Total Charges: Rs.{total}")
                print("-"*90)
    except:
        print("❌ Error reading bookings!")

def view_bills():
    """View all generated bills"""
    print("\n" + "="*90)
    print("ALL BILLS".center(90))
    print("="*90)
    
    try:
        with open(BILLS_FILE, "r") as f:
            f.readline()
            lines = f.readlines()
            
            if not lines:
                print("No bills found.")
                return
            
            print(f"{'Bill No':<10} {'Booking ID':<12} {'Customer':<25} {'Room':<10} {'Amount':<15} {'Date':<20}")
            print("-"*90)
            
            for line in lines:
                data = line.strip().split("|")
                print(f"{data[0]:<10} {data[1]:<12} {data[2]:<25} {data[3]:<10} Rs.{data[4]:<12} {data[5]:<20}")
    except:
        print("❌ Error reading bills!")
    
    print("="*90)

# ==================== MAIN MENU ====================

def main_menu():
    """Display main menu"""
    print("\n" + "="*90)
    print("THE SAPPHIRE RETREAT - HOTEL MANAGEMENT SYSTEM".center(90))
    print("="*90)
    print("1.  Display Available Rooms")
    print("2.  Display All Rooms")
    print("3.  Book a Room")
    print("4.  Restaurant Service")
    print("5.  Sports Facility")
    print("6.  Gaming Zone")
    print("7.  Checkout & Generate Bill")
    print("8.  Search Booking")
    print("9.  View All Bills")
    print("10. Exit")
    print("="*90)

def main():
    """Main function"""
    initialize_all()
    
    while True:
        main_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-10): "))
            
            if choice == 1:
                display_available_rooms()
            elif choice == 2:
                display_all_rooms()
            elif choice == 3:
                book_room()
            elif choice == 4:
                restaurant_billing()
            elif choice == 5:
                sports_billing()
            elif choice == 6:
                gaming_billing()
            elif choice == 7:
                checkout_room()
            elif choice == 8:
                search_booking()
            elif choice == 9:
                view_bills()
            elif choice == 10:
                print("\n" + "="*90)
                print("Thank you for choosing The Sapphire Retreat!".center(90))
                print("We hope to see you again soon!".center(90))
                print("="*90)
                break
            else:
                print("❌ Invalid choice! Please enter 1-10.")
            
            input("\nPress Enter to continue...")
            
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nThank you for choosing The Sapphire Retreat!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# Run the program
if __name__ == "__main__":
    main()
