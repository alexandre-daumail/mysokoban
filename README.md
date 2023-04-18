# Sokoban Puzzle Game

***
Sokoban is a puzzle game in which the objective is to 
move crates through a warehouse to a defined location within the warehouse.

Crates can be pushed but not pulled, so the player must carefully anticipate 
their movements to avoid getting a crate stuck against a wall or in a corner.

A crate can be placed on any available spot within the warehouse,
and a placed crate can still be moved again if the player pushes it elsewhere.

The game ends when all crates are placed in their designated locations.
***

## Getting Started

### Prerequisites

* Python 3.x installed

### Installing

* Clone the repository

```bash
git clone https://github.com/alexandre-daumail/mysokoban.git
```

* Change into the project directory
```bash
cd src
```
* Install dependencies
```bash
pip install -r requirements.txt
```

## Running the game

To start the game, run the following command in the project directory :

```bash
python .\sokoban.py
```

### How to play

* Use the arrow keys to move the player character
* Push the crates to their designated locations
* The game ends when all crates are placed in their designated locations