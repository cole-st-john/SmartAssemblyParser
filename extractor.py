"""
Data structure extractor for .tab files.

Usage: python.exe -m extractor <Input Path(.tab)> <Output Path(.txt/.tab)>

Example Usage:
    python.exe -m extractor "examples\\test1.tab" "out\\test1.tab"

This script extracts data structure names from SmartAssembly (.tab) files into a standardized, human-readable format.

Note: The script does not validate input file contents. Invalid file syntax will result in an error.
"""

import os
import argparse
import textwrap
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from manually_modified_parser.SADATALexer import SADATALexer
from manually_modified_parser.SADATAParser import SADATAParser
from extracted_sa_listener import ExtractedSAListener


def sa_data_parse(in_path, out_stream):
    """Parses a .tab file, outputting a stream of data structure names."""
    try:
        input_stream = FileStream(in_path)
        lexer = SADATALexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SADATAParser(token_stream)
        tree = parser.program()  # Start rule
        listener = ExtractedSAListener(out_stream)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
    except Exception as e:
        print(f"Error during parsing: {e}")
        exit(1)


def validate_paths(in_path, out_path):
    """Validates input and output paths for existence and correct extensions."""
    if not os.path.isfile(in_path):
        print(f"Error: Input file '{in_path}' does not exist.")
        exit(1)

    if not in_path.endswith(".tab"):
        print("Error: Input file must have a '.tab' extension.")
        exit(1)

    if not out_path.endswith((".txt", ".tab")):
        print("Error: Output file must have a '.txt' or '.tab' extension.")
        exit(1)


def main():
    """Main function providing a simple CLI for extracting data structures."""
    parser = argparse.ArgumentParser(
        description=textwrap.dedent("""\
            Data structure extractor for .tab files.
            
            Extracts data structure names from SmartAssembly (.tab) files into a standardized human-readable format.
            
            Example usage:
                python.exe -m extractor "examples\\test1.tab" "out\\test1.tab"
        """),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("inpath", type=str, help="Path to the input .tab file.")
    parser.add_argument("outpath", type=str, help="Path to the output .txt/.tab file.")
    args = parser.parse_args()

    validate_paths(args.inpath, args.outpath)

    try:
        with open(args.outpath, "w", encoding="utf8", newline="\r\n") as output:
            sa_data_parse(args.inpath, output)
        print(f"Data successfully extracted to '{args.outpath}'")
    except Exception as e:
        print(f"Failed to write output: {e}")
        exit(1)


if __name__ == "__main__":
    main()
