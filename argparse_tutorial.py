"""
here we are writing a program that takes 3 inputs,
1,first number
2, second number
3, operation : add, subtract multiply

it should return result of operation based on inputs
"""

"""
To make argument optional just add __ in front of argument name
"""
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    #add arguments to parser all positional arguments
    #parser.add_argument("number1", help="first number")
    #parser.add_argument("number2", help="second number")
    #parser.add_argument("operation", help="operation")

    #add arguments to parser all optional arguments
    parser.add_argument("--number1", help="first number")
    parser.add_argument("--number2", help="second number")
    parser.add_argument("--operation", help="operation", \
                        choices=["add", "subtract", "multiply"])

    args = parser.parse_args() # args is a object which has the value of arguments which
    #user has passed  using command line
    """
    two types of arguments:
        positional
        optional
        
    """

    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.operation == "add":
        result = n1 + n2

    elif args.operation == "subtract":
        result = n1 - n2

    elif args.operation == "multiply":
        result = n1 * n2

    else:
        print("unsupported operation")

    print(result)