import sys, os

import test_lab_3

def main(tester, proctor, dynImport):
    '''
    Validates and fixes input, and calls test_main().
    :param tester: Located in ./test; Student script with .py
    :param proctor: Located in ./ ; Professor script with .py
    :param dynImport: Located in ./test; Import test 
    '''

    print(f"Testing '{tester}' against '{proctor}'...")

    validate_file(tester) # Program exits if file is not found
    validate_file(proctor) # Program exits if file is not found

    test_lab_3.test_main(tester, proctor, dynImport)

def validate_file(checkedFile):
    if not os.path.exists(checkedFile): 
        sys.exit(f"{checkedFile} not found.")


if __name__ == "__main__":
    try:
        tester = str(sys.argv[1])
        proctor = str(sys.argv[2])
        if len(sys.argv) > 3:
            dynImport = str(sys.argv[3])
        else: 
            print("Import test omitted!!")
            dynImport = None
    except IndexError:
        sys.exit("""Please provide a file name for testing (student file), a proctor (answer file), and an import file (formula.py) as standard in argument.
Proctor file must be in \\ while testing scripts must be in .\\test""")
    
    if not dynImport == 'formulas' and not dynImport == None:
        input("WARNING: The file that you are trying to import is an incorrect module name. Please check rubric for proper grading. Please press enter to continue...")

    main(tester, proctor, dynImport)