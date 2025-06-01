# ilyasYildirim_2305041006_BasicProgramming2_FinalAssignment
Here is an English summary text that you can use in your project report or presentation. It is based on the instructions you provided and the contents of your three Python files (tsubasaMain.py, players.py, and saveSystem.py):

Project Summary: Captain Tsubasa Football Match Simulation
Course: Basic Programming 2
Topic: Simulation of an Event from a Film or Game
Selected Scenario: A football match simulation inspired by the Captain Tsubasa anime series, implemented entirely through backend logic and command-line interaction.

Overview
This Python-based simulation models a dramatic football match between fictional team Nankatsu and real-life team Ankaragücü. The simulation is turn-based and entirely interactive via the terminal. It emphasizes decision-making, randomness, and the strategic use of player skills, energy, and supporter morale to impact match outcomes.

Modules and Functional Overview
1. tsubasaMain.py — Match Controller
Orchestrates the full match flow: kickoff, random possession events, player actions, enemy attacks, and match outcome.

Simulates crowd cheering, stamina impact, and special abilities like "Twin Shot."

Saves goals during the match using the SaveSystem.

Utilizes FootballPlayer and Goalkeeper classes for team and enemy behaviors.

2. players.py — Player Logic
Implements two main classes:

FootballPlayer: Models each outfield player's name, position, skill set, and stamina.

Goalkeeper: Inherits from FootballPlayer with unique save mechanics and skill-specific success chances.

Includes error handling for unknown or invalid skills.

Implements stamina reduction and random success logic using random and time.

3. saveSystem.py — Data Persistence
Manages match saving via local JSON files.

Automatically assigns match IDs and stores timestamped match data, including goal events.

Provides functions to:

Save new matches.

Append goals to ongoing matches.

Display all saved matches and goal logs.

Export a summary of all matches played (summary.json).

Topics and Concepts Used
✅ Object-Oriented Programming (OOP):

Class definitions (FootballPlayer, Goalkeeper, FootballMatch).

Inheritance and method overriding in Goalkeeper.

✅ Functional Programming:

Use of lambda-style logic and randomness to simulate outcomes dynamically.

✅ Error Handling:

Graceful responses to invalid inputs during gameplay and skill selection.

✅ File I/O and Persistence:

JSON files for storing match data and summaries.

Dynamic directory creation and management of multiple match records.

✅ Modules and Package Management:

Code is separated into logical files (players, save system, match logic).

Proper use of import statements and custom module usage.

✅ Standard Libraries:

random for probabilistic logic.

time for simulation pacing.

datetime for timestamps in save files.

os and json for file operations.
