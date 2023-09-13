import typing


def get_next_element(elements: typing.List[str], key: str) -> str:
    for i, word in enumerate(elements):
        if word == key:
            return elements[i+1]