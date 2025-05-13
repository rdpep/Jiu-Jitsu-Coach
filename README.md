# Jiu Jitsu Coach CLI

A command-line Python app that simulates a personalized jiu jitsu coach. Users can choose the type of training they want (e.g., offense, defense (not currently built), takedowns, etc.), and the program randomly selects drills based on their input and speaks them aloud using text-to-speech.

---

## Features

- Text-based menu for choosing training focus
- Deep drill selection using nested decision structure
- Randomized drill output for variety
- Text-to-speech announcements for hands-free training

---

## Technologies Used

- Python 3
- `random` module
- Text-to-Speech: `pyttsx3` or `gTTS` *(whichever you used)*
- Command Line Interface (CLI)

---

## Getting Started

### Prerequisites

- Python 3.x installed
- Required Python packages (install with pip)

```bash
pip install pyttsx3

---

**## Running the App**

Follow the prompts in the terminal to choose your training path. The app will speak the drills using TTS.

---

**## Project Structure**

jiu-jitsu-coach-cli/
├── README.md
├── blitz_mode.py
├── coach.py
├── dictionary.py
└── selections.py

---

**## Future Improvements**

- Replace nested dictionaries with a tree-based structure
- Load training structure from a JSON file
- Add user profiles to save preferences
- Build a web version using Flask or React
- Add timers and workout intervals
- Include videos or links for each drill

---

**## Why I Built This**

I'm combining my interest in programming with my background in jiu jitsu. This is a portfolio project to learn Python and eventually explore web development.

---

**## License**

This project is open source and free to use.

---

## Feedback or Ideas?

Feel free to open an issue or reach out with suggestions!

