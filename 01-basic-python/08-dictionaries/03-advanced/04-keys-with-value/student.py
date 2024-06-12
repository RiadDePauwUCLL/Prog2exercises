# Write your code here
def keys_with_value(dictionary, value):
    new = []
    for k, v in dictionary.items():
        if v == value:
            new.append(k)
    return new

# With comprehensions
def keys_with_value(dictionary, value):
    return [k for k, v in dictionary.items() if v == value]