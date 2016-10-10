import argparse
import os
import sys

def extractDataFromFile(header_file, data_file):
    with open(header_file) as file:
        headers = file.read().splitlines()

    with open(data_file) as file:
        data_file_lines = file.read().splitlines()

    outputData = list()
    for header in headers:
        for i in range(0, len(data_file_lines)):
            currentLine = data_file_lines[i]
            if header == currentLine:
                outputData.append(currentLine)
                outputData.append(data_file_lines[i + 1])
                i += 1

    return outputData

def getFileNamesFromDirectory(directory):
    files = list()
    for fileName in os.listdir(directory):
        files.append(fileName)

    return files

def writeDataToFile(fileData, fileName):
    outputFile = open(fileName, 'w+')
    for data in fileData:
        outputFile.write(data + "\n")

    print('Created file ' + fileName + '.')

def handleCreateDirectoryDecision(directoryToMake):
    print('That directory doesn\'t seem to exist..')

    createDirectoryInput = ''
    while createDirectoryInput is not 'y' and createDirectoryInput is not 'n':
        createDirectoryInput = input('Would you like to create it? (y/n) ')

    if createDirectoryInput is 'y':
        os.makedirs(directoryToMake)
        return

    sys.exit()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('header_directory', help = 'The directory to get the header data from.')
    parser.add_argument('data_directory', help = 'The directory to extract the data files from.')
    parser.add_argument('output_files_name', help = 'The common name for the output files.')
    parser.add_argument('output_directory', help = 'The output directory.')

    arguments = parser.parse_args()

    if not os.path.exists(arguments.output_directory):
        handleCreateDirectoryDecision(arguments.output_directory)

    headerFiles = getFileNamesFromDirectory(arguments.header_directory)
    dataFiles = getFileNamesFromDirectory(arguments.data_directory)

    outputDataList = list()
    for i in range(0, len(headerFiles)):
        headerFile = os.path.join(arguments.header_directory, headerFiles[i])
        dataFile = os.path.join(arguments.data_directory, dataFiles[i])
        data = extractDataFromFile(headerFile, dataFile)
        outputDataList.append(data)

    for i, outputData in enumerate(outputDataList):
        outputFileName = arguments.output_files_name + str(i) + '.conf'
        outputFile = os.path.join(arguments.output_directory, outputFileName)
        writeDataToFile(outputData, outputFile)

    print('Done!')

main()
