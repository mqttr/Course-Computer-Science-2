import csv
import re
import os.path
import sys

def main():

    # Input File
    while True:
        try: 
            inFile = r"files/" + input("Input file name: ").strip()
            f = open(inFile, "r")
            break
        except:
            print("File Does Not Exist!")

    # Output File
    outFile = get_outfile()
    
    # Reading Input File
    with open(inFile, "r") as f:
        fileString = ''.join(f.read())
    
    mailAddresses = re.findall('From (\S+@\S+)', fileString)
    subjectLines = re.findall('Subject: \[sakai\] svn commit:\s(r\d+)\s', fileString)
    spamConfidence = re.findall('X-DSPAM-Confidence:\s(\d*\.\d+)', fileString)

    if not (len(mailAddresses) == len(subjectLines) == len(spamConfidence)):
        print("Stop now input file does not have the same levels across all measured figures!")
        sys.exit("Input file does not have correct Mail Addresses, Subject Lines, or X-DSPAM Confidence Values.")

    # Writing Output File
    special_csv_writer(mailAddresses, subjectLines, spamConfidence, file=outFile, fieldnames=["Email","Subject","Confidence"])
    
    return

def special_csv_writer(col1, col2, col3, file="", fieldnames=[]):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(len(col1)):
            writer.writerow( {fieldnames[0]:col1[i], fieldnames[1]:col2[i], fieldnames[2]:col3[i] } )


    print("Data Stored!")
    return


def get_outfile():

    file = r"files/" + input("Output file name: ").strip()
    while True: 

        if not (os.path.isfile(file)):
            return file # File does not exist we are chillin'
        else:
            delExistingFile = input("Overwrite existing file (y/n): ").strip().lower()
            while True:
                if delExistingFile == "y":
                    return file
                elif delExistingFile == "n":
                    file = r"files/" + input("New output file name: ").strip()
                    break
                else:
                    delExistingFile = input("Enter (y/n): ").strip().lower()

    return
    

if __name__ == "__main__":
    main()