from datetime import date, datetime, timedelta
from typing import List, Optional
import random


class Airline:
    """
    Represents an airline company with its fleet of planes.
    
    Attributes:
        id (str): Two-letter airline code (e.g., 'AA', 'BA')
        name (str): Full name of the airline
        planes (List[Airplane]): List of airplanes belonging to this airline
    """
    
    def __init__(self, id: str, name: str):
        self.id = id.upper()
        self.name = name
        self.planes: List[Airplane] = []
    
    def __repr__(self):
        return f"Airline({self.id} - {self.name}, {len(self.planes)} planes)"


class Airport:
    """
    Represents an airport with scheduled departures and arrivals.
    
    Attributes:
        city (str): City code where the airport is located
        planes (List[Airplane]): Planes currently at this airport
        scheduled_departures (List[Flight]): Future flights departing from here
        scheduled_arrivals (List[Flight]): Future flights arriving here
    """
    
    def __init__(self, city: str):
        self.city = city.upper()
        self.planes: List[Airplane] = []
        self.scheduled_departures: List[Flight] = []
        self.scheduled_arrivals: List[Flight] = []
    
    def schedule_flight(self, destination: 'Airport', flight_date: date, airline: Optional[Airline] = None) -> Optional['Flight']:
        """
        Schedule a new flight from this airport to destination.
        
        Args:
            destination: Target airport
            flight_date: Date of the flight
            airline: Preferred airline (optional)
            
        Returns:
            Flight object if scheduled successfully, None otherwise
        """
        # Find available airplane
        available_plane = None
        
        if airline:
            # Check specific airline first
            available_plane = self._find_available_plane_in_airline(airline, flight_date)
        
        # If no specific airline or no plane found, search all planes at airport
        if not available_plane:
            for plane in self.planes:
                if plane.available_on_date(flight_date, self):
                    available_plane = plane
                    break
        
        if not available_plane:
            print(f"❌ No available planes at {self.city} for {flight_date}")
            return None
        
        # Create and schedule the flight
        flight = Flight(flight_date, destination, self, available_plane)
        
        # Add to airport schedules
        self.scheduled_departures.append(flight)
        self.scheduled_departures.sort(key=lambda f: f.date)
        
        destination.scheduled_arrivals.append(flight)
        destination.scheduled_arrivals.sort(key=lambda f: f.date)
        
        # Add to plane's schedule
        available_plane.next_flights.append(flight)
        available_plane.next_flights.sort(key=lambda f: f.date)
        
        # Update plane location (it will leave)
        if flight_date == date.today():
            available_plane.current_location = None  # In the air
        
        print(f"✅ Scheduled flight {flight.id}: {self.city} -> {destination.city} on {flight_date}")
        return flight
    
    def _find_available_plane_in_airline(self, airline: Airline, flight_date: date) -> Optional['Airplane']:
        """Helper to find available plane from a specific airline."""
        for plane in self.planes:
            if plane.company == airline and plane.available_on_date(flight_date, self):
                return plane
        return None
    
    def info(self, start_date: date, end_date: date):
        """
        Display all scheduled flights within date range.
        
        Args:
            start_date: Start of date range (inclusive)
            end_date: End of date range (inclusive)
        """
        print(f"\n{'='*60}")
        print(f"📍 AIRPORT {self.city} - FLIGHT INFORMATION")
        print(f"   Period: {start_date} to {end_date}")
        print(f"{'='*60}")
        
        # Departures
        print(f"\n🛫 SCHEDULED DEPARTURES:")
        relevant_departures = [
            f for f in self.scheduled_departures 
            if start_date <= f.date <= end_date
        ]
        
        if relevant_departures:
            for flight in relevant_departures:
                status = "🟢" if flight.date >= date.today() else "✅"
                print(f"   {status} {flight.id} -> {flight.destination.city} on {flight.date}")
        else:
            print("   No scheduled departures in this period")
        
        # Arrivals
        print(f"\n🛬 SCHEDULED ARRIVALS:")
        relevant_arrivals = [
            f for f in self.scheduled_arrivals 
            if start_date <= f.date <= end_date
        ]
        
        if relevant_arrivals:
            for flight in relevant_arrivals:
                status = "🟡" if flight.date >= date.today() else "✅"
                print(f"   {status} {flight.id} from {flight.origin.city} on {flight.date}")
        else:
            print("   No scheduled arrivals in this period")
        
        print(f"\n📊 Current planes at airport: {[p.id for p in self.planes]}")
        print(f"{'='*60}\n")
    
    def __repr__(self):
        return f"Airport({self.city})"


