class Bus:
    def __init__ (self, route_nubmer, destination):
        self.route_number = route_nubmer
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum Brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty_bus(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        for people in bus_stop.queue:
            self.passengers.append(people)
        #self.passengers = bus_stop.queue
        #self.passenger_count()
        bus_stop.clear()



