def add(n1,n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operation={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    process=True
    x=float(input("Enter the first number: "))
    while process:
        symbol=input("Enter a choice of operation: +,-,*,/: ")
        if symbol in list(operation.keys()):
                y=float(input("Enter the second number: "))
                result=operation[symbol](x,y)
                keep_going=input("Do you want to continue? Enter yes to continue, no to restart, any character to finish. ")
                if keep_going=='yes':
                    x=result
                elif keep_going=='no':
                    print(result)
                    process=False
                    calculator()
                elif keep_going!='yes' and keep_going!='no':
                    print(result)
                    return
        else:
            symbol = input("Enter a choice of operation: +,-,*,/: ")

calculator()


