# Jiu Jitsu Coach CLI

A command-line Python app that simulates a personalized jiu jitsu coach. Users can choose the type of training they want (e.g., offense, defense (not currently built), takedowns, etc.), and the program randomly selects drills based on their input and speaks them aloud using text-to-speech. This is currently a tool that I built for my own personal jiu jitsu game that I have been developing. It does not encompass every possible move or attack. The overall of it includes a general 'Specialized' mode that is more tailored towards learning the moves and drilling their sequences. The 'BLITZ' mode is a mode that is intended to be used after many moves have already been learned from the 'Specialized' mode. This mode is slightly faster in its move calls and is less descriptive in the move sequences. In an attempt to simulate an actual supportive coach, there are random encouragement/supportive callouts spoken during the 'BLITZ' mode. 

---

## Features

- Text-based menu for choosing training focus
- Deep drill selection using nested decision structure
- Randomized drill output for variety
- Text-to-speech announcements for hands-free training
- BLITZ mode to drill a larger array of moves with shorter time intervals and simpler move descriptions

---

## Technologies Used

- Python 3
- `random` module
- `time` module
- Text-to-Speech: `pyttsx3`
- Command Line Interface (CLI)

---

## Getting Started

### Prerequisites

- Python 3.x installed
- Required Python packages (install with pip)

```bash
pip install pyttsx3
```

---

## Running the App

```bash
python coach.py
```

Follow the prompts in the terminal to choose your training path. The app will speak the drills using TTS. In Specialized mode, it will end after 8 drills are completed. In BLITZ mode, it will loop forever unless manually stopped using 'ctrl+c'.

---

## Project Structure

```bash
jiu-jitsu-coach-cli/
├── README.md
├── built_drill_tree.py
├── coach.py
└── drill_tree.py
```

---

## Future Improvements

- Replace nested dictionaries with a tree-based structure or load training structure from a JSON file✅ (Complete)
- Build a web version using Flask or React
- Add defense mode

---

## Why I Built This

I'm combining my interest in programming with my background in jiu jitsu. I find it hard to have a structured training regimen unless you are present in a jiu jitsu class. So, if you're like me and are busy with work and overall life, it can be very challenging to make most classes. This project came about as a means of 'simulating' a personal jiu jitsu coach that will call out moves to you while you are practicing at home. It is intened to be used with a training partner or a grappling dummy to drill the moves being spoken. Ultimately, this is to serve as a training tool that can be used anywhere, anytime, to continue training when away from a structured class/gym. 

---

## License

This project is open source and free to use.

---

## Feedback or Ideas?

Feel free to open an issue or reach out with suggestions!
