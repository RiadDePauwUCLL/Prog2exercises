def genres(movies):
    return {genre for m in movies for genre in m.genres}


def actors(movies):
    return {actor for m in movies for actor in m.actors}