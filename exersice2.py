from pathlib import Path
from random import randint
import requests

currFile = Path(__file__)
parentFolder  = currFile.parents[0];
txtFile = Path(str(parentFolder.absolute()) + '/assets/lorem.txt')

# Write a Python program to count the number of lines in a text file.
###############
with txtFile.open() as myFile:
    linesCount = len(myFile.readlines())

print("Number of lines in file:\n" + str(linesCount))

# Write a Python program to read a random line from a file.
###############
randLine = randint(0, linesCount - 1)
with txtFile.open() as myFile:
    print("Rand line:\n" + myFile.readlines()[randLine])

# Write a Python program to append text to a file and display the text
###############
url = "https://baconipsum.com/api/?type=meat-and-filler&sentences=2&format=text"
response = requests.post(url, verify="/usr/share/ca-certificates/custom/netspark.crt")
newText = response.text

with txtFile.open('a+') as myFile:
    myFile.write(newText + "\n")
    myFile.seek(0)
    print(myFile.readlines())

# Write a Python program to read last n lines of a file, and copy it to new file
###############
readLast = linesCount - randLine

with txtFile.open() as myFile:
    with Path(str(parentFolder.absolute()) + '/assets/newFile.txt').open('a') as newFile:
        for i, line in enumerate(myFile):

            if readLast <= i:
                newFile.write(line)

# Choose file extension for example pdf ,doc etc. Calculate size of all files on your machine or in specific directory from that type
###############
txtFiles = list(Path(str(parentFolder.absolute()) + '/assets').glob('**/*.txt'))
size = 0
for myTxtFile in txtFiles:
    print("size for {0} is {1}".format(myTxtFile.name, myTxtFile.stat().st_size))
    size += myTxtFile.stat().st_size

print("All files size is " + str(size))
