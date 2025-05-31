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

    firstname = cleanedUsername[0]
    lastname = cleanedUsername[1]


    print(f"Firstname: {firstname}, Lastname: {lastname}")

if __name__ == "__main__":
    username_generator(input("Please input a first and last name: "))