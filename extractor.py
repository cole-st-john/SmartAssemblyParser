"""
Usage: python.exe -m extractor <Input Path(.tab)> <Output Path(.txt/.tab)>

**  Example Usage: python.exe -m extractor "examples\\test1.tab" "out\\test1.tab"  **

Extracts data structure names from SmartAssembly (.tab), into a standardised human readable format.

This script does not do any validation.  Invalid syntax of the arguments or the the input file will result in an error.

ANTLR4-based CLI tool for .tab files - providing a basis for deeper Smartassembly automation static analysis and coding tools.
"""

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from manually_modified_parser.SADATALexer import SADATALexer
from manually_modified_parser.SADATAParser import SADATAParser
from extracted_sa_listener import ExtractedSAListener
import argparse


def sa_data_parse(in_path, out_stream):
    """Parses a .tab file, outputting a stream of data structure names."""
    input = FileStream(in_path)
    lexer = SADATALexer(input)
    stream = CommonTokenStream(lexer)
    parser = SADATAParser(stream)
    tree = parser.program()  # the first rule
    actionable_parsed = ExtractedSAListener(out_stream)
    walker = ParseTreeWalker()  # future
    walker.walk(actionable_parsed, tree)  # future


# Example Usage
if "__name__" == "__main__":
    sa_data_parse(r"examples\test1.tab", r"out\test1.tab")


def main():
    """Main script function, providing a simple CLI for the functionality (extracting data structures)."""
    parser = argparse.ArgumentParser(
        description="Data structure extractor for .tab files."
    )
    parser.add_argument("inpath", type=str, help="The path to the .tab file to format")
    parser.add_argument("outpath", type=str, help="The path to write output to")
    args = parser.parse_args()
    if not all([args.inpath, args.outpath]):
        print("Invalid input arguments.  Leaving application.")
        exit()

    with open(args.outpath, "w", encoding="utf8", newline="\r\n") as output:
        sa_data_parse(args.inpath, output)


if __name__ == "__main__":
    main()
