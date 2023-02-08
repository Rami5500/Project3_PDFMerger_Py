import PyPDF2
import sys
#os module is used to work with directorys(folders), e.g; fetching its contents
import os


#creates a merger object
merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        #To test it prints out the correct file
        #print(file)

        merger.append(file)

    merger.write("combined_Files.pdf")
