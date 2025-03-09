import random

class Vehicle:
    def __init__(self, vehicle_id, arrival_time):
        self.id = vehicle_id
        self.arrival_time = arrival_time
        self.departure_time = arrival_time + random.uniform(1, 5)  # Random stay duration

    def __repr__(self):
        return f"Vehicle({self.id}, Arrives: {self.arrival_time:.2f}, Departs: {self.departure_time:.2f})"
