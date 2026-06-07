numbers = [4, 5, 6, 7, 8, 10, 14, 16, 18, 21, 23, 24]
ask = int(input("which number would you like to search for?"))
start = 0
end = len(numbers) - 1
while start <= end:
    mid = (start + end)//2
    if numbers[mid] == ask:
        print(f"yes!! we have your number! at index {mid}")
        break
    elif numbers[mid] < ask:
        start = mid + 1
    elif numbers[mid] > ask:
        end = mid - 1
if start > end:
    print("nope, sorry!")