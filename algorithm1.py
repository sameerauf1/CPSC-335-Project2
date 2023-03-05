def Cities_in_California():
    array1a = []
    array1b = []
    array2a = []
    array2b = []
    array3a = []
    array3b = []
    mydict = {}  # city: index
    with open('in2a.txt', 'r') as file:
        # all the lines in the text file
        file_lines = file.readlines()

        for line in file_lines:
            if ' = ' not in line:
                continue
            # key will be array1, values will list of values
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

    array1a = array1a[0]
    array2a = array2a[0]
    array3a = array3a[0]
    print("array1a: ", array1a.strip(' "'))
    print("array1b", array1b)
    print()
    # for i in array1b:
    #    for j in range(len(i)):
    #      print(i[j])
    for city in array1b:
        lenghtOF = len(city)
        clean_city = city[1:len(city)-1]
        print("the lenght of clean city is",
              clean_city, "is ", len(clean_city))
        size_looking_for = len(clean_city)
        for index in range(1, len(array1a)):
            # print(" we are printing here",
            #      array1a[index: index + size_looking_for], "and the clean city is", clean_city)
            if clean_city == array1a[index: index + size_looking_for]:
                print(" **************at index we have a match:",
                      index - 2, ":", clean_city)
                mydict[clean_city] = index-2
            if index == 90:
                exit()
        if clean_city in array1b:
            print(clean_city, "is in array1b")
        # if array2a[city] in array1a:
        # print("true")
    sorted_dict = dict(sorted(mydict.items(), key=lambda x: x[1]))
    print(sorted_dict)
    Output_order = [sorted_dict[key] for key in sorted_dict.keys()]
    Output_array = [key for key in sorted_dict.keys()]
    #print(Output_order)
    #print(Output_array)
    return (Output_order, Output_array)


print("--------------------------------------------------------------------------------------------------------------------------------")

print(Cities_in_California())
