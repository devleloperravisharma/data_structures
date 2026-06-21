list = [7, 21, 6, 18, 5]
length = len(list)
for i in range(1, len(list)):
    # i points to index
    num = list[i]
    prev_index = i-1
    while prev_index >= 0 and num < list[prev_index]:
        list[prev_index + 1] = list[prev_index]
        prev_index = prev_index-1
    list[prev_index + 1] = num
    print(list)
# STUDY!