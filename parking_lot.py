from queue import Queue

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.occupied_spaces = 0
        self.queue = Queue()
        self.vehicles = []

    def is_full(self):
        return self.occupied_spaces >= self.capacity

    def park_vehicle(self, vehicle):
        if not self.is_full():
            self.vehicles.append(vehicle)
            self.occupied_spaces += 1
            return True  # Successfully parked
        else:
            self.queue.put(vehicle)  # Add to waiting queue
            return False  # Parking lot full

    def remove_vehicle(self, current_time):
        departing_vehicles = [v for v in self.vehicles if v.departure_time <= current_time]
        for vehicle in departing_vehicles:
            self.vehicles.remove(vehicle)
            self.occupied_spaces -= 1

        # If there is space, try parking vehicles from the queue
        while not self.is_full() and not self.queue.empty():
            new_vehicle = self.queue.get()
            self.vehicles.append(new_vehicle)
            self.occupied_spaces += 1
