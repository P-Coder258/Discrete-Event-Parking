# Parking Lot Simulation

## Overview
This project is a **parking lot simulation** using **discrete event simulation (DES)** to model vehicle arrivals, parking, and departures. The goal is to analyze parking lot efficiency, occupancy rates, and wait times using Python.

## Implementation Goals
- Model a parking lot system with **capacity constraints** and **vehicle queues**.
- Simulate **random vehicle arrivals and departures** over a set duration.
- Track **key metrics** such as occupancy rates and waiting times.

## Project Structure
```
parking-lot-simulation/
├── README.md                  # Project documentation
├── simulation.py               # Main simulation logic
├── parking_lot.py              # ParkingLot class implementation
├── vehicle.py                  # Vehicle class implementation
├── UML_Diagram.png             # UML Diagram
├── Design_Documentation.pdf    # Design Documentation
├── Literature_Review.pdf       # Literature Review
```

## Operating Instructions

### Installation
1. Install Python 3.x from the official website: https://www.python.org/
2. No external libraries are required beyond the Python standard library.

### Dependencies
- Built-in modules: `random`, `queue`, `math`
- No additional packages are necessary.

### Running the Simulation
1. Clone or download this repository.
2. Open a terminal or command prompt in the project directory.
3. Run the following command:
```bash
python simulation.py
```
4. Adjust parameters like parking lot capacity and arrival rate inside `simulation.py` if needed.

### Specific Requirements
- Compatible with Windows, macOS, or Linux systems.
- Python 3.8+ is recommended.
- No external libraries or frameworks required.

## Notes
- All data output is printed directly to the console.
- Simulation parameters (duration, arrival rate, lot capacity) can be customized inside the `Simulation` class.
- Future improvements include graphical data visualization and advanced logging.

---

Feel free to open an issue or suggest improvements!
