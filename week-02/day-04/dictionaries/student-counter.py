
students = [
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

print(candy_find(students))
# create a function that takes a list of students and prints:
# - how many candies are owned by students
def who_have_candies(s):
    age = 0
    for student in s:
        if student['candies'] >= 5:
            age += student['age']
    return age

print(who_have_candies(students))

def most_candies(nums):
    num_big = students[0]['candies']
    for num in nums:
        if num['candies'] > num_big:
            num_big = num['candies']
    return num_big

print(most_candies(students))

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies
