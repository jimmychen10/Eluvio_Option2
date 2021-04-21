# Eluvio_Option2

## By: Jimmy Chen
## Date Of Submition: 4/20/2021

## Language: Python 3

## Summary:
###   The program first goes through the testSamples folder and goes through all files inside and stores each line of binary to the files dictionary, including its line index location, length of the strand of the binary, and the binary in hexadecimal form. Next the program sorts each strand based on its size from smallest to largest. Once that is complete, the program finds the largest strand through each file from the sorted array until it finds 2 or more files with the same strand length. If it does, it prints out the length of the strand, what files the strands appear, and the index location of the strand. However, if there is no strand from each file that matches with one another, the program will display that there were no matches. 