import typing
from .parse_bitbucket import parse_bitbucket
from .parse_github import parse_github


def parse_instructions(instructions: typing.List[str]) -> dict:
    for line in instructions:
        if "atlassian" in line:
            return {
                "SOURCE": "BITBUCKET",
                "data": parse_bitbucket(instructions)
            }
        if "github" in line:
            return {
                "SOURCE": "GITHUB",
                "data": parse_github(instructions)
            }
    print("Unknown input.")
