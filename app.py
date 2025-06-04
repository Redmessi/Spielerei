import csv
import random

# Name of the CSV file that contains the Elo ratings. The file should have a
# header with at least the columns "Team" and "Rating".
ELO_CSV = "elo.csv"


def load_elo_ratings(path: str = ELO_CSV) -> dict:
    """Load team Elo ratings from a CSV file."""
    ratings = {}
    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            team = row.get("Team")
            rating = row.get("Rating")
            if not team or not rating:
                continue
            try:
                ratings[team] = float(rating)
            except ValueError:
                # Skip rows with invalid numeric values
                continue
    return ratings


def win_probability(home: float, away: float) -> float:
    diff = home - away
    return 1 / (1 + 10 ** (-diff / 400))


def simulate_game(home: str, away: str, ratings: dict, runs: int = 10000) -> float:
    prob_home = win_probability(ratings[home], ratings[away])
    wins = sum(random.random() < prob_home for _ in range(runs))
    return wins / runs


def main():
    try:
        ratings = load_elo_ratings()
    except FileNotFoundError:
        print(f"Could not find '{ELO_CSV}'. Please place the file in this directory.")
        return
    except Exception as e:
        print("Failed to load Elo ratings:", e)
        return

    if not ratings:
        print("No ratings retrieved.")
        return

    teams = sorted(ratings)
    print(f"Loaded {len(teams)} teams.")

    def choose_team(prompt: str) -> str:
        while True:
            name = input(prompt).strip()
            if name in ratings:
                return name
            # Suggest up to five matches containing the typed substring.
            suggestions = [t for t in teams if name.lower() in t.lower()]
            if suggestions:
                print("Did you mean:")
                for s in suggestions[:5]:
                    print("  ", s)
            else:
                print("Team not found. Please try again.")

    home = choose_team("Home team: ")
    away = choose_team("Away team: ")

    prob = simulate_game(home, away, ratings)
    print(f"{home} wins {prob:.2%} of the time against {away} based on Elo ratings.")


if __name__ == "__main__":
    main()
