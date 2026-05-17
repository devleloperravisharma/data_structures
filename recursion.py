"""
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)
    

question = input("give a number, the program will sum the digits ")

result = sum_of_digits(int(question))
print(result)
"""

def countdown(n):
    if n <=0:
        print("blast off!!")
        return " "
    else:
        print(n)
        return countdown(n-1)
result = countdown(5)
print(result)