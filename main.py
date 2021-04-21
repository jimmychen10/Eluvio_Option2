"""
By: Jimmy Chen
Date Of Submition: 4/20/2021

Language: Python 3

Summary:
The program first goes through the testSamples folder and goes through all files inside and stores each line of binary to the files dictionary, 
including its line index location, length of the strand of the binary, and the binary in hexadecimal form. Next the program sorts each strand 
based on its size from smallest to largest. Once that is complete, the program finds the largest strand through each file from the sorted array 
until it finds 2 or more files with the same strand length. If it does, it prints out the length of the strand, what files the strands appear, 
and the index location of the strand. However, if there is no strand from each file that matches with one another, the program will display that 
there were no matches. 
"""

import binascii
import os


files = {} # stores the files and thier info
directory = "testSamples" # folder that consist all binary file

# Insertion sort
def sortLengthBinaryLines(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key[1] < arr[j][1] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# go through the binary file and adds each line of binary to the files dictionary includeing its
# line index location, length of the strand of the binary, and the binary in hexidecimal form
def goThroughFile(file, fileName):
    indexLoc = 0
    fileIfno=[]
    # goes binary file
    for line in file:
        c = line.strip()
        hexForm = str(binascii.hexlify(c))
        strandLength= (len(hexForm)-3)*4
        # adds the location, length of strand, and herform into the program
        fileIfno.append([indexLoc,strandLength,hexForm])
        indexLoc += 1

    #sorts file from smallest length of strand to highest 
    sortLengthBinaryLines(fileIfno)
    # add file name and its info to files dictionary
    files[fileName]= {"fileIfno":fileIfno, "counter": indexLoc -1}


def result():
    highestStrandsFiles = [] # store longest strands files names
    found = False
    while found == False:
        stopCounter = 0
        longest = 0
        for i in files:
            StrandsCounter = files.get(i).get("counter") 
            longetsStrand = files.get(i).get("fileIfno")[StrandsCounter][1]
            longetsStrandIndexLocation =  files.get(i).get("fileIfno")[StrandsCounter][0]

            if StrandsCounter ==0:
                stopCounter +=1

    
            # if find larger strand, reset highestStrandsFiles
            if longetsStrand > longest:
                longest  =longetsStrand
                # empties current longest strands files names
                highestStrandsFiles = [] 
                # add new longest strands files name
                highestStrandsFiles.append(i)
            # Store file names if mathch with longest strand 
            elif longetsStrand == longest:
                highestStrandsFiles.append(i)
        

        # determines if there are two or more files that match
        if len(highestStrandsFiles) > 1:
            tempBinarys = {}

            for i in range (len(highestStrandsFiles)):
                tempBinarys.update({highestStrandsFiles[i] :[]}) 
                # adds all the same length strands into the binary dictionary
                StrandsCounter = files.get(highestStrandsFiles[i]).get("counter") 
                while longest == files.get(highestStrandsFiles[i]).get("fileIfno")[StrandsCounter][1]:

                    strandLoc = files.get(highestStrandsFiles[i]).get("fileIfno")[StrandsCounter][0] # Strand Index Location
                    standSize = files.get(highestStrandsFiles[i]).get("fileIfno")[StrandsCounter][1] # Strand Size
                    hexForm = files.get(highestStrandsFiles[i]).get("fileIfno")[StrandsCounter][2]   # Hexidecimal

                    tempBinarys.get(highestStrandsFiles[i]).append([strandLoc, standSize, hexForm])

                    if files.get(highestStrandsFiles[i]).get("counter") -1 > -1:
                        files[highestStrandsFiles[i]]["counter" ] =files.get(highestStrandsFiles[i]).get("counter") -1
                        StrandsCounter = files.get(highestStrandsFiles[i]).get("counter") 
                    else:
                        break
            found = True  

            # Displays disired info
            print( "Longest Strand Length:", longest)
            print( "Longest Strand Length files:",end =" ")
            for file in tempBinarys:
                print(file, end=" ")
            print()

            print( "Offsets: ")
            for file in tempBinarys:
                print("FILE:",file) #name of file
                for i in range(len(tempBinarys.get(file))):
                    
                    print("     Strand Index Location:",tempBinarys.get(file)[i][0])
                    for file2 in tempBinarys:
                        if file != file2:
                            print("\t Offset with file "+ file2+":", end=" ")
                            for j in range(len(tempBinarys.get(file2))):
                                print(abs(tempBinarys.get(file)[i][0] - tempBinarys.get(file2)[j][0]), end =" ")
                            print()
    
        else:
            # changes the counter of the file by -1
            # Checks to see if all th files have reached torwards the first index line and if so and there were no matching strands, 

            if len(highestStrandsFiles) == stopCounter:
                print("there are no matching strands through the files")
                break
            else:
                for i in range(len(highestStrandsFiles)):
                    if files.get(highestStrandsFiles[i]).get("counter")>-1:
                        files[highestStrandsFiles[i]]["counter" ] =files.get(highestStrandsFiles[i]).get("counter") -1

    
for fileName in os.listdir(directory):
    goThroughFile(open( os.path.join(directory, fileName), "rb"), fileName)

result()


