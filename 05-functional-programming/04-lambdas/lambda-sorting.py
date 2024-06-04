# Now imagine you want to sort out a list with dictionaries with lambda, how would you proceed?
# You can basically sort them out like this as an example, from highest to lowest count.

myList = [{'name':'tim', 'count':2}, {'name':'joe', 'count':5}, {'name':'tom', 'count':3}]

myList.sort(key= lambda x: x['count'], reverse=True)
print(myList)


# Okay great! Now, let's try another one:
# Let's make an age checker for adults and use the lambda & sort the ages by youngest to oldest.

age_checker = lambda age: True if age >= 18 else False

myList = [16, 35, 14, 21, 17]

adults = [age for age in myList if age_checker(age)]
adults.sort(key=lambda x: x)

print(adults)