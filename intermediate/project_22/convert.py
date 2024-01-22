def pluralize(total, singular, plural=None):
    assert isinstance(total, int) and total >=0
    if not plural:
        plural = singular + "s"
    string = singular if total <= 1 else plural

    return f"{total} {string}"


def basket_stat(name, wins, losses):
    wins = int(wins)
    losses = int(losses)
    return f"{name}, {pluralize(wins, 'victoire')}, {pluralize(losses, 'defaite')}"


print(basket_stat("Team Marseille", 1, 8))