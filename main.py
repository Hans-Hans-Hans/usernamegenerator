from typing import List
import re

NAME_PATTERN = r"^[A-Za-z]+(?:[-'][A-Za-z]+)*\s+[A-Za-z]+(?:[-'][A-Za-z]+)*$"
CONNECTORS = [".", "-", "_"]

def is_valid_name(name: str) -> bool:
    return bool(re.match(NAME_PATTERN, name))

def clean_name_part(name_part: str) -> str:
    return name_part.replace("'", "").replace("-", "")

def username_generator(name: str) -> List[str]:
    if not is_valid_name(name):
        raise ValueError("Invalid name format. Please input a first and last name separated by space.")
    
    parts = name.strip().split()
    firstname = clean_name_part(parts[0])
    lastname = clean_name_part(parts[1])

    # Prepare different case versions
    firstnames = [firstname, firstname.upper(), firstname.lower(), firstname[0].upper(), firstname[0].lower()]
    lastnames = [lastname, lastname.upper(), lastname.lower(), lastname[0].upper(), lastname[0].lower()]

    usernames = []

    for fname in firstnames:
        for lname in lastnames:
            # Without connector
            usernames.append(fname + lname)
            usernames.append(lname + fname)
            # With connectors
            for conn in CONNECTORS:
                usernames.append(fname + conn + lname)
                usernames.append(lname + conn + fname)

    # Filter usernames longer than 3 chars
    filtered_usernames = [u for u in usernames if len(u) > 3]

    # Remove duplicates while preserving order
    seen = set()
    unique_usernames = []
    for u in filtered_usernames:
        if u not in seen:
            unique_usernames.append(u)
            seen.add(u)

    with open("usernamelist.txt", "w") as file:
        for uname in unique_usernames:
            file.write(uname + "\n")

    return unique_usernames

def main():
    while True:
        user_input = input("Please input a first and last name: ")
        try:
            usernames = username_generator(user_input)
            print("Here is your list of potential usernames:")
            for u in usernames:
                print(u)
            break
        except ValueError as e:
            print(e)
            print("Try again.\n")

if __name__ == "__main__":
    main()
