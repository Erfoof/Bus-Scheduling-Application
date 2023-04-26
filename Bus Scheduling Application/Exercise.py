entry1 = int(input("First number? "))
entry2 = int(input("Second number? "))
choice = input("Input A to find the sum of the numbers"
               "Input M to find the product of the numbers")
if choice.upper() == "A":
    answer = entry1 + entry2
elif choice.upper() == "M":
    answer = entry1 * entry2
else:
    print("Wrong entry!")
print(answer)