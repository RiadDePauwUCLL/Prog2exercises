def movie_count(movies, director):
    return len([m.director for m in movies if director == m.director])


def longest_movie_runtime_with_actor(movies, actor):
    return max([m.runtime for m in movies if actor in m.actors])


def has_director_made_genre(movies, director, genre):
    return any([m.genres for m in movies if director in m.director if genre in m.genres])


def is_prime(n):
    return any([prime for prime in range(2, n) if n <= 1 if n % prime == 0])


def is_increasing(ns):
    return any([x for x in range(len(ns)) for x in range(len(ns) + 1)])