text = input().split()
command = input().split()
while command[0] != "3:1":
    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(text) - 1:
            end_index = len(text) - 1
        merged_elements = "".join(text[start_index:end_index + 1])
        text[start_index:end_index + 1] = [merged_elements]
    elif command[0] == "divide":
        index = int(command[1])
        partition = int(command[2])
        element_for_change = text[index]
        partition_count = len(element_for_change) // partition
        result = []
        for curr_element in range(partition):
            if curr_element != partition - 1:
                result.append(element_for_change[curr_element * partition_count:(curr_element + 1) * partition_count])
            else:
                result.append(element_for_change[curr_element * partition_count:])
        text[index:index + 1] = result
    command = input().split()

print(" ".join(text))
