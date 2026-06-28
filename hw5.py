# List of numbers
numbers = [45, 12, 89, 34, 7, 56]

# Insertion Sort in Descending Order
for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1

    while j >= 0 and key > numbers[j]:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = key

# Display the sorted list
print("Sorted list in descending order:", numbers)