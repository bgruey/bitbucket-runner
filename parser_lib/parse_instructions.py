import typing
from .parse_bitbucket import parse_bitbucket


def parse_instructions(instructions: typing.List[str]):
    for line in instructions:
        if "atlassian" in line:
            return parse_bitbucket(instructions)
    print("Unknown input.")
