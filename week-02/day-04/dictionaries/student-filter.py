students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

def who_have_most(s):
    for student in s:
        if student['candies'] > 4:
            print(student['name'])

who_have_most(students)

def candy_average(s):
    candy = 0
    for student in s:
        candy += student['candies']
    return candy / len(s)

print(candy_average(students))
# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints:
#  - how many candies they have on average
