def points(games):
    total_points = 0

    for game_result in games:
        scores = game_result.split(":")
        x = int(scores[0])
        y = int(scores[1])

        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1

    return total_points
