# 🎯 Guessing Game

A simple number-guessing game built in Python. The computer picks a random number, and you guess until you get it right.

## How it works

Run the game, and it'll think of a number between 1 and 100. Enter a guess, and it'll tell you if you're too high, too low, or correct.

## Requirements

- Python 3.10+

## Setup

```bash
git clone https://github.com/itsmrroot/guessing-game.git
cd guessing-game
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the game

```bash
python main.py
```

## Running tests

```bash
pytest
```

## Project Structure
```
guessing-game/
├── guessing_game/
│ ├── init.py
│ └── game.py # check_guess() — pure logic, and play_game() — the console loop
├── tests/
│ ├── init.py
│ └── test_game.py
├── main.py # Entry point
└── requirements.txt
```
## License

MIT — see [LICENSE](LICENSE).
