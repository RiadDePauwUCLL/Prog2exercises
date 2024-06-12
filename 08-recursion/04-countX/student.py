def countX(text):
    if not text:
        return 0
    
    find_x = 1 if text[0] == 'x' else 0

    return find_x + countX(text[1:])
    
print(countX("caaxrxx"))
print(countX("caa"))