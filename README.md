# Red Car Survival Game

This is a survival-oriented car game developed in Python using PyGame and PyOpenGL. The player controls a red sports car moving along a straight, multi-lane road. Randomly positioned enemy cars continuously approach from the top of the screen. The player must avoid collisions by switching lanes and staying alert.

Unlike traditional racing games, this project does not involve laps, finish lines, or speed challenges. Instead, it tests the player’s focus, timing, and ability to survive under increasing pressure.

## Objective

The goal is to survive and avoid hitting enemy cars until the player's score reaches **300**. If the player collides with an enemy car, the game ends. A dedicated game-over screen appears, allowing the player to restart or quit.

## Gameplay Features

- A four-lane highway with lane-specific car movement
- Randomized enemy car generation (color, position, speed)
- Score-based progression system
- Collision detection and crash logic
- Game over screen with replay functionality
- Background engine sound and crash audio feedback
- Animated scenery including flags, dashed road lines, and tire barriers

## Controls

- **Left Arrow (←)** — Move the red car one lane to the left
- **Right Arrow (→)** — Move the red car one lane to the right

## Installation

Make sure Python 3.7 or later is installed, then install the required dependencies:

```bash
pip install pygame PyOpenGL
