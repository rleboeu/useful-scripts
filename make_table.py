#!/usr/bin/env python

"""
make_table.py -- Convert a .tsv or .csv file into an HTML table (with human readable source)
Ryan LeBoeuf (05-10-2022)
"""

import sys
import os

USAGE = f"\nUsage: {sys.argv[0]} input output\n"
USAGE += "\ninput............the name of the file to be converted to an HTML table (supported filetypes are .tsv and .csv)"
USAGE += "\noutput...........the name of the file that will store the converted input file as an HTML table\n"

def create_table(args: list) -> None:
    if ".tsv" in args[0]:
        separator = "\t"
    else:
        separator = ","
    
    input_file = args[0]
    output_file = args[1]
    
    fp = open(input_file, "r")
    split_lines = []
    
    # split lines into individual tokens
    for line in fp:
        if line[len(line)-1] == "\n":
            line = line[:len(line)-1]   # delete \n
        line = line.split(separator)
        split_lines.append(line)

    # style
    output = "<style>\n"
    output += "  tr, td, th {\n"
    output += "    border: 1px solid black;\n"
    output += "  }\n"
    output += "</style>\n"

    output += "<table>\n"

    # headers
    output += "  <tr>"
    for header in split_lines[0]:
        output += f"\n    <th>{header}</th>"
    output += "\n  </tr>\n"
    
    # table entries (ignore headers)
    for split_line in split_lines[1:]:
        output += "  <tr>"
        for x in split_line:
            output += f"\n    <td>{x}</td>"
        output += "\n  </tr>\n"
    output += "</table>"

    # write output
    with open(output_file, "w") as outfile:
        outfile.write(output)
    
# validate arguments
def validate(args: list) -> None:
    if not os.path.exists(args[0]):
        raise SystemExit(f"'{args[0]}' does not exist.")
    else:
        create_table(args)

## main program
def main() -> None:
    args = sys.argv[1:]
    if not args or len(args) < 2:
        raise SystemExit(USAGE)
    
    if args[0] == "--help":
        print(USAGE)
    else:
        validate(args)
    
if __name__ == "__main__":
    main()