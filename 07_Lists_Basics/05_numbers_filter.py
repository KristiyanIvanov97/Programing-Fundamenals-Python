n = int(input())
even_numbers = []
odd_numbers = []
positive_numbers = []
negative_numbers = []

for _ in range(n):
    current_int = int(input())
    if current_int >= 0:
        positive_numbers.append(current_int)
    else:
        negative_numbers.append(current_int)

    if current_int % 2 == 0:
        even_numbers.append(current_int)
    else:
        odd_numbers.append(current_int)

command = input()

if command == "even":
    print(even_numbers)
elif command == "odd":
    print(odd_numbers)
elif command == "positive":
    print(positive_numbers)
else:
    print(negative_numbers)


# n = int(input())
#
# some_list = []
# final_list = []
#
# for _ in range(n):
#     current_int = int(input())
#     some_list.append(current_int)
#
# command = input()

# for el in some_list:
#     if command == 'even':
#         if el % 2 == 0:
#             final_list.append(el)
#     elif command == 'odd':
#         if el % 2!= 0:
#             final_list.append(el)
#     elif command == 'positive':
#         if el >= 0:
#             final_list.append(el)
#     elif command == 'negative':
#         if el < 0:
#             final_list.append(el)
#
# print(final_list)


# n = int(input())
#
# some_list = []
# final_list = []
#
# for _ in range(n):
#     current_int = int(input())
#     some_list.append(current_int)
#
# command = input()
#
# if command == "even":
#     final_list = list(filter(lambda x: (x % 2 == 0), some_list))
#     print(final_list)
# if command == "odd":
#     final_list = list(filter(lambda x: (x % 2 != 0), some_list))
#     print(final_list)
# if command == "positive":
#     final_list = list(filter(lambda x: (x >= 0), some_list))
#     print(final_list)
# if command == "negative":
#     final_list = list(filter(lambda x: (x < 0), some_list))
#     print(final_list)
