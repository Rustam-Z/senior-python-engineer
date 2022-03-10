"""
How to run: python argparse_example.py --name Rustam --age 20 100 200 --values 1 2 3

1. --name is a required arg (flag)
2. x, y are positional arguments
3. --age is an optional argument
4. Multiple Input Arguments
5. Mutually Exclusive Arguments, depending on one argument, you want to restrict the use of another.
6. Subparser

https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
"""

import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--age', type=int)
parser.add_argument('x', type=int, help='The first value to multiply')
parser.add_argument('y', type=int, help='The second value to multiply')
parser.add_argument('--values', type=int, nargs=3)  # Multiple Input Arguments, nargs='+

# Parse the argument
args = parser.parse_args()

sum_ = sum(args.values)

# Print "Hello" + the user input argument
print('Checking...', args.name)

if args.age:
    print(args.name, 'is', args.age, 'years old.')
else:
    print('Hello,', args.name + '!')

print('Multiplication:', args.x * args.y)
print('Sum:', sum_)
