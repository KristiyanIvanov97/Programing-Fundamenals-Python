some_string = input()
times_to_repeat = int(input())

repeat_string = lambda string, times: string * times

result = repeat_string(some_string, times_to_repeat)
print(result)
