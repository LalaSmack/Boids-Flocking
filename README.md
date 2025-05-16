# 🐦 Boids Flocking Simulator

A 2D Boids simulator built with **Python** and **Pygame** that visualizes flocking behavior through simple rules.Featuring real-time **GUI sliders** to adjust flocking parameters and a **predator** that dynamically alters boid behavior.

## Features

- Real-time flocking simulation with colorful boids  
- **Sliders** to adjust:
  - Cohesion strength  
  - Alignment strength  
  - Separation strength  
- Screen boundary handling to keep boids in view  
- Boids react to a **predator** that actively chases them  
- Clean, modular code using `pygame_gui`

## Requirements

Install dependencies using the included `requirements.txt`:

```bash
pip install -r requirements.txt

```

## Getting Started

1. Clone or download the repository.
2. Navigate to the project folder.
3. Run the simulator:

```bash
python main.py
```
## 🧠 Behavior Logic

### Boids

Each boid follows four main rules:

- **Cohesion**: Steer toward the average position of nearby boids  
- **Alignment**: Match the direction of nearby boids  
- **Separation**: Keep a safe distance from other boids to avoid collisions  
- **Avoidance**: Steer away from the predator when it's within a certain range

The strength of the first three rules can be adjusted in real time using GUI sliders.

### Predator

The predator continuously moves toward the flock’s center and causes nearby boids to flee, simulating a natural threat that disrupts flock movement.

---

## GUI

A simple control panel is integrated using `pygame_gui`:

- **Cohesion Slider** – Adjusts how strongly boids are pulled toward their neighbors  
- **Alignment Slider** – Adjusts how much boids align their direction with the group  
- **Separation Slider** – Adjusts how much boids avoid getting too close to each other

All sliders are interactive and take effect immediately, allowing you to experiment with flocking behavior without restarting the simulation.

## Resources 
https://vergenet.net/~conrad/boids/pseudocode.html




