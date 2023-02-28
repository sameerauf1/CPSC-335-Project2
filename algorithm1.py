def Cities_in_California():
    with open('in2a.txt', 'r') as file:
        # all the lines in the text file
        file_lines = file.readlines()
    # loop through each line in the text file
    for line in file_lines:
        arrays = line.split(' = ')
        print(arrays)

        # print(line)
print("--------------------------------------------------------------------------------------------------------------------------------")

Cities_in_California()
