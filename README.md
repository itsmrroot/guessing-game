# 🎯 Guessing Game

[![CI](https://github.com/itsmrroot/guessing-game/actions/workflows/ci.yml/badge.svg)](https://github.com/itsmrroot/guessing-game/actions/workflows/ci.yml)

A simple number-guessing game built in Python. The computer picks a random number, and you guess until you get it right.

## How it works

Run the game, and it'll think of a number between 1 and 100. Enter a guess, and it'll tell you if you're too high, too low, or correct.

## Download

No Python installation needed — grab a prebuilt executable from the [latest release](../../releases/latest):

- **macOS**: `guessing-game-macos`
- **Linux**: `guessing-game-linux`
- **Windows**: `guessing-game-windows.exe`

Run it from a terminal (double-clicking may close the window instantly, since this is a console app):
```bash
./guessing-game-macos
```

## Running from source

### Requirements
- Python 3.10+

### Setup

```bash
git clone https://github.com/itsmrroot/guessing-game.git
cd guessing-game
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run the game

```bash
python main.py
```

### Run tests

```bash
pytest
```

## Project Structure

```
guessing-game/
├── guessing_game/
│   ├── __init__.py
│   └── game.py          # check_guess() — pure logic, and play_game() — the console loop
├── tests/
│   ├── __init__.py
│   └── test_game.py
├── main.py               # Entry point
└── requirements.txt
```

## Building executables yourself

Prebuilt binaries are published automatically for every tagged release (see `.github/workflows/release.yml`). To build one locally instead:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

The output will be in `dist/`.

## License

MIT — see [LICENSE](LICENSE).
