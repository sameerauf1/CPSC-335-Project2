def Cities_in_California():
    with open('in2a.txt', 'r') as file:
        # all the lines in the text file
        file_lines = file.readlines()
    # loop through each line in the text file
    counter = 0
    for line in file_lines:
        counter += 1
        arrays = line.split(' = ')
        if counter == 3:
            print(arrays[0])
            print(arrays[1])
        print(arrays)
        if counter == 3:
            break

        # print(line)
print("--------------------------------------------------------------------------------------------------------------------------------")

Cities_in_California()
