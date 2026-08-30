contacts = ["Alice", "Bob", "Charlie", "David", "Eve"]

name = input("Enter a name: ")

low = 0
high = len(contacts) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if contacts[mid] == name:
        found = True
        break
    elif contacts[mid] < name:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Name is in the contacts list.")
else:
    print("Name is not in the contacts list.")
