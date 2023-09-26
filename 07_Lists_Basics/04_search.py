n = int(input())
word = input()
some_list = []
current_list = []
for _ in range(n):
    current_string = input()
    some_list.append(current_string)
    if word in current_string:
        current_list.append(current_string)

print(some_list)
print(current_list)