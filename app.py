from flask import Flask, jsonify, request
from elo import update_elo

app = Flask(__name__)

# In-memory team store: {team_name: rating}
teams = {
    "Germany": 1800,
    "Brazil": 1900,
    "Argentina": 1850
}

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
