import sys      # sys.argv
import os       # os.path

"""
Script to print common lines between two text files using set intersection.

Ryan LeBoeuf (rleboeu)

Ex:
-- file1.txt --
hello
344
banana
grape
---------------

-- file2.txt --
grape
lettuce
344
apple
pear
---------------

-- python3 intersect_files.py file1.txt file2.txt --
Common elements between 'file1.txt' and 'file2.txt':
344
grape
----------------------------------------------------

"""

# Add each line in a file to a set and return that set.
def fileToSet(fp: str) -> set:
    s = set()
    with open(fp, 'r') as file:
        for line in file:
            s.add(line.strip('\n'))
    return s

# Run the program
def run(filepath1: str, filepath2: str) -> None:

    set1 = fileToSet(filepath1)
    set2 = fileToSet(filepath2)

    intersect = set1.intersection(set2)

    print(f"Common elements between '{filepath1}' and '{filepath2}':")
    for itm in intersect:
        print(itm)

### Entry Point ###
if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python3 intersect_files.py <file one> <file two>")
    else:
        file_not_found = " does not exist or was not found."
        if not os.path.isfile(sys.argv[1]):
            raise SystemExit(f"'{sys.argv[1]}' {file_not_found}")
        elif not os.path.isfile(sys.argv[2]):
            raise SystemExit(f"'{sys.argv[2]}' {file_not_found}")
        else:
            run(sys.argv[1], sys.argv[2])