class Flight:
    """
    Represents a scheduled flight between two airports.
    
    Attributes:
        date (date): Date of the flight
        destination (Airport): Arrival airport
        origin (Airport): Departure airport
        plane (Airplane): Aircraft assigned to this flight
        id (str): Encoded ID: DESTINATION+AIRLINE_CODE+DATE
    """
    
    def __init__(self, flight_date: date, destination: Airport, origin: Airport, plane: 'Airplane'):
        self.date = flight_date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        
        # Generate ID: DESTINATION + AIRLINE_CODE + DATE (YYYYMMDD)
        date_str = flight_date.strftime('%Y%m%d')
        self.id = f"{destination.city}{plane.company.id}{date_str}"
        
        self._completed = False
    
    def take_off(self):
        """Execute takeoff - remove plane from origin airport."""
        if self.plane in self.origin.planes:
            self.origin.planes.remove(self.plane)
            print(f"🛫 Flight {self.id} taking off from {self.origin.city}")
        self.plane.current_location = None  # In the air
    
    def land(self):
        """Execute landing - add plane to destination airport."""
        self.destination.planes.append(self.plane)
        self.plane.current_location = self.destination
        self._completed = True
        print(f"🛬 Flight {self.id} landed at {self.destination.city}")
        
        # Remove from future schedules
        if self in self.plane.next_flights:
            self.plane.next_flights.remove(self)
    
    def __repr__(self):
        return f"Flight({self.id}: {self.origin.city}->{self.destination.city})"


class Airplane:
    """
    Represents an airplane with scheduling capabilities.
    
    Attributes:
        id (int): Unique identifier
        current_location (Airport): Where the plane currently is
        company (Airline): Owning airline
        next_flights (List[Flight]): Scheduled future flights
    """
    
    _id_counter = 1
    
    def __init__(self, company: Airline, current_location: Airport):
        self.id = Airplane._id_counter
        Airplane._id_counter += 1
        
        self.company = company
        self.current_location = current_location
        self.next_flights: List[Flight] = []
        
        # Register plane with airline and airport
        company.planes.append(self)
        current_location.planes.append(self)
    
    def fly(self, destination: Airport):
        """
        Execute flight to destination if scheduled.
        
        Args:
            destination: Target airport
        """
        today = date.today()
        
        # Find flight scheduled for today to this destination
        flight_to_execute = None
        for flight in self.next_flights:
            if flight.date == today and flight.destination == destination:
                flight_to_execute = flight
                break
        
        if not flight_to_execute:
            print(f"❌ No flight scheduled today from {self.current_location.city} to {destination.city}")
            return False
        
        # Execute the flight
        flight_to_execute.take_off()
        flight_to_execute.land()
        return True
    
    def location_on_date(self, query_date: date) -> Optional[Airport]:
        """
        Determine where the plane will be on a specific date.
        
        Args:
            query_date: Date to check
            
        Returns:
            Airport where plane will be, or None if in flight
        """
        # If before today, we don't track history (assume at current location)
        if query_date < date.today():
            return self.current_location
        
        if query_date == date.today():
            return self.current_location
        
        # Check if there's a flight on that date
        for flight in self.next_flights:
            if flight.date == query_date:
                # Plane will be at destination after flight
                return flight.destination
            
            # If query date is between flights, plane stays at last destination
            if flight.date > query_date:
                break
        
        # Check historical flights that would have completed
        # For future dates beyond last scheduled flight, plane stays at last known location
        return self.current_location
    
    def available_on_date(self, check_date: date, location: Airport) -> bool:
        """
        Check if plane can fly from location on date.
        
        Args:
            check_date: Date to check availability
            location: Required departure location
            
        Returns:
            True if available (at location and no conflict)
        """
        # Must be at the specified location on that date
        if self.location_on_date(check_date) != location:
            return False
        
        # Check if already has a flight on that date
        for flight in self.next_flights:
            if flight.date == check_date:
                return False
        
        return True
    
    def __repr__(self):
        loc = self.current_location.city if self.current_location else "IN_AIR"
        return f"Airplane({self.id}, {self.company.id}, at {loc})"


