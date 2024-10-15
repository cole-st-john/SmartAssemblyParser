# Generated from C:/Users/Cole/OneDrive/CODING/PYTHON/LANGUAGE/sa_data/parser_generator/SADATA.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,207,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,4,0,48,8,0,11,0,12,0,49,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,60,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,
        6,1,7,1,7,4,7,89,8,7,11,7,12,7,90,1,8,1,8,4,8,95,8,8,11,8,12,8,96,
        1,9,1,9,1,9,1,9,4,9,103,8,9,11,9,12,9,104,1,9,1,9,3,9,109,8,9,1,
        10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,123,
        8,12,1,13,1,13,5,13,127,8,13,10,13,12,13,130,9,13,1,13,1,13,1,14,
        1,14,5,14,136,8,14,10,14,12,14,139,9,14,1,14,1,14,1,14,1,15,1,15,
        5,15,146,8,15,10,15,12,15,149,9,15,1,15,1,15,1,15,1,15,1,16,1,16,
        5,16,157,8,16,10,16,12,16,160,9,16,1,16,1,16,1,16,1,16,1,16,1,17,
        1,17,1,17,5,17,170,8,17,10,17,12,17,173,9,17,1,18,1,18,1,18,1,18,
        5,18,179,8,18,10,18,12,18,182,9,18,1,19,1,19,1,19,1,19,1,19,5,19,
        189,8,19,10,19,12,19,192,9,19,1,20,1,20,1,20,1,20,1,20,4,20,199,
        8,20,11,20,12,20,200,1,21,1,21,1,22,1,22,1,22,7,128,137,147,158,
        171,180,190,0,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,0,3,1,0,24,26,1,0,20,21,1,0,19,22,210,0,47,1,0,0,
        0,2,59,1,0,0,0,4,61,1,0,0,0,6,66,1,0,0,0,8,71,1,0,0,0,10,76,1,0,
        0,0,12,81,1,0,0,0,14,88,1,0,0,0,16,94,1,0,0,0,18,108,1,0,0,0,20,
        110,1,0,0,0,22,112,1,0,0,0,24,122,1,0,0,0,26,124,1,0,0,0,28,133,
        1,0,0,0,30,143,1,0,0,0,32,154,1,0,0,0,34,166,1,0,0,0,36,174,1,0,
        0,0,38,183,1,0,0,0,40,193,1,0,0,0,42,202,1,0,0,0,44,204,1,0,0,0,
        46,48,3,2,1,0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,
        0,0,0,50,51,1,0,0,0,51,52,5,0,0,1,52,1,1,0,0,0,53,60,3,6,3,0,54,
        60,3,4,2,0,55,60,3,8,4,0,56,60,3,10,5,0,57,60,3,12,6,0,58,60,3,16,
        8,0,59,53,1,0,0,0,59,54,1,0,0,0,59,55,1,0,0,0,59,56,1,0,0,0,59,57,
        1,0,0,0,59,58,1,0,0,0,60,3,1,0,0,0,61,62,5,10,0,0,62,63,3,22,11,
        0,63,64,3,14,7,0,64,65,5,9,0,0,65,5,1,0,0,0,66,67,5,12,0,0,67,68,
        3,22,11,0,68,69,3,14,7,0,69,70,5,11,0,0,70,7,1,0,0,0,71,72,5,14,
        0,0,72,73,3,22,11,0,73,74,3,16,8,0,74,75,5,13,0,0,75,9,1,0,0,0,76,
        77,5,15,0,0,77,78,3,22,11,0,78,79,3,16,8,0,79,80,5,16,0,0,80,11,
        1,0,0,0,81,82,5,17,0,0,82,83,3,22,11,0,83,84,3,16,8,0,84,85,5,18,
        0,0,85,13,1,0,0,0,86,89,3,18,9,0,87,89,3,20,10,0,88,86,1,0,0,0,88,
        87,1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,15,1,0,0,
        0,92,95,3,18,9,0,93,95,3,20,10,0,94,92,1,0,0,0,94,93,1,0,0,0,95,
        96,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,17,1,0,0,0,98,99,3,24,
        12,0,99,100,3,22,11,0,100,109,1,0,0,0,101,103,3,44,22,0,102,101,
        1,0,0,0,103,104,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,106,
        1,0,0,0,106,107,3,22,11,0,107,109,1,0,0,0,108,98,1,0,0,0,108,102,
        1,0,0,0,109,19,1,0,0,0,110,111,3,22,11,0,111,21,1,0,0,0,112,113,
        7,0,0,0,113,23,1,0,0,0,114,123,3,26,13,0,115,123,3,28,14,0,116,123,
        3,30,15,0,117,123,3,32,16,0,118,123,3,34,17,0,119,123,3,36,18,0,
        120,123,3,38,19,0,121,123,3,40,20,0,122,114,1,0,0,0,122,115,1,0,
        0,0,122,116,1,0,0,0,122,117,1,0,0,0,122,118,1,0,0,0,122,119,1,0,
        0,0,122,120,1,0,0,0,122,121,1,0,0,0,123,25,1,0,0,0,124,128,5,1,0,
        0,125,127,3,44,22,0,126,125,1,0,0,0,127,130,1,0,0,0,128,129,1,0,
        0,0,128,126,1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,132,3,42,
        21,0,132,27,1,0,0,0,133,137,5,2,0,0,134,136,3,44,22,0,135,134,1,
        0,0,0,136,139,1,0,0,0,137,138,1,0,0,0,137,135,1,0,0,0,138,140,1,
        0,0,0,139,137,1,0,0,0,140,141,3,42,21,0,141,142,3,42,21,0,142,29,
        1,0,0,0,143,147,5,3,0,0,144,146,3,44,22,0,145,144,1,0,0,0,146,149,
        1,0,0,0,147,148,1,0,0,0,147,145,1,0,0,0,148,150,1,0,0,0,149,147,
        1,0,0,0,150,151,3,42,21,0,151,152,3,42,21,0,152,153,3,42,21,0,153,
        31,1,0,0,0,154,158,5,4,0,0,155,157,3,44,22,0,156,155,1,0,0,0,157,
        160,1,0,0,0,158,159,1,0,0,0,158,156,1,0,0,0,159,161,1,0,0,0,160,
        158,1,0,0,0,161,162,3,42,21,0,162,163,3,42,21,0,163,164,3,42,21,
        0,164,165,3,42,21,0,165,33,1,0,0,0,166,167,5,5,0,0,167,171,3,42,
        21,0,168,170,3,44,22,0,169,168,1,0,0,0,170,173,1,0,0,0,171,172,1,
        0,0,0,171,169,1,0,0,0,172,35,1,0,0,0,173,171,1,0,0,0,174,175,5,6,
        0,0,175,176,3,44,22,0,176,180,3,42,21,0,177,179,3,44,22,0,178,177,
        1,0,0,0,179,182,1,0,0,0,180,181,1,0,0,0,180,178,1,0,0,0,181,37,1,
        0,0,0,182,180,1,0,0,0,183,184,5,7,0,0,184,185,3,44,22,0,185,186,
        3,44,22,0,186,190,3,42,21,0,187,189,3,44,22,0,188,187,1,0,0,0,189,
        192,1,0,0,0,190,191,1,0,0,0,190,188,1,0,0,0,191,39,1,0,0,0,192,190,
        1,0,0,0,193,194,5,8,0,0,194,195,3,44,22,0,195,196,3,44,22,0,196,
        198,3,44,22,0,197,199,3,42,21,0,198,197,1,0,0,0,199,200,1,0,0,0,
        200,198,1,0,0,0,200,201,1,0,0,0,201,41,1,0,0,0,202,203,7,1,0,0,203,
        43,1,0,0,0,204,205,7,2,0,0,205,45,1,0,0,0,17,49,59,88,90,94,96,104,
        108,122,128,137,147,158,171,180,190,200
    ]

