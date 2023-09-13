import sys

from parser_lib.args import parse_args
from parser_lib.parse_instructions import parse_instructions
args = parse_args(sys.argv[1:])

with open(args.infile) as f:
    args.instructions = f.readlines()

instructions = parse_instructions(args.instructions)
env_file = ""
with open(".env", "w") as f:
    temp_str = f"SOURCE={instructions['SOURCE']}\n"
    f.write(temp_str)
    env_file += temp_str
    for k, v in instructions["data"].items():
        temp_str = f"{k}={v}\n"
        f.write(temp_str)
        env_file += temp_str

print(env_file)
