# SmartAssembly (.TAB) Program - Language Parsing Project

## History 

The goal of this project was an exercise in understanding the structure of the proprietary language Smartassembly (*.tab), as well as some getting some feel for [ANTLR4](https://www.antlr.org/).

Given the nature of the business model of this automation language:
- no formal language specification is available
- no CST or AST are provided to users
- no existing independent compiler/translators that can be used in pair with the debugger of an IDE to debug the language easily at runtime / support major refactorings / etc.
  
I was interested in making some first steps in an "independent" tool for static analysis of the language to support the following steps / developer tools - 
- formatting
- static analysis 
- refactoring

This project currently contains a functioning, if incomplete, grammar for .TAB files and can extra all of the data structure names from the logic portion of the programs (ASM_DESCR block).

For ambitious developers, I hope this might help in making further steps in developer tools for the language. 


## Installing Dependencies
``
pip install -r requirements.txt
``


## Want To Use As Is? 


- Use as a CLI - from CMD or from a SmartAssembly program to parse and extract data structure names from .TAB files.

	Example Usage:

	``
	python.exe -m extractor "examples\\test1.tab" "out\\test1.tab" 
	``


## Want To Build Your Own Program For .Tab Files?

### Want To Further Develop The Grammar? 

- Modify grammar file:  \parser_generator\SADATA.g4  - see [antlr.org](https://www.antlr.org/) for more details.

### Want To Generate New Parser From Grammar?  

- Execute \parser_generator\generate_parser.py

### Want To Do Something More Interesting With .Tab Parsing? 

1. Generate a new parser (per above statement).

2. Move the generated files from /generated_parser to /manually_modified_parser for modification.

3. Modify stubs in the /manually_modified_parser to do what you want to accomplish. I certainly can recommend Terrence Parr's Book - [The Definitive ANTLR 4 Reference](https://pragprog.com/titles/tpantlr2/the-definitive-antlr-4-reference/)


