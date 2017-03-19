import re

email_addresses = []

# from advanced_python_regex
with open('faculty.csv') as file:
    for i, line in enumerate(file):
        for email in re.findall(r'[a-zA-Z0-9]+@[a-zA-Z\.]+\.[a-zA-Z]+', line):
            email_addresses.append(email)
    #print(email_addresses)

with open('emails.csv', 'w') as email_csv:
    for email in email_addresses:
        email_csv.write(email + '\n')