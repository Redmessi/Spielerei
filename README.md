# Spielerei

This is a small Python app that loads international football Elo ratings from an
`elo.csv` file and runs a Monte Carlo simulation to estimate match outcomes.

## Setup

The script uses only the Python standard library, so no extra packages are
required.

## Running

Run the app from the repository root and follow the prompts:

```bash
python3 app.py
```

Make sure that an `elo.csv` file containing the Elo data (with at least the
columns `Team` and `Rating`) is present in the project directory. A small
sample file is included. The program loads all teams, then interactively asks
for the home and away team. If you enter an unknown team name, the program will
suggest matches so you can pick the correct one.
