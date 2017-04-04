
zodiac = [
    {'name': 'Teodor', 'age': 3, 'candies': 2},
    {'name': 'Rezso', 'age': 9.5, 'candies': 2},
    {'name': 'Zsombor', 'age': 12, 'candies': 5},
    {'name': 'Aurel', 'age': 7, 'candies': 3},
    {'name': 'Olaf', 'age': 12, 'candies': 7},
    {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

def candy_find(s):
    candy = 0
    for student in s:
        candy += student['candies']
    return candy

print(candy_find(zodiac))
# create a function that takes a list of students and prints:
# - how many candies are owned by students
def who_have_candies(s):
    age = 0
    for student in s:
        if student['candies'] >= 5:
            age += student['age']
    return age

print(who_have_candies(zodiac))

def most_candies(s):
    num_big = s[0]['candies']
    for student in s:
        if student['candies'] > num_big:
            num_big = student['candies']
    return num_big

print(most_candies(zodiac))

def most_candie_name(s):
    name = s[0]['name']
    num_big = s[0]['candies']
    for student in s:
        if student['candies'] > num_big:
            num_big = student['candies']
            name = student['name']
    return name

print(most_candie_name(zodiac))

def most_candie_name_enhanced(s):
    student_with_most_candies = s[0]
    for student in s:
        if student['candies'] > student_with_most_candies['candies']:
            student_with_most_candies = student
    return student_with_most_candies['name']

print(most_candie_name_enhanced(zodiac))
# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies
