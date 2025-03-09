# Discrete-Event-Parking

# Parking Lot Simulation

## Overview
This project is a **Parking Lot Simulation** using **Discrete Event Simulation (DES)** to model vehicle arrivals, parking, and departures. The goal is to analyze parking lot efficiency, occupancy rates, and wait times using Python.

## Implementation Goals
- Model a parking lot system with **capacity constraints** and **vehicle queues**.
- Simulate **random vehicle arrivals and departures** over a set duration.
- Track **key metrics** such as occupancy rates and waiting times.
- Implement **a UML-based design** for modularity and scalability.
- Provide **future extensibility** for smart parking or dynamic pricing.

## Project Structure
```
📂 parking-lot-simulation
├── 📄 README.md           # Project documentation
├── 📄 simulation.py       # Main simulation logic
├── 📄 parking_lot.py      # ParkingLot class implementation
├── 📄 vehicle.py          # Vehicle class implementation
├── 📄 uml_diagram.png     # UML Diagram
├── 📄 design_doc.pdf      # Design Documentation
└── 📄 requirements.txt    # Dependencies (if needed)
```

## UML Diagram
The simulation follows a **structured UML model**:
- **Simulation** (⚫ Composition with ParkingLot, - - - > Dependency on Vehicle)
- **ParkingLot** (◇ Aggregation with Vehicle)
- **Vehicle** (Independent entity managed by Simulation & ParkingLot)

## Installation & Running the Simulation
### Prerequisites
- Python 3.x
- Required libraries (if any): `queue`, `random`, `matplotlib`

### Running the Simulation
```bash
python simulation.py
```

## Planned Extensions
- **Data visualization**: Graphs showing occupancy trends.
- **Dynamic parking policies**: Priority parking, reserved spots.
- **Smart parking integration**: Real-time tracking of available spaces.

## Documentation Updates
This repository includes:
- **Literature Review**: Research on parking simulations.
- **UML Diagram**: Visual representation of system structure.
- **Design Document**: Detailed breakdown of system components.

---
Contributions and suggestions are welcome! 🚀
