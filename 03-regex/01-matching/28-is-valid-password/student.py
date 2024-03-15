# Write your code here
import re

def is_valid_password(string):

    if re.search(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).{12,}", string):
        if re.search(r"(?!.*?(.)\1\1\1)", string):
            return True
    else:
        return False