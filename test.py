def Cities_in_California():
    array1a = []
    array1b = []
    array2a = []
    array2b = []
    array3a = []
    array3b = []

    with open('in2a.txt', 'r') as file:
        # all the lines in the text file
        file_lines = file.readlines()

        for line in file_lines:
            if ' = ' not in line:
                continue
            key, values = line.strip().split(' = ')
            values = [v.strip().strip('"')
                      for v in values.strip('[]\n').split(', ')]

            if key == "array 1a":
                array1a = values
            elif key == "array 1b":
                array1b = values
            elif key == "array 2a":
                array2a = values
            elif key == "array 2b":
                array2b = values
            elif key == "array 3a":
                array3a = values
            elif key == "array 3b":
                array3b = values

    print(array1a)
    long_list = array1a[0]

    print(array1b)


print("--------------------------------------------------------------------------------------------------------------------------------")

Cities_in_California()
