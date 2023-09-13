import typing

START_ARG_PARSE_DICT = {
    "accountUuid": "ACCOUNT_UUID",
    "runnerUuid": "RUNNER_UUID",
    "OAuthClientId": "OAUTH_CLIENT_ID",
    "OAuthClientSecret": "OAUTH_CLIENT_SECRET"
}


def parse_bitbucket(instructions: typing.List[str]) -> dict:
    ret = {
        "DOWNLOAD_URL": None,
        "ACCOUNT_UUID": None,
        "RUNNER_UUID": None,
        "OAUTH_CLIENT_ID": None,
        "OAUTH_CLIENT_SECRET": None,
        "RUN_TIME": "linux-shell",
        "WORK_DIR": "../temp"
    }
    for line in instructions:
        if line.startswith("curl"):
            ret["DOWNLOAD_URL"] = line.strip().split()[1]
        elif line.startswith("./start.sh"):
            split_line = line.strip().split()
            for i, word in enumerate(split_line):
                for k, v in START_ARG_PARSE_DICT.items():
                    if k in word:
                        ret[v] = split_line[i+1]
    return ret
