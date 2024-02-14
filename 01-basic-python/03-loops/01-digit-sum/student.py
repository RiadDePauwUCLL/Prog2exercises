# Write your code here
def last_digit(n):
    return n % 10

def remove_last_digit(n):
    return n // 10

def digit_sum(n):
    sum = last_digit(n)
    for digit in str(remove_last_digit(n)):
        sum += int(digit)
    return sum