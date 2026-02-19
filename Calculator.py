
print("Welcome to the calculator!")

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations = {
    "add": add,
              "subtract": subtract,
              "multiply": multiply,
              "divide": divide
              }

def available_operations():
    print(f"\nAvailable operations: {', '.join(operations.keys())}\n")

def calculator(a,b,operation):
    return operations[operation](a,b)

def user_input():
    return input("\nEnter the operation: ").lower()

def main():

    available_operations()
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = user_input()
        result = calculator(a,b,operation)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        return
    except KeyError as e:
        print(f"Invalid operation: {e.args[0]}")
        return
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

if __name__ == "__main__":
    main()