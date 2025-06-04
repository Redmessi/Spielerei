# Football Simulation Webapp

This project aims to build a simple web application that simulates football matches between national teams using an ELO rating system.

## Features
- Manage national teams with initial ELO ratings
- Simulate matches and update team ratings
- Expose a basic API using Flask

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
With the server running you can access these endpoints:

- `GET /teams` lists all teams with their current ELO rating.
- `POST /simulate` simulates a match. Send JSON with `team_a`, `team_b` and
  `result` (1 for win by `team_a`, 0.5 for draw, 0 for loss).

Example request:
```bash
curl -X POST http://127.0.0.1:5000/simulate \
  -H "Content-Type: application/json" \
  -d '{"team_a": "Germany", "team_b": "Brazil", "result": 1}'
```

## Future Improvements
- Add a frontend interface for easier team selection and match simulation
- Persist team data in a database
- Improve match simulation realism

