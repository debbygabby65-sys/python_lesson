# Mystery Island: The Lost Lighthouse

## About the Project
Mystery Island is a beginner-friendly, text-based adventure game built with Python. The player explores an island, collects useful items, makes decisions, and tries to restore the lost lighthouse beacon.

## Objective
Explore the island, manage your energy, collect the Rope and Lantern, cross the Old Bridge, and reach the Lighthouse to win.

## Features
- Interactive command-line menu.
- Player name input.
- Energy management system.
- Multiple locations to explore.
- Item collection and inventory.
- Decisions with different consequences.
- Input validation.
- Win and lose conditions.
- Replay option.
- Automated unit tests.

## Locations
- **Beach:** Starting point.
- **Jungle:** Search for the Rope or encounter danger.
- **Cave:** Find the Lantern or face falling rocks.
- **Old Bridge:** Use the Rope to cross.
- **Lighthouse:** Use the Rope and Lantern to restore the beacon.

## Requirements
- Python 3
- No external libraries required.

## How to Run

1. Open your terminal.
2. Navigate into the project folder.
3. Run:

   `python3 main.py`

## How to Run Tests

Run:

`python3 -m unittest discover -s tests -v`

## Game Rules
- You start with 5 energy points.
- Some actions reduce your energy.
- Collect the Rope and Lantern.
- You need the Rope to cross the Old Bridge.
- You need both items to restore the lighthouse beacon.
- If your energy reaches zero, the game ends.

## Learning Objectives
This project demonstrates beginner Python concepts, including:
- Variables and data types.
- Functions.
- Conditional statements.
- Loops.
- Lists.
- User input.
- Exception and input handling.
- Unit testing with `unittest`.