import re

def is_valid_name(name):
    if re.match(r"\w+\s\w+.+", name):
        print(name)
    
is_valid_name("monke monke")
is_valid_name("modfdsfds     d")