class SADATAParser ( Parser ):

    grammarFileName = "SADATA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'PARSE_STRING'", "'END_GUI_DESCR'", "'BEGIN_GUI_DESCR'", 
                     "'END_ASM_DESCR'", "'BEGIN_ASM_DESCR'", "'END_TABLE_DESCR'", 
                     "'BEGIN_TABLE_DESCR'", "'BEGIN_COMP_DESCR'", "'END_COMP_DESCR'", 
                     "'BEGIN_DEP_DESCR'", "'END_DEP_DESCR'" ]

    symbolicNames = [ "<INVALID>", "FUNCT_1", "FUNCT_2", "FUNCT_3", "FUNCT_4", 
                      "FUNCT_5", "FUNCT_6", "FUNCT_7", "FUNCT_8", "END_GUI_DESCR", 
                      "BEGIN_GUI_DESCR", "END_ASM_DESCR", "BEGIN_ASM_DESCR", 
                      "END_TABLE_DESCR", "BEGIN_TABLE_DESCR", "BEGIN_COMP_DESCR", 
                      "END_COMP_DESCR", "BEGIN_DEP_DESCR", "END_DEP_DESCR", 
                      "STRING", "ID_CANDIDATE", "STRUCT_CANDIDATE", "RAW_STATEMENT", 
                      "ESC", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                      "NEWLINE", "WHITE" ]

    RULE_program = 0
    RULE_big_block = 1
    RULE_gui_block = 2
    RULE_asm_block = 3
    RULE_table_block = 4
    RULE_comp_block = 5
    RULE_dep_block = 6
    RULE_relevant_content = 7
    RULE_non_relevant_content = 8
    RULE_line = 9
    RULE_non_relevant_line = 10
    RULE_eol = 11
    RULE_functional_expression = 12
    RULE_funct_1 = 13
    RULE_funct_2 = 14
    RULE_funct_3 = 15
    RULE_funct_4 = 16
    RULE_funct_5 = 17
    RULE_funct_6 = 18
    RULE_funct_7 = 19
    RULE_funct_8 = 20
    RULE_data_structure_of_interest = 21
    RULE_argument = 22

    ruleNames =  [ "program", "big_block", "gui_block", "asm_block", "table_block", 
                   "comp_block", "dep_block", "relevant_content", "non_relevant_content", 
                   "line", "non_relevant_line", "eol", "functional_expression", 
                   "funct_1", "funct_2", "funct_3", "funct_4", "funct_5", 
                   "funct_6", "funct_7", "funct_8", "data_structure_of_interest", 
                   "argument" ]

    EOF = Token.EOF
    FUNCT_1=1
    FUNCT_2=2
    FUNCT_3=3
    FUNCT_4=4
    FUNCT_5=5
    FUNCT_6=6
    FUNCT_7=7
    FUNCT_8=8
    END_GUI_DESCR=9
    BEGIN_GUI_DESCR=10
    END_ASM_DESCR=11
    BEGIN_ASM_DESCR=12
    END_TABLE_DESCR=13
    BEGIN_TABLE_DESCR=14
    BEGIN_COMP_DESCR=15
    END_COMP_DESCR=16
    BEGIN_DEP_DESCR=17
    END_DEP_DESCR=18
    STRING=19
    ID_CANDIDATE=20
    STRUCT_CANDIDATE=21
    RAW_STATEMENT=22
    ESC=23
    SINGLE_LINE_COMMENT=24
    MULTI_LINE_COMMENT=25
    NEWLINE=26
    WHITE=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SADATAParser.EOF, 0)

        def big_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.Big_blockContext)
            else:
                return self.getTypedRuleContext(SADATAParser.Big_blockContext,i)


        def getRuleIndex(self):
            return SADATAParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = SADATAParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.big_block()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 125490686) != 0)):
                    break

            self.state = 51
            self.match(SADATAParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Big_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asm_block(self):
            return self.getTypedRuleContext(SADATAParser.Asm_blockContext,0)


        def gui_block(self):
            return self.getTypedRuleContext(SADATAParser.Gui_blockContext,0)


        def table_block(self):
            return self.getTypedRuleContext(SADATAParser.Table_blockContext,0)


        def comp_block(self):
            return self.getTypedRuleContext(SADATAParser.Comp_blockContext,0)


        def dep_block(self):
            return self.getTypedRuleContext(SADATAParser.Dep_blockContext,0)


        def non_relevant_content(self):
            return self.getTypedRuleContext(SADATAParser.Non_relevant_contentContext,0)


        def getRuleIndex(self):
            return SADATAParser.RULE_big_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBig_block" ):
                listener.enterBig_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBig_block" ):
                listener.exitBig_block(self)




    def big_block(self):

        localctx = SADATAParser.Big_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_big_block)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.asm_block()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.gui_block()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.table_block()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.comp_block()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.dep_block()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 19, 20, 21, 22, 24, 25, 26]:
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.non_relevant_content()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Gui_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_GUI_DESCR(self):
            return self.getToken(SADATAParser.BEGIN_GUI_DESCR, 0)

        def eol(self):
            return self.getTypedRuleContext(SADATAParser.EolContext,0)


        def relevant_content(self):
            return self.getTypedRuleContext(SADATAParser.Relevant_contentContext,0)


        def END_GUI_DESCR(self):
            return self.getToken(SADATAParser.END_GUI_DESCR, 0)

        def getRuleIndex(self):
            return SADATAParser.RULE_gui_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGui_block" ):
                listener.enterGui_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGui_block" ):
                listener.exitGui_block(self)




    def gui_block(self):

        localctx = SADATAParser.Gui_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_gui_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(SADATAParser.BEGIN_GUI_DESCR)
            self.state = 62
            self.eol()
            self.state = 63
            self.relevant_content()
            self.state = 64
            self.match(SADATAParser.END_GUI_DESCR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asm_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_ASM_DESCR(self):
            return self.getToken(SADATAParser.BEGIN_ASM_DESCR, 0)

        def eol(self):
            return self.getTypedRuleContext(SADATAParser.EolContext,0)


        def relevant_content(self):
            return self.getTypedRuleContext(SADATAParser.Relevant_contentContext,0)


        def END_ASM_DESCR(self):
            return self.getToken(SADATAParser.END_ASM_DESCR, 0)

        def getRuleIndex(self):
            return SADATAParser.RULE_asm_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsm_block" ):
                listener.enterAsm_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsm_block" ):
                listener.exitAsm_block(self)




    def asm_block(self):

        localctx = SADATAParser.Asm_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asm_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(SADATAParser.BEGIN_ASM_DESCR)
            self.state = 67
            self.eol()
            self.state = 68
            self.relevant_content()
            self.state = 69
            self.match(SADATAParser.END_ASM_DESCR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_TABLE_DESCR(self):
            return self.getToken(SADATAParser.BEGIN_TABLE_DESCR, 0)

        def eol(self):
            return self.getTypedRuleContext(SADATAParser.EolContext,0)


        def non_relevant_content(self):
            return self.getTypedRuleContext(SADATAParser.Non_relevant_contentContext,0)


        def END_TABLE_DESCR(self):
            return self.getToken(SADATAParser.END_TABLE_DESCR, 0)

        def getRuleIndex(self):
            return SADATAParser.RULE_table_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_block" ):
                listener.enterTable_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_block" ):
                listener.exitTable_block(self)




    def table_block(self):

        localctx = SADATAParser.Table_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_table_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(SADATAParser.BEGIN_TABLE_DESCR)
            self.state = 72
            self.eol()
            self.state = 73
            self.non_relevant_content()
            self.state = 74
            self.match(SADATAParser.END_TABLE_DESCR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_COMP_DESCR(self):
            return self.getToken(SADATAParser.BEGIN_COMP_DESCR, 0)

        def eol(self):
            return self.getTypedRuleContext(SADATAParser.EolContext,0)


        def non_relevant_content(self):
            return self.getTypedRuleContext(SADATAParser.Non_relevant_contentContext,0)


        def END_COMP_DESCR(self):
            return self.getToken(SADATAParser.END_COMP_DESCR, 0)

        def getRuleIndex(self):
            return SADATAParser.RULE_comp_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_block" ):
                listener.enterComp_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_block" ):
                listener.exitComp_block(self)




    def comp_block(self):

        localctx = SADATAParser.Comp_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comp_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(SADATAParser.BEGIN_COMP_DESCR)
            self.state = 77
            self.eol()
            self.state = 78
            self.non_relevant_content()
            self.state = 79
            self.match(SADATAParser.END_COMP_DESCR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dep_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_DEP_DESCR(self):
            return self.getToken(SADATAParser.BEGIN_DEP_DESCR, 0)

        def eol(self):
            return self.getTypedRuleContext(SADATAParser.EolContext,0)


        def non_relevant_content(self):
            return self.getTypedRuleContext(SADATAParser.Non_relevant_contentContext,0)


        def END_DEP_DESCR(self):
            return self.getToken(SADATAParser.END_DEP_DESCR, 0)

        def getRuleIndex(self):
            return SADATAParser.RULE_dep_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDep_block" ):
                listener.enterDep_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDep_block" ):
                listener.exitDep_block(self)




    def dep_block(self):

        localctx = SADATAParser.Dep_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dep_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(SADATAParser.BEGIN_DEP_DESCR)
            self.state = 82
            self.eol()
            self.state = 83
            self.non_relevant_content()
            self.state = 84
            self.match(SADATAParser.END_DEP_DESCR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relevant_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.LineContext)
            else:
                return self.getTypedRuleContext(SADATAParser.LineContext,i)


        def non_relevant_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.Non_relevant_lineContext)
            else:
                return self.getTypedRuleContext(SADATAParser.Non_relevant_lineContext,i)


        def getRuleIndex(self):
            return SADATAParser.RULE_relevant_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelevant_content" ):
                listener.enterRelevant_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelevant_content" ):
                listener.exitRelevant_content(self)




    def relevant_content(self):

        localctx = SADATAParser.Relevant_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_relevant_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 88
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 4, 5, 6, 7, 8, 19, 20, 21, 22]:
                    self.state = 86
                    self.line()
                    pass
                elif token in [24, 25, 26]:
                    self.state = 87
                    self.non_relevant_line()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 125305342) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_relevant_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.LineContext)
            else:
                return self.getTypedRuleContext(SADATAParser.LineContext,i)


        def non_relevant_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.Non_relevant_lineContext)
            else:
                return self.getTypedRuleContext(SADATAParser.Non_relevant_lineContext,i)


        def getRuleIndex(self):
            return SADATAParser.RULE_non_relevant_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_relevant_content" ):
                listener.enterNon_relevant_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_relevant_content" ):
                listener.exitNon_relevant_content(self)




    def non_relevant_content(self):

        localctx = SADATAParser.Non_relevant_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_non_relevant_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 94
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2, 3, 4, 5, 6, 7, 8, 19, 20, 21, 22]:
                        self.state = 92
                        self.line()
                        pass
                    elif token in [24, 25, 26]:
                        self.state = 93
                        self.non_relevant_line()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 96 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functional_expression(self):
            return self.getTypedRuleContext(SADATAParser.Functional_expressionContext,0)


        def eol(self):
            return self.getTypedRuleContext(SADATAParser.EolContext,0)


        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(SADATAParser.ArgumentContext,i)


        def getRuleIndex(self):
            return SADATAParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = SADATAParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8]:
                self.state = 98
                self.functional_expression()
                self.state = 99
                self.eol()
                pass
            elif token in [19, 20, 21, 22]:
                self.state = 102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 101
                    self.argument()
                    self.state = 104 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                        break

                self.state = 106
                self.eol()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_relevant_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eol(self):
            return self.getTypedRuleContext(SADATAParser.EolContext,0)


        def getRuleIndex(self):
            return SADATAParser.RULE_non_relevant_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_relevant_line" ):
                listener.enterNon_relevant_line(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_relevant_line" ):
                listener.exitNon_relevant_line(self)




    def non_relevant_line(self):

        localctx = SADATAParser.Non_relevant_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_non_relevant_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.eol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_LINE_COMMENT(self):
            return self.getToken(SADATAParser.SINGLE_LINE_COMMENT, 0)

        def NEWLINE(self):
            return self.getToken(SADATAParser.NEWLINE, 0)

        def MULTI_LINE_COMMENT(self):
            return self.getToken(SADATAParser.MULTI_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return SADATAParser.RULE_eol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEol" ):
                listener.enterEol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEol" ):
                listener.exitEol(self)




    def eol(self):

        localctx = SADATAParser.EolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_eol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Functional_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funct_1(self):
            return self.getTypedRuleContext(SADATAParser.Funct_1Context,0)


        def funct_2(self):
            return self.getTypedRuleContext(SADATAParser.Funct_2Context,0)


        def funct_3(self):
            return self.getTypedRuleContext(SADATAParser.Funct_3Context,0)


        def funct_4(self):
            return self.getTypedRuleContext(SADATAParser.Funct_4Context,0)


        def funct_5(self):
            return self.getTypedRuleContext(SADATAParser.Funct_5Context,0)


        def funct_6(self):
            return self.getTypedRuleContext(SADATAParser.Funct_6Context,0)


        def funct_7(self):
            return self.getTypedRuleContext(SADATAParser.Funct_7Context,0)


        def funct_8(self):
            return self.getTypedRuleContext(SADATAParser.Funct_8Context,0)


        def getRuleIndex(self):
            return SADATAParser.RULE_functional_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctional_expression" ):
                listener.enterFunctional_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctional_expression" ):
                listener.exitFunctional_expression(self)




    def functional_expression(self):

        localctx = SADATAParser.Functional_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functional_expression)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.funct_1()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.funct_2()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.funct_3()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 117
                self.funct_4()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 118
                self.funct_5()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 119
                self.funct_6()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 120
                self.funct_7()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 8)
                self.state = 121
                self.funct_8()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funct_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCT_1(self):
            return self.getToken(SADATAParser.FUNCT_1, 0)

        def data_structure_of_interest(self):
            return self.getTypedRuleContext(SADATAParser.Data_structure_of_interestContext,0)


        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(SADATAParser.ArgumentContext,i)


        def getRuleIndex(self):
            return SADATAParser.RULE_funct_1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunct_1" ):
                listener.enterFunct_1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunct_1" ):
                listener.exitFunct_1(self)




    def funct_1(self):

        localctx = SADATAParser.Funct_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_funct_1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(SADATAParser.FUNCT_1)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 125
                    self.argument() 
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 131
            self.data_structure_of_interest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funct_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCT_2(self):
            return self.getToken(SADATAParser.FUNCT_2, 0)

        def data_structure_of_interest(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.Data_structure_of_interestContext)
            else:
                return self.getTypedRuleContext(SADATAParser.Data_structure_of_interestContext,i)


        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(SADATAParser.ArgumentContext,i)


        def getRuleIndex(self):
            return SADATAParser.RULE_funct_2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunct_2" ):
                listener.enterFunct_2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunct_2" ):
                listener.exitFunct_2(self)




    def funct_2(self):

        localctx = SADATAParser.Funct_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funct_2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(SADATAParser.FUNCT_2)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 134
                    self.argument() 
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 140
            self.data_structure_of_interest()
            self.state = 141
            self.data_structure_of_interest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funct_3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCT_3(self):
            return self.getToken(SADATAParser.FUNCT_3, 0)

        def data_structure_of_interest(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.Data_structure_of_interestContext)
            else:
                return self.getTypedRuleContext(SADATAParser.Data_structure_of_interestContext,i)


        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(SADATAParser.ArgumentContext,i)


        def getRuleIndex(self):
            return SADATAParser.RULE_funct_3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunct_3" ):
                listener.enterFunct_3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunct_3" ):
                listener.exitFunct_3(self)




    def funct_3(self):

        localctx = SADATAParser.Funct_3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_funct_3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(SADATAParser.FUNCT_3)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 144
                    self.argument() 
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 150
            self.data_structure_of_interest()
            self.state = 151
            self.data_structure_of_interest()
            self.state = 152
            self.data_structure_of_interest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funct_4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCT_4(self):
            return self.getToken(SADATAParser.FUNCT_4, 0)

        def data_structure_of_interest(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.Data_structure_of_interestContext)
            else:
                return self.getTypedRuleContext(SADATAParser.Data_structure_of_interestContext,i)


        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(SADATAParser.ArgumentContext,i)


        def getRuleIndex(self):
            return SADATAParser.RULE_funct_4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunct_4" ):
                listener.enterFunct_4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunct_4" ):
                listener.exitFunct_4(self)




    def funct_4(self):

        localctx = SADATAParser.Funct_4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_funct_4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(SADATAParser.FUNCT_4)
            self.state = 158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 155
                    self.argument() 
                self.state = 160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 161
            self.data_structure_of_interest()
            self.state = 162
            self.data_structure_of_interest()
            self.state = 163
            self.data_structure_of_interest()
            self.state = 164
            self.data_structure_of_interest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funct_5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCT_5(self):
            return self.getToken(SADATAParser.FUNCT_5, 0)

        def data_structure_of_interest(self):
            return self.getTypedRuleContext(SADATAParser.Data_structure_of_interestContext,0)


        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(SADATAParser.ArgumentContext,i)


        def getRuleIndex(self):
            return SADATAParser.RULE_funct_5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunct_5" ):
                listener.enterFunct_5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunct_5" ):
                listener.exitFunct_5(self)




    def funct_5(self):

        localctx = SADATAParser.Funct_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funct_5)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(SADATAParser.FUNCT_5)
            self.state = 167
            self.data_structure_of_interest()
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 168
                    self.argument() 
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funct_6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCT_6(self):
            return self.getToken(SADATAParser.FUNCT_6, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(SADATAParser.ArgumentContext,i)


        def data_structure_of_interest(self):
            return self.getTypedRuleContext(SADATAParser.Data_structure_of_interestContext,0)


        def getRuleIndex(self):
            return SADATAParser.RULE_funct_6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunct_6" ):
                listener.enterFunct_6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunct_6" ):
                listener.exitFunct_6(self)




    def funct_6(self):

        localctx = SADATAParser.Funct_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funct_6)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(SADATAParser.FUNCT_6)
            self.state = 175
            self.argument()
            self.state = 176
            self.data_structure_of_interest()
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 177
                    self.argument() 
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funct_7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCT_7(self):
            return self.getToken(SADATAParser.FUNCT_7, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(SADATAParser.ArgumentContext,i)


        def data_structure_of_interest(self):
            return self.getTypedRuleContext(SADATAParser.Data_structure_of_interestContext,0)


        def getRuleIndex(self):
            return SADATAParser.RULE_funct_7

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunct_7" ):
                listener.enterFunct_7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunct_7" ):
                listener.exitFunct_7(self)




    def funct_7(self):

        localctx = SADATAParser.Funct_7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_funct_7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(SADATAParser.FUNCT_7)
            self.state = 184
            self.argument()
            self.state = 185
            self.argument()
            self.state = 186
            self.data_structure_of_interest()
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 187
                    self.argument() 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funct_8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCT_8(self):
            return self.getToken(SADATAParser.FUNCT_8, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(SADATAParser.ArgumentContext,i)


        def data_structure_of_interest(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SADATAParser.Data_structure_of_interestContext)
            else:
                return self.getTypedRuleContext(SADATAParser.Data_structure_of_interestContext,i)


        def getRuleIndex(self):
            return SADATAParser.RULE_funct_8

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunct_8" ):
                listener.enterFunct_8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunct_8" ):
                listener.exitFunct_8(self)




    def funct_8(self):

        localctx = SADATAParser.Funct_8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funct_8)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(SADATAParser.FUNCT_8)
            self.state = 194
            self.argument()
            self.state = 195
            self.argument()
            self.state = 196
            self.argument()
            self.state = 198 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 197
                self.data_structure_of_interest()
                self.state = 200 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20 or _la==21):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_structure_of_interestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_CANDIDATE(self):
            return self.getToken(SADATAParser.ID_CANDIDATE, 0)

        def STRUCT_CANDIDATE(self):
            return self.getToken(SADATAParser.STRUCT_CANDIDATE, 0)

        def getRuleIndex(self):
            return SADATAParser.RULE_data_structure_of_interest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_structure_of_interest" ):
                listener.enterData_structure_of_interest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_structure_of_interest" ):
                listener.exitData_structure_of_interest(self)




    def data_structure_of_interest(self):

        localctx = SADATAParser.Data_structure_of_interestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_data_structure_of_interest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RAW_STATEMENT(self):
            return self.getToken(SADATAParser.RAW_STATEMENT, 0)

        def ID_CANDIDATE(self):
            return self.getToken(SADATAParser.ID_CANDIDATE, 0)

        def STRUCT_CANDIDATE(self):
            return self.getToken(SADATAParser.STRUCT_CANDIDATE, 0)

        def STRING(self):
            return self.getToken(SADATAParser.STRING, 0)

        def getRuleIndex(self):
            return SADATAParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = SADATAParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





