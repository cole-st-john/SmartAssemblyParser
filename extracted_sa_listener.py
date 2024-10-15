from manually_modified_parser.SADATAListener import SADATAListener
from manually_modified_parser.SADATAParser import SADATAParser


class ExtractedSAListener(SADATAListener):
    """An ANTLR4 listener for .tab files  - current stubs just provide for writing the names of the data structures to an output file."""

    def __init__(self, out_stream, indent="    "):
        """Instantiates a listener with a given output stream, and an option configurable indent."""
        super().__init__()
        self.__out = out_stream
        self.__indent_level = 0
        self.__indent = indent

    def __write(self, s):
        self.__out.write(s)

    def __line(self, s):
        pfix = self.__indent * self.__indent_level
        self.__write(pfix)
        self.__write(s)
        self.__write("\n")

    def enterData_structure_of_interest(
        self, ctx: SADATAParser.Data_structure_of_interestContext
    ):
        txt = "Data_structure:" + ctx.getText().strip()
        self.__line(txt)
