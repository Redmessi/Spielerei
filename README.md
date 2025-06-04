# Football Simulation Webapp

This project aims to build a simple web application that simulates football matches between national teams using an ELO rating system.
All initial team ratings are loaded from the included `ELO.csv` file, so the
application works completely offline.

## Features
- Manage national teams with initial ELO ratings
- Simulate matches and update team ratings
- Expose a basic API using Flask
- Web form to run Monte Carlo match simulations

## Setup
1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```bash
   flask run --app app
   ```

## Running the App
With the server running you can visit `http://127.0.0.1:5000/` to choose two teams and run a Monte Carlo simulation. The result shows the win percentage for each side along with their flags.

You can also access these endpoints programmatically:

- `GET /teams` returns all loaded teams with their current ELO rating.
- `POST /simulate` records an actual match result. Provide `team_a`, `team_b`
  and `result` (1 for win by `team_a`, 0.5 for draw, 0 for loss).

For example, the following command would register a victory for Germany and
return the updated ratings:

```bash
curl -X POST http://127.0.0.1:5000/simulate \
  -H "Content-Type: application/json" \
  -d '{"team_a": "Germany", "team_b": "Brazil", "result": 1}'
```

## Future Improvements
- Persist team data in a database
- Improve match simulation realism

