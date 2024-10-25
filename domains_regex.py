
""" Task 1: Email Extraction Enhancement

Problem Statement: You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains (e.g., '[exclude.com](http://exclude.com/)'). Modify the script to extract all email addresses except those from the specified domain.

Code Example:

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)
Adapt the regex pattern to exclude email addresses from '[exclude.com](http://exclude.com/)'.

Ensure the script still extracts all other valid email addresses.  """


import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

def find_excluded():
    excluded = re.finditer(r"(\b[A-Za-z0-9._%+-]+@((\b[excl]\w*)[A-Za-z0-9.-]+)\.[A-Z|a-z]{2,}\b)", text)
    if excluded:
        blocked_email_list = []

        for match in excluded:
            blocked = match.group(0)
            blocked_email_list.append(blocked)
            emails.remove(blocked)
            
            print(f'These emails were blocked: {blocked_email_list}')
            print(f'The list of valid emails: {emails}')

find_excluded()