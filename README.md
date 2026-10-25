Nuclear Escape: Fruit Survival

A text-based adventure game developed in Python where players navigate a nuclear facility, collect supplies, and attempt to escape a radioactive monster.

The objective is to explore the facility, collect all six pieces of fruit, and reach the monster's location with enough energy to survive.

Features:

- Room Navigation: Explore eight interconnected rooms using directional commands.
- Inventory Management: Collect and track items throughout the facility.
- Interactive Gameplay: Enter text commands to move between rooms and retrieve objects.
- Input Validation: Receive feedback when entering an invalid command or attempting an unavailable action.
- Win/Loss Conditions: Successfully escape by collecting all six fruits before confronting the monster, or lose by entering its room too early.

Technologies Used:

- Python 3
- Python Dictionaries
- Lists and Inventory Management
- Conditional Statements
- Loops and Functions
- User Input Handling

How to Run:

1. Download or clone this repository.
2. Make sure Python 3 is installed.
3. Open a terminal in the project directory.
4. Run the following command:

   python TextBasedGame.py

5. Follow the instructions displayed in the terminal.

No additional Python libraries are required.

How to Play:

The player begins in the START room and must navigate the facility to locate six fruits.

Movement Commands:
- go North
- go South
- go East
- go West

Item Collection:
- get BANANA
- get APPLE
- get CHERRY

The available directions and items depend on the current room.


Example Gameplay:

You are in the START room
Inventory: []

Enter your move: go West

You are in the LAB room
Inventory: []
You see a BANANA

Enter your move: get BANANA
BANANA retrieved!

Winning: Collect all six fruits before entering the HAZARD room.

Losing: Enter the HAZARD room without collecting all six fruits.

Programming Concepts Demonstrated

This project demonstrates several foundational Python programming concepts:

- Dictionary-Based Data Structures: Rooms, directions, and items are organized using nested dictionaries.
- Control Flow: Conditional statements determine available actions and game outcomes.
- Inventory Tracking: A list stores collected items and updates during gameplay.
- Functions: Separate functions handle game instructions and player status information.
- Loops: A continuous game loop processes player commands until the game ends.
- Input Processing: Player commands are split and evaluated to determine the requested action.

What I Learned:

Developing this project helped me strengthen my understanding of Python fundamentals and how multiple programming concepts work together within an interactive application.

I gained experience organizing game data, managing player input, and creating logical conditions that determine the outcome of a program.

Future Improvements:

Potential improvements include:

- Adding more rooms, items, and obstacles.
- Introducing a health or energy system.
- Implementing difficulty levels.
- Adding randomized events or encounters.
- Creating a graphical interface.

Project Background

Developed as an academic programming project for Southern New Hampshire University (SNHU).

**Author:** Alyssa Osborne
