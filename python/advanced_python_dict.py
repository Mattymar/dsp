import csv
from itertools import islice

faculty_dict = {}
professor_dict = {}

with open('faculty.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header
    for row in reader:
        # Build dict with last names as keys
        faculty_dict[row[0].split()[-1]] = {'degree': row[1], 'title': row[2], 'email': row[3]}
        # Build dict with first, last names as keys
        professor_dict[(' '.join(row[0].split()[:-1]), row[0].split()[-1])] = {'degree': row[1], 'title': row[2], 'email': row[3]}

# This is from itertools recipes
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

# Print 3 key, value pairs
print(take(3, faculty_dict.items()))
print(take(3, professor_dict.items()))

# Print sorted by professor's last name
print(sorted(professor_dict.items(), key=lambda x: x[0][1]))