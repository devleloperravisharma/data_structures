list = [7, 21, 6, 18, 4, 16, 8, 23, 12, 31, 24]
list = [1, 2, 3, 4, 5, 6]
for i in range(len(list)):
    swap = False
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            p = list[j]
            list[j] = list[j+1]
            list[j+1] = p
            swap = True
            print(list)
    if swap == False:
        break
            
            

