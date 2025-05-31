from typing import List
import re

def is_valid_name(name: str) -> bool:
    usernamePattern = r"^[A-Za-z]+(?:[-'][A-Za-z]+)*\s+[A-Za-z]+(?:[-'][A-Za-z]+)*$"
    return bool(re.match(usernamePattern, name))

def username_generator(name: str) -> List[str]:
    cleanedUsername = []

    if is_valid_name(name):
        cleanedUsername = name.strip().split()
    else:
        print("Please input a valid name...")
        return username_generator(input("Please input a first and last name: "))

    firstname = cleanedUsername[0].replace("'", "").replace("-", "")
    lastname = cleanedUsername[1].replace("'", "").replace("-", "")

    firstnameUpper = firstname.upper()
    lastnameUpper = lastname.upper()

    firstnameLower = firstname.lower()
    lastnameLower = lastname.lower()

    firstIUpper = firstname[0].upper()
    lastIUpper = lastname[0].upper()

    firstILower = firstname[0].lower()
    lastILower = lastname[0].lower()

    firstnames = [firstname, firstnameUpper, firstnameLower, firstIUpper, firstILower]
    lastnames = [lastname, lastnameUpper, lastnameLower, lastIUpper, lastILower]

    connectors = [".", "-", "_"]
    finalUsernameList = []

    for fname in firstnames:
        for lname in lastnames:
            finalUsernameList.append(fname + lname)
            finalUsernameList.append(lname + fname)
            for connector in connectors:
                finalUsernameList.append(fname + connector + lname)
                finalUsernameList.append(lname + connector + fname)

    filteredUsernames = []

    for usernames in finalUsernameList:
        if len(usernames) > 3:
            filteredUsernames.append(usernames)



    print(f"Here is your list of potential usernames: {filteredUsernames}")

if __name__ == "__main__":
    username_generator(input("Please input a first and last name: "))