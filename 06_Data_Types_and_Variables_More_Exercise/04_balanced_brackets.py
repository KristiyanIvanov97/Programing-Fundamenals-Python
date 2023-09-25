number_of_lines = int(input())
isBalanced = False
temporary_char = ""
for _ in range(number_of_lines):
    current_char = input()
    if current_char == "(":
        temporary_char += "("
    elif current_char == ")":
        temporary_char += ")"
    if temporary_char == ")":
        isBalanced = False
        break
    elif temporary_char == "()":
        temporary_char = ""

if temporary_char == "":
    isBalanced = True
if isBalanced:
    print("BALANCED")
else:
    print("UNBALANCED")