# ============== TESTING THE SYSTEM ==============

def run_demo():
    """Test the air traffic management system."""
    print("🛫 AIR TRAFFIC MANAGEMENT SYSTEM DEMO")
    print("=" * 60)
    
    # Create airlines
    american = Airline("AA", "American Airlines")
    british = Airline("BA", "British Airways")
    el_al = Airline("LY", "El Al")
    
    print(f"\n✈️  Created airlines: {american.name}, {british.name}, {el_al.name}")
    
    # Create airports
    jfk = Airport("NYC")  # New York
    lhr = Airport("LON")  # London
    tlv = Airport("TLV")  # Tel Aviv
    cdg = Airport("PAR")  # Paris
    
    print(f"🌍 Created airports: JFK ({jfk.city}), LHR ({lhr.city}), TLV ({tlv.city}), CDG ({cdg.city})")
    
    # Create airplanes
    plane1 = Airplane(american, jfk)      # AA plane at NYC
    plane2 = Airplane(british, lhr)       # BA plane at London
    plane3 = Airplane(el_al, tlv)         # LY plane at Tel Aviv
    plane4 = Airplane(american, jfk)      # Another AA plane at NYC
    
    print(f"\n🛩️  Created {Airplane._id_counter - 1} airplanes")
    for p in [plane1, plane2, plane3, plane4]:
        print(f"   • Plane {p.id}: {p.company.name} at {p.current_location.city}")
    
    # Schedule some flights
    today = date.today()
    tomorrow = today + timedelta(days=1)
    day_after = today + timedelta(days=2)
    
    print(f"\n📅 Today is: {today}")
    print("\n" + "=" * 60)
    print("SCHEDULING FLIGHTS")
    print("=" * 60)
    
    # Schedule flights
    flight1 = jfk.schedule_flight(lhr, tomorrow, american)      # NYC -> LON tomorrow
    flight2 = lhr.schedule_flight(tlv, day_after, british)      # LON -> TLV day after
    flight3 = tlv.schedule_flight(jfk, tomorrow, el_al)         # TLV -> NYC tomorrow
    flight4 = jfk.schedule_flight(cdg, day_after)               # NYC -> PAR day after (any airline)
    
    # Test availability checks
    print("\n" + "=" * 60)
    print("TESTING AVAILABILITY SYSTEM")
    print("=" * 60)
    
    # Check plane locations
    print(f"\n📍 Plane {plane1.id} location on {tomorrow}: {plane1.location_on_date(tomorrow)}")
    print(f"📍 Plane {plane2.id} location on {tomorrow}: {plane2.location_on_date(tomorrow)}")
    
    # Check availability
    print(f"\n✅ Plane {plane1.id} available at JFK tomorrow? {plane1.available_on_date(tomorrow, jfk)}")
    print(f"✅ Plane {plane1.id} available at LHR tomorrow? {plane1.available_on_date(tomorrow, lhr)}")
    
    # Try to schedule conflicting flight (should fail)
    print(f"\n🚫 Trying to schedule conflicting flight for plane {plane1.id}...")
    conflict = jfk.schedule_flight(tlv, tomorrow, american)  # Should fail - plane1 busy
    
    # Show airport info
    jfk.info(today, day_after)
    lhr.info(today, day_after)
    tlv.info(today, day_after)
    
    # Simulate flight execution
    print("\n" + "=" * 60)
    print("SIMULATING FLIGHT EXECUTION")
    print("=" * 60)
    
    # Note: In real scenario, we'd advance time. Here we demonstrate logic:
    print(f"\n🎮 Simulating: Today is {tomorrow} (tomorrow)")
    print(f"   Plane {plane1.id} attempting to fly to London...")
    # This won't work because today is still today, not tomorrow
    # But we can demonstrate the fly method logic
    
    print("\n" + "=" * 60)
    print("SYSTEM STATUS SUMMARY")
    print("=" * 60)
    
    for airline in [american, british, el_al]:
        print(f"\n🏢 {airline.name} ({airline.id}):")
        for plane in airline.planes:
            flights = [f.id for f in plane.next_flights]
            print(f"   Plane {plane.id}: at {plane.current_location.city}, flights: {flights if flights else 'None'}")


if __name__ == "__main__":
    run_demo()