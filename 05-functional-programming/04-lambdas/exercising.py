# Lambda's are essentially functions but smaller, making them more compact.
# If you recall list comprehensions for example, it's the same principle.

def subtract(x, y):
    return x-y
print(subtract(5,2))

print(f"The lambda way:{(lambda x,y:x-y)(5,2)}")

multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
ucll = lambda the_amazing_school, studies: the_amazing_school+" & "+studies
age_check = lambda age: True if age >= 18 else False

print(f'multiplication: {multiply(2,3)}')
print(f'adding up: {add(1, 3, 5)}')
print(f'I study at with the bachelor: {ucll("UCLL","BCS")}')
print(f'Age above or equal to 18: {age_check(18)}\n')

def my_map(my_function, my_iterable):
    result = []
    for item in my_iterable:
        new_item = my_function(item)
        result.append(new_item)
    return(result)

nums = [3, 5, 4, 34, 2, 10]

cubed =  my_map(lambda x: x**3, nums)

print('A more advanced way of using lambda: ', cubed)

# This is a clear example of what lambda EXACTLY does.
# You basically call the function in a smaller expression.