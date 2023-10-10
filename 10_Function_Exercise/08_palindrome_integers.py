list_of_integers = input().split(", ")

for curr_int in list_of_integers:
    if curr_int == curr_int[::-1]:
        print("True")
    else:
        print("False")
