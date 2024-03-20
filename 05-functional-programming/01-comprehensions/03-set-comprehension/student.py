def directors(movies):
    return {m.director for m in movies}


def common_elements(xs, ys):
    return {a for a in range(len(xs) - 1) and range(len(ys) - 1)}