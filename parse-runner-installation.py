import sys

from parser_lib.args import parse_args
from parser_lib.parse_instructions import parse_instructions
args = parse_args(sys.argv[1:])

with open(args.infile) as f:
    args.instructions = f.readlines()

parse_instructions(args.instructions)
