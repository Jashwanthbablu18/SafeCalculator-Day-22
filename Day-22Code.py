# Day 22 - Safe Calculator using Exception Handling

# This defines the safe calculator function
def safe_calculator():
    # A welcome msg with an intimation.
    print("🧮 Welcome to the Safe Calculator! (type 'q' to quit)\n")

    # This loop runs until it breaks (Breaks when typed q)
    while True:

        # Try block (This consists of the code which produces less/no errors).
        try:
            # Asks input1 for the user, if user enters 'q' then it quits by breaking the loop.
            num1 = input("Enter first number: ")
            if num1.lower() == 'q':
                break
            # else stores that number in 'num1' as float.
            num1 = float(num1)

            # Asks user for operation to perform by displaying available operations.
            op = input("Enter operator (+, -, *, /): ")
            # If the entered operator is not in the given list then it raises error with user friendly msg. 
            if op not in ['+', '-', '*', '/']:
                raise ValueError("❌ Invalid operator!")

            # Asks input2 for the user, if user enters 'q' then it quits by breaking the loop.
            num2 = input("Enter second number: ")
            if num2.lower() == 'q':
                break
            # else stores that number in 'num2' as float.
            num2 = float(num2)

            # Here we are performing operations based on the operator choosen.
            # if operator is + then it performs the addition operation
            if op == '+':
                result = num1 + num2
            # if operator is - then it performs the subraction operation
            elif op == '-':
                result = num1 - num2
            # if operator is * then it performs the multiplication operation
            elif op == '*':
                result = num1 * num2
            # if operator is / then it performs the division operation
            elif op == '/':
                # So, if the num2 is 0 then in this case it raises the error with user friendly msg that numerator cannot be divided by 0.
                if num2 == 0:
                    raise ZeroDivisionError("🚫 Cannot divide by zero!")
                # if num2 isn't zero then performs division operation successfully.
                result = num1 / num2

            # Then finally displays the result
            print(f"✅ Result: {result}\n")

        # These handles the value erros(like strs in place of ints), zero division error(Division by zero) and any other exceptions.
        except ValueError as ve:
            print("It's a Value Error")
            print(f"⚠️ Error: {ve}\n")
        except ZeroDivisionError as zde:
            print("It's a Zero Division Error")
            print(f"⚠️ Error: {zde}\n")
        except Exception as e:
            print("This is an unexpeced error")
            print(f"⚠️ Unexpected Error: {e}\n")


# calling main() to starting execution of program
if __name__ == "__main__":
    safe_calculator()

