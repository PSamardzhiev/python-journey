from art import logo
#add
def add(n1, n2):
  return n1 + n2


#subtract
def subtract(n1, n2):
  return n1 - n2


#multiply


def multiply(n1, n2):
  return n1 * n2


#divide


def divide(n1, n2):
  return n1 / n2
print(logo)

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
  num1 = float(input("What's the first number: "))

  for symbol in operations:
    print(symbol)

  should_contunue = True
  while should_contunue:
    operation_symbol = input("Please pick an operation symbol: ")
    num2 = float(input("What's the second number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(
        f"Type 'y' to continue calculating with {answer} or n to start new calculation: "
    ) == 'y':
      num1 = answer
    else:
      should_contunue = False
      calculator()


calculator()


