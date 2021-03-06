import csv
import re


def format_degree(degree):
    """Takes degree and returns one string for a number of possible matches"""
    if bool(re.search(r'^ph.?d.?$', degree, re.IGNORECASE)):
        return 'PhD'
    if bool(re.search(r'^sc.?d.?$', degree, re.IGNORECASE)):
        return 'ScD'
    if bool(re.search(r'^m.?s.?$', degree, re.IGNORECASE)):
        return 'MS'
    if degree == '0':
        return None
    else:
        return degree


def remove_extra(title):
    """Remove the extra words from title"""
    stop_words = ['is', 'of', 'in', 'biostatistics']
    split_title = title.split()
    result_title = [word for word in split_title if word.lower() not in stop_words]
    return ' '.join(result_title)


# Set up the dictionaries
degrees_dict = {}
titles_dict = {}

with open('faculty.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header

    # Build a dict of faculty members
    faculty_dict = {rows[0]: {'degree': rows[1], 'title': rows[2], 'email': rows[3]} for rows in reader}
    for key in faculty_dict:
        # Format the titles to avoid multiple keys for same title and add to dictionary
        title = remove_extra(faculty_dict[key]['title'])
        titles_dict[title] = titles_dict.get(title, 0) + 1

        # Build dict of degrees
        degrees = faculty_dict[key]['degree']
        degrees_list = degrees.split()
        for degree in degrees_list:
            degree = format_degree(degree)  # Avoid duplicate keys
            if degree:
                degrees_dict[degree] = degrees_dict.get(degree, 0) + 1

    print(degrees_dict)
    print(len(degrees_dict))
    print(titles_dict)
    print(len(titles_dict))


# Create list of email addresses
email_addresses = []
domains = []
for i, line in enumerate(open('faculty.csv')):
    for email in re.findall(r'[a-zA-Z0-9]+@[a-zA-Z\.]+\.[a-zA-Z]+', line):
        email_addresses.append(email)
        domains.append(email.split('@')[1])
print(email_addresses)
print(set(domains))
print(len(set(domains)))