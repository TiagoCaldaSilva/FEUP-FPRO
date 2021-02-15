def square_odds(values):
    return ",".join([str(int(x) ** 2) for x in values.split(",") if int(x) % 2 == 1])