string = input().split()
new_list = []
for current_int in string:
    current_int = -int(current_int)
    new_list.append(current_int)

print(new_list)