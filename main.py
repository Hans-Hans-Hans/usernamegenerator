from typing import List

def username_generator(name: str) -> List(str):
    cleanedUsername = name.strip().split()

    firstname = cleanedUsername[0]
    lastname = cleanedUsername[1]

    print(f"Firstname: {firstname}, Lastname: {lastname}")

if __name__ == "__main__":
    username_generator("John Doe")