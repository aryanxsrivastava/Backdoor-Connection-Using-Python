class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price=price

class FlightDatabase:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_flights_by_city(self, city, search_type):
        result = []
        if search_type == 1:  
            result = [flight for flight in self.flights if flight.source == city or flight.destination == city]
        elif search_type == 2:  
            result = [flight for flight in self.flights if flight.source == city]
        return result

    def get_flights_between_cities(self, source, destination):
        result = [flight for flight in self.flights if flight.source == source and flight.destination == destination]
        return result

def main():
    database = FlightDatabase()
    database.add_flight(Flight("AI161E90" , "BLR", "BOM", 5600))
    database.add_flight(Flight("BR161F91" , "BOM", "BBI", 6750))
    database.add_flight(Flight("AI161F99" , "BBI", "BLR", 8210))
    database.add_flight(Flight("VS171E20" , "JLR", "BBI", 5500))
    database.add_flight(Flight("AS171G30" , "HYD", "JLR", 4400))
    database.add_flight(Flight("AI131F49" , "HYD", "BOM", 3499))
    
    

    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter city name: ")
        flights = database.get_flights_by_city(city, 1)
    elif choice == 2:
        city = input("Enter city name: ")
        flights = database.get_flights_by_city(city, 2)
    elif choice == 3:
        source = input("Enter source city: ")
        destination = input("Enter destination city: ")
        flights = database.get_flights_between_cities(source, destination)
    else:
        print("Invalid choice")
        return

    if not flights:
        print("No flights found.")
    else:
        print("Flight ID\tSource\t\tDestination\tPrice")
        for flight in flights:
            print(f"{flight.flight_id}\t\t{flight.source}\t\t{flight.destination}\t\t{flight.price}\t\t")

if __name__ == "__main__":
    main()
