# This program demonstrates If, Elif, Else, For loops, While loops, Break, and Continue

# Part 1: Using If, Elif, Else
number = 5
if number > 10:
    print("The number is greater than 10.")
elif number == 10:
    print("The number is exactly 10.")
else:
    print("The number is less than 10.")

# Part 2: Using a For Loop
print("\nFor loop demonstration:")
for i in range(1, 6):
    print(f"Current number in the loop: {i}")
    if i == 3:
        print("Found 3! Breaking the loop.")
        break  # Breaks the loop when i is 3

# Part 3: Using a While Loop
print("\nWhile loop demonstration:")
count = 0
while count < 5:
    count += 1
    if count == 2:
        print("Skipping the number 2.")
        continue  # Skips the current iteration when count is 2
    print(f"Current count: {count}")
    
    if count == 4:
        print("Found 4! Breaking the loop.")
        break  # Breaks the loop when count is 4