
def add(n1 , n2):
    """
    this funtion gives addition
    """
    return n1 + n2

def sub(n1, n2):
    """
    this function gives subtraction
    """
    return n1 - n2

def multiply(n1, n2):
    """
        this function gives multiplication
        """
    return n1 * n2

def divide(n1, n2):
    """
        this function gives division
        """
    return n1/n2


#ToDO: store function in an dictionary

operations = {
           "+" : add,
           "-" : sub,
           "*":multiply,
           "/":divide
           }


def calculator():
    should_continue = True
    first_number = float(input("Enter first number: \n"))

    while should_continue:
        for symbols in operations:
            print(symbols)
        operation_symbol = input("Enter the symbol you want to choose: \n")
        second_number = float(input("Enter Second number: \n"))
        answer = operations[operation_symbol](first_number,second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {answer}")

        choice = input(f"Type 'yes' if you want to continue the {answer}, or type 'No' to start fresh \n").lower()

        if choice == "yes":
            first_number = answer
        else:
            should_continue = False
            print("\n" * 30)
            calculator()

calculator()
