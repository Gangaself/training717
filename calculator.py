# write a calculator that can handle basic arithmetic operations,and the calculator with terminal interface
# and can evaluate expressions from the command line.
import sys
import operator
import re
import argparse
import tkinter as tk
from tkinter import messagebox

def evaluate_expression(expression):
    # 只允许数字、运算符和括号
    if not re.match(r'^[\d+\-*/().\s]+$', expression):
        raise ValueError("Expression contains invalid characters")
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")

def gui_calculate():
    expr = entry.get()
    try:
        result = evaluate_expression(expr)
        result_label.config(text=f"结果: {result}")
    except Exception as e:
        messagebox.showerror("错误", str(e))

def run_gui():
    window = tk.Tk()
    window.title("简易计算器")

    tk.Label(window, text="请输入算术表达式:").pack()
    global entry
    entry = tk.Entry(window, width=30)
    entry.pack()

    calc_btn = tk.Button(window, text="计算", command=gui_calculate)
    calc_btn.pack()

    global result_label
    result_label = tk.Label(window, text="结果: ")
    result_label.pack()

    window.mainloop()

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
    import sys
    if len(sys.argv) == 1:
        run_gui()
    else:
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