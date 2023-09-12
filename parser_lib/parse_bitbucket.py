import typing


def parse_bitbucket(instructions: typing.List[str]):
    for line in instructions:
        if line.startswith("curl"):
            pass
