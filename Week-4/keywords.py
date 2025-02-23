'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>
def welcome_message(user_name, place):
    if user_name == '':
        if place == '':
            return 'Hello and welcome'
        else:
            return 'Hello and welcome to ' + place
    else:
        if place == '':
            return 'Hello, ' + user_name + ', and welcome'
        else:
            return 'Hello, ' + user_name + ', and welcome to ' + place

# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword argument is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list
def list_average(list, avg_type):
    if avg_type == '' or 'mean':
        return sum(list) / len(list)
    elif avg_type == 'mode':
        return max(set(list), key=list.count)
    elif avg_type == 'median':
        list.sort()
        if len(list) % 2 == 1:
            return list[len(list) // 2]
        else:
            return (list[int(len(list)/2)] + list[int(len(list)/2 - 1)]) / 2