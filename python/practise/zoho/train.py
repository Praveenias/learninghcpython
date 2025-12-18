import uuid

class TrainService:
    def __init__(self):
        self.stations = ['A', 'B', 'C', 'D', 'E']
        self.seats = 8  # Total seats
        self.waiting_list_limit = 2
        self.train_seats = {i: [None] * (len(self.stations) - 1) for i in range(self.seats)}  # Seat allocation
        self.waiting_list = []  # Waiting list queue
        self.pnr_records = {}  # Store PNR details
        self.pnrnumber = 0

    def generate_pnr(self):
        """Generate a unique PNR number"""
        self.pnrnumber += 1

    def get_avilabilty_seats(self,source,destinaton):
        source_idx = self.stations.index(source)
        dest_idx = self.stations.index(destinaton)
        seats = 0
        for i,j in self.train_seats.items():
            if all(cell is None for cell in j[source_idx:dest_idx]):
                seats +=1
        return seats



    def book_seats(self, source, destination, num_tickets):
        """Book confirmed seats or add to waiting list if full, returns a single PNR"""
        source_idx = self.stations.index(source)
        dest_idx = self.stations.index(destination)
        available_seats = self.get_avilabilty_seats(source,destination)
        if available_seats < num_tickets and (len(self.waiting_list) > num_tickets):
            print("seat is full")
            return
        
        booked = 0
        self.generate_pnr()
        booked_seats = []
        
        for seat in self.train_seats:
            if booked == num_tickets:
                break
            #print(all(cell is None for cell in self.train_seats[seat][source_idx:dest_idx]))
            if all(cell is None for cell in self.train_seats[seat][source_idx:dest_idx]):
                for i in range(source_idx, dest_idx):
                   # print("hit",pnr)
                    self.train_seats[seat][i] = self.pnrnumber  # Assign PNR to seat
                booked_seats.append(seat)               
                booked += 1
            self.pnr_records[self.pnrnumber] = (booked_seats, source, destination)
            print(f"{num_tickets} tickets booked from {source} to {destination} with PNR: {self.pnrnumber}")
        
        if booked < num_tickets:
            remaining = num_tickets - booked
            if len(self.waiting_list) <= self.waiting_list_limit:
                self.waiting_list.append((self.pnrnumber, source, destination, remaining))
                self.pnr_records[self.pnrnumber] = ('WL', source, destination)
                print(f"{remaining} added to the waiting list with PNR: {self.pnrnumber}")
            else:
                print("No seats available! Waiting list is full.")
                return None
        
        return self.pnrnumber

    def cancel_ticket(self, pnr,nooftickets):
        """Cancel a ticket based on PNR and move waiting list passengers if possible"""
        if pnr not in self.pnr_records:
            print("Invalid PNR! No such booking found.")
            return
        
        seats, source, destination = self.pnr_records.pop(pnr)
        if nooftickets > len(seats):
            print(f"booked is less ticket seat :{len(seats)}")
        # seats = nooftickets
        doforseats = 0
        
        if seats != 'WL':
            source_idx = self.stations.index(source)
            dest_idx = self.stations.index(destination)

            for seat in seats:
                for i in range(source_idx, dest_idx):
                    if nooftickets > 0:
                        self.train_seats[seat][i] = None  # Clear seat
                doforseats +=1
                if doforseats == nooftickets:
                        break
            print(f"Ticket with PNR {pnr} from {source} to {destination} cancelled for {nooftickets} tickets")
            print(self.waiting_list)
            
            # Move a waiting list passenger to the confirmed seat
            # if self.waiting_list:
            #     waiting_pnr, waiting_source, waiting_dest, count = self.waiting_list.pop(0)
            #     self.book_seats(waiting_source, waiting_dest, count)
            #     self.pnr_records.pop(waiting_pnr, None)
        else:
            print(f"PNR {pnr} was in the waiting list and has been removed.")

    def print_chart(self):
        """Print seat chart as a table"""
        print("\nSeat Chart:")
        print("Seat | " + " | ".join(self.stations[:-1]))  # Header row
        print("-" * (6 + len(self.stations) * 4))

        for seat, bookings in self.train_seats.items():
            #print(seat,bookings)
            row_data = " | ".join('*' if cell else " " for cell in bookings)
            print(f" {seat}  | {row_data}")
            print()

        print("\nWaiting List:")
        if not self.waiting_list:
            print("No waiting list entries.")
        else:
            for idx, (pnr, src, dest, count) in enumerate(self.waiting_list, start=1):
                print(f"{idx}. PNR: {pnr}, {count} Ticket(s) from {src} to {dest}")

if __name__ == "__main__":
    ts = TrainService()
    pnr = ts.book_seats(source='A',destination= 'E',num_tickets= 8)
    if pnr:
        print("Your PNR number:", pnr)
    # ts.print_chart()

    source = 'A'
    destination = 'E'
    num_tickets = 2
    pnr = ts.book_seats('A', 'E', 2)
    if pnr:
        print("Your PNR number:", pnr)
    pnr = ts.book_seats('A', 'E', 2)
    if pnr:
        print("Your PNR number:", pnr)
   
    # ts.cancel_ticket(1,5)
    #ts.print_chart()
    # source = 'A'
    # destination = 'B'
    # num_tickets = 2
    # pnr = ts.book_seats(source, destination, num_tickets)
    # if pnr:
    #     print("Your PNR number:", pnr)
    # ts.print_chart()
    # ts.cancel_ticket(2)
    # ts.print_chart()
    # ts.cancel_ticket(2)
    # ts.print_chart()
    
    
    # while True:
    #     print("\n------------------------------Train Ticket Booking -------------")
    #     print("1. Book Ticket")
    #     print("2. Cancel Ticket")
    #     print("3. Show Chart")
    #     print("4. Exit")
    #     choice = int(input("Enter your option: "))

    #     if choice == 1:
    #         source = input("Enter source: ")
    #         destination = input("Enter destination: ")
    #         num_tickets = int(input("Enter number of tickets: "))
    #         pnr = ts.book_seats(source, destination, num_tickets)
    #         if pnr:
    #             print("Your PNR number:", pnr)
    #     elif choice == 2:
    #         pnr = input("Enter PNR to cancel: ")
    #         ts.cancel_ticket(pnr)
    #     elif choice == 3:
    #         ts.print_chart()
    #     elif choice == 4:
    #         print("Exiting system. Have a nice day!")
    #         break
    #     else:
    #         print("Invalid choice! Please try again.")
