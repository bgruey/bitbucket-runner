import typing
from .parse_bitbucket import parse_bitbucket


def parse_instructions(instructions: typing.List[str]) -> dict:
    for line in instructions:
        if "atlassian" in line:
            return {
                "SOURCE": "BITBUCKET",
                "data": parse_bitbucket(instructions)
            }
    print("Unknown input.")
