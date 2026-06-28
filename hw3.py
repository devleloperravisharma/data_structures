# List of contacts
contacts = ["mimi", "rashi", "ravi", "shubha", "raeya", "prestin", "abhimanyu", "dushyant", "navya", "rita", "rajendra", "siddhant", "maa"]

# User input
name = input("Who are you looking for? ")

# Linear Search
found = False

for i in range(len(contacts)):
    if contacts[i] == name:
        print("Found", name, "at index", i)
        found = True
        break

if not found:
    print("Contact not found")