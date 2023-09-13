import os
import typing
import uuid

from .lib import get_next_element


def clean_github_line(raw: str) -> str:
    """
        Some github lines have comments suffixed when copied from web.
    :param raw: string
    :return: string
    """
    return raw.lstrip('"').rstrip('"').split("#")[0]


def parse_github(instructions: typing.List[str]) -> dict:
    ret = {
        "DOWNLOAD_URL": None,
        "DOWNLOAD_OUTPUT": None,
        "GITHUB_HASH": None,
        "REPO_URL": None,
        "GITHUB_TOKEN": None,
        "RUNNER_GROUP": "Default",
        "RUNNER_NAME": os.getenv("HOSTNAME", f"default-name-{uuid.uuid4().hex}"),
        "ADDITIONAL_LABELS": "dockerized",
        "WORK_DIR": "_work",
        "RUNNER_ALLOW_RUNASROOT": 1
    }
    for line in instructions:
        split_line = line.strip().split()
        if "curl -o" in line:
            ret["DOWNLOAD_URL"] = clean_github_line(
                get_next_element(split_line, "-L")
            )
            ret["DOWNLOAD_OUTPUT"] = clean_github_line(
                get_next_element(split_line, "-o")
            )
        elif "echo" in line:
            ret["GITHUB_HASH"] = clean_github_line(
                get_next_element(split_line, "echo")
            )
        elif "./config.sh" in line:
            ret["REPO_URL"] = clean_github_line(
                get_next_element(split_line, "--url")
            )
            ret["GITHUB_TOKEN"] = clean_github_line(
                get_next_element(split_line, "--token")
            )
    return ret
