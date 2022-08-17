import requests
import argparse
import csv
import shutil
import warnings

parser = argparse.ArgumentParser(description='Request HTTP response codes for a list of domains.')
parser.add_argument('-i', '--input', required=True, help='The file for the program to use')
parser.add_argument('-o', '--output', required=True, help='The destination of the output file')
parser.add_argument('-nv', '--noverify', action='store_true', help='Toggle to disable SSL verification')
args = parser.parse_args()

# Create a copy of the input file at the output location.
shutil.copyfile(args.input, args.output)

# Create CSV reader and writer objects.
domainList = open(args.input)
domainReader = csv.reader(domainList)

domainListWrite = open(args.output, 'w', newline='')
outputWriter = csv.writer(domainListWrite)

# Set whether SSL verification should happen.
if args.noverify == True:
    verifarg = False
    warnings.filterwarnings('ignore', 'Unverified HTTPS request')
    print("Running with certificate verification disabled.")
else:
    verifarg = True

# Meat and potatoes. Iterate over each domain, make the request, and write the status code.
for row in domainReader:
    try:
        x = requests.get(str(row[0]), verify=verifarg)
    except requests.exceptions.SSLError:
        x = requests.get(str(row[0]), verify=False)
        outputWriter.writerow([row[0], str(x.status_code) + ", SSL certificate error. Perhaps run with -nv argument?"])
    except:
        outputWriter.writerow([row[0], "Unreachable"])
    else:
        outputWriter.writerow([row[0], str(x.status_code)])

print("Done.")
domainList.close()
domainListWrite.close()
