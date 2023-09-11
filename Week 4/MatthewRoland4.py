import re
import csv

def main():
    inputFile = r"files/input.txt"
    outputcsv = r"output.csv"
    outputtxt = r"files/output.txt"

    # Counting Mailers and Writing to file
    mailCount = email_counter(inputFile)
    csv_writer(mailCount, outputcsv)

    # X-DSPAM-Confidence Stuffs
    confidenceLevels = spam_reader(inputFile)
    txt_writer(confidenceLevels, outputtxt, pretext="X-DSPAM-Confidence: ")
    return

def txt_writer(data, file, pretext=""):
    with open(file, 'w') as f:
        for line in data:
            f.writelines([ pretext+str(line), "\n"])
        f.writelines("-------------------------------------------------\n")
        f.writelines("Total dspam confidence = " + str(format(sum(data), "0.2f")) + "\n")
        f.writelines( "Average dspam confidence = " + str(format(sum(data)/len(data), "0.2f")) +"\n" )
    return

def spam_reader(file):
    with open(file, 'r') as f:
        lines = f.read()

    confidenceLevels = [ float(confidenceLevelString) for confidenceLevelString in re.findall("X-DSPAM-Confidence: (\d.\d\d\d\d)", lines) ]

    return confidenceLevels

def email_counter(file):
    with open(file, 'r') as f:
        emailLines = f.read()
    
    allEmails = re.findall('From: (\S+@\S+)', emailLines)

    
    mailCount = {} 
    for email in allEmails:
        if email in mailCount.keys():
            mailCount[email] += 1
        else:
            mailCount[str(email)] = 1
    return mailCount

def csv_writer(dictData, file):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Email', 'Count'])
        writer.writeheader()

        for address in dictData.keys():
            writer.writerow({"Email":address, "Count":dictData[address]})
        writer.writerow({"Email":"TOTAL", "Count":sum(dictData.values())})
    return

if __name__ == "__main__":
    main()