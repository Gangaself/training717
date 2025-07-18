
# write a calculator that can handle basic arithmetic operations,and the calculator with terminal interface
# and can evaluate expressions from the command line.
import sys
import operator
import re
import argparse

def evaluate_expression(expression):
    # Define the supported operations
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    # Split the expression into tokens
    tokens = re.findall(r'\d+|[+\-*/]', expression)

    if len(tokens) < 3 or len(tokens) % 2 == 0:
        raise ValueError("Invalid expression format")

    # Initialize the result with the first number
    result = float(tokens[0])

    # Iterate through the tokens and apply operations
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        next_num = float(tokens[i + 1])
        if op in operations:
            result = operations[op](result, next_num)
        else:
            raise ValueError(f"Unsupported operation: {op}")

    return result
def main():
    parser = argparse.ArgumentParser(description='Simple Calculator')
    parser.add_argument('expression', type=str, help='Arithmetic expression to evaluate')
    args = parser.parse_args()

    
    if args.expression is None:
        expression = input("Enter an arithmetic expression: ")
    else:
        expression = args.expression
        
    try:
        result = evaluate_expression(args.expression)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    if len(sys.argv) == 1:
        print("No expression provided. Please provide an arithmetic expression to evaluate.")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many arguments provided. Please provide only one arithmetic expression.")
        sys.exit(1)
    if len(sys.argv) == 2:
        expression = sys.argv[1]
        try:
            result = evaluate_expression(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()
# This script provides a simple command-line calculator that can evaluate basic arithmetic expressions.
# It supports addition, subtraction, multiplication, and division.
# The user can input an expression in the form of "number operator number" (e.g., "3 + 4 * 2").
# The script will parse the expression, evaluate it, and print the result.
# It also handles errors such as invalid expressions and unsupported operations.
# The calculator can be run from the terminal with an expression as an argument.
# Usage example: ./calculator.py "3 + 4 * 2"  
# The script will output the result of the expression or an error message if the input is invalid.
# Usage example: ./calculator.py "3 + 4 * 2"  