print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = float(first_number)/float(second_number)
    except ZeroDivisionError:
        print("You can not divide by zero")
    except ValueError:
        print("Your input has to be only numbers")
    else:
        print(answer)