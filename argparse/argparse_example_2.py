"""
Mutually exclusive group example.
"""
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument('--add', action='store_true')
group.add_argument('--subtract', action='store_true')
parser.add_argument('x', type=int)
parser.add_argument('y', type=int)

args = parser.parse_args()

if args.add:
    sum = args.x + args.y
    print('Sum:', sum)
elif args.subtract:
    difference = args.x - args.y
    print('Difference:', difference)
