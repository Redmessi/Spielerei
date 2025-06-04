from flask import Flask, jsonify, request, render_template, url_for
from elo import update_elo, expected_score
import csv
import random
from pathlib import Path
import pycountry

app = Flask(__name__)


def load_ratings(path: str = "ELO.csv") -> dict:
    """Load initial team ratings from the local ELO.csv file."""
    ratings = {}
    file_path = Path(path)
    if not file_path.exists():
        return ratings
    with file_path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            team = row.get("Team")
            rating = row.get("Rating")
            if team and rating:
                try:
                    ratings[team] = int(float(rating))
                except ValueError:
                    continue
    return ratings


def country_code(name: str) -> str:
    """Return ISO 3166-1 alpha-2 code for a country name."""
    try:
        return pycountry.countries.search_fuzzy(name)[0].alpha_2.lower()
    except Exception:
        return ""


# In-memory team store loaded from ELO.csv
teams = load_ratings()


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        home = request.form.get('home')
        away = request.form.get('away')
        if home and away and home != away:
            prob_home = expected_score(teams.get(home, 0), teams.get(away, 0))
            sims = 10000
            wins = sum(random.random() < prob_home for _ in range(sims))
            pct_home = wins / sims * 100
            result = {
                'home': home,
                'away': away,
                'home_pct': pct_home,
                'away_pct': 100 - pct_home,
                'home_code': country_code(home),
                'away_code': country_code(away)
            }
    return render_template('index.html', teams=sorted(teams.keys()), result=result)

@app.route('/teams', methods=['GET'])
def list_teams():
    return jsonify(teams)

@app.route('/simulate', methods=['POST'])
def simulate_match():
    data = request.get_json(force=True)
    team_a = data.get('team_a')
    team_b = data.get('team_b')
    result = data.get('result')  # 1 if team_a wins, 0.5 draw, 0 if team_a loses
    rating_a = teams.get(team_a)
    rating_b = teams.get(team_b)
    if rating_a is None or rating_b is None:
        return jsonify({'error': 'Unknown team'}), 400
    new_a, new_b = update_elo(rating_a, rating_b, result)
    teams[team_a] = new_a
    teams[team_b] = new_b
    return jsonify({team_a: new_a, team_b: new_b})

if __name__ == '__main__':
    app.run(debug=True)
