import argparse
import typing


class ParsedArgs:
    infile: str
    outfile: str

    def __init__(self, infile: str, outfile: str):
        self.infile = infile
        self.outfile = outfile


def parse_args(args: typing.Sequence):
    cl_arg_parser = argparse.ArgumentParser()
    cl_arg_parser.add_argument(
        "-i", "--infile",
        type=str,
        required=True,
        help="Input file of runner installation instructions from bitbucket or github."
    )
    cl_arg_parser.add_argument(
        "-o", "--outfile",
        type=str,
        default=None,
        required=False,
        help="Output file for parsed values, used in debugging."
    )
    namespace_args = cl_arg_parser.parse_args(args)
    return ParsedArgs(
        infile=namespace_args.infile,
        outfile=namespace_args.outfile
    )
