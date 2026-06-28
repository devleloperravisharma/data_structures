# List of words
words = ["apple", "kiwi", "banana", "pie", "date"]

# Insertion Sort based on word length
for i in range(1, len(words)):
    key = words[i]
    j = i - 1

    while j >= 0 and len(key) < len(words[j]):
        words[j + 1] = words[j]
        j -= 1

    words[j + 1] = key

# Display the sorted list
print("Sorted list:", words)