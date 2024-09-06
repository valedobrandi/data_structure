
def software_monitor(data):
    stable = []
    current_group = []
    for n in data + [0]:
        if n == 1:
            current_group.append(n)
        elif current_group:
            stable.append(current_group)
            current_group = []
    return max(len(group) for group in stable)


print(software_monitor([0, 1, 1, 1, 0, 0, 1, 1]))

print(software_monitor([1, 1, 1, 1, 0, 0, 1, 1]))