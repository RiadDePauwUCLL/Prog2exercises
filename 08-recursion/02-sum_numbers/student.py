def sum_numbers(number):
    # We turn the negative number into an ABS
    number = abs(number)

    # checking base-10 number aka more than 1 digit
    if number < 10:
        return number
    
    # Modulo & Division // 10
    return (number % 10) + sum_numbers(number // 10)