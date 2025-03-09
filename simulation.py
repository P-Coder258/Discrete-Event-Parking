import random

class Simulation:
    def __init__(self, duration, parking_lot):
        self.duration = duration
        self.parking_lot = parking_lot
        self.vehicles = []
        self.time = 0

    def generate_vehicle(self):
        vehicle_id = len(self.vehicles) + 1
        arrival_time = random.uniform(0, self.duration)  # Random arrival within the simulation duration
        new_vehicle = Vehicle(vehicle_id, arrival_time)
        self.vehicles.append(new_vehicle)
        return new_vehicle

    def run_simulation(self):
        for _ in range(self.duration):  # Simulating each time unit
            self.time += 1
            
            # Generate a vehicle at random intervals
            if random.random() < 0.3:  # 30% chance of a new vehicle arriving
                vehicle = self.generate_vehicle()
                self.parking_lot.park_vehicle(vehicle)

            # Remove vehicles that have completed their parking time
            self.parking_lot.remove_vehicle(self.time)

        self.display_results()

    def display_results(self):
        print(f"Simulation completed in {self.duration} time units.")
        print(f"Total vehicles processed: {len(self.vehicles)}")
        print(f"Vehicles still in queue: {self.parking_lot.queue.qsize()}")
