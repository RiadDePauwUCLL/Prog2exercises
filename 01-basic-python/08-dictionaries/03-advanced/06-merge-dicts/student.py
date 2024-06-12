def merge_dicts(dict1, dict2):
    new = dict1.copy()
    new.update(dict2)
    return new

# Comprehensions
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}