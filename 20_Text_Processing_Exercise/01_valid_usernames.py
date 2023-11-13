def length_is_valid(usernames):
    if 3 <= len(username) <= 16:
        return True
    return False


def characters_are_valid(usernames):
    for characters in usernames:
        if not (characters.isalnum() or characters == "-" or characters == "_"):
            return False
    return True


def no_redundant_symbols(usernames):
    if " " in usernames:
        return False
    return True


def isvalid(usernames):
    if length_is_valid(usernames) and characters_are_valid(usernames) and no_redundant_symbols(usernames):
        return True
    return False


usernames = input().split(", ")

for username in usernames:
    if isvalid(username):
        print(username)
