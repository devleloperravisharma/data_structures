numbers = [6, 18, 7, 21, 4, 16, 8, 23, 5, 21, 4, 24]
ask = int(input("what number would you want to know if we have said number acquired in the list?"))
# found = False
# for number in numbers:
#     if number == ask:
#         print("yes!!")
#         found = True
#         break
# if found == False:
#     print("no :(")

#--------------------------

for i in range(len(numbers)):
    print(numbers[i])
if ask in numbers:
    print("yes!!!!!")
else:
    print("nooooo")
