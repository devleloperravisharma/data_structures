def reverse_string(s):
    # Base Case
    if len(s) == 0:
        return ""

    # Recursive Step
    return s[-1] + reverse_string(s[:-1])


# Example
text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))