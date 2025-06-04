"""Simple ELO rating update function."""

K = 40  # constant factor


def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))


def update_elo(rating_a, rating_b, result_a):
    """Update ELO ratings for two teams.

    :param rating_a: current rating of team A
    :param rating_b: current rating of team B
    :param result_a: match outcome from A's perspective (1 win, 0.5 draw, 0 loss)
    :return: tuple of new ratings (new_rating_a, new_rating_b)
    """
    exp_a = expected_score(rating_a, rating_b)
    exp_b = expected_score(rating_b, rating_a)
    new_a = rating_a + K * (result_a - exp_a)
    new_b = rating_b + K * ((1 - result_a) - exp_b)
    return round(new_a, 2), round(new_b, 2)

