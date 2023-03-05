def Cities_in_California():
    # intializing list for array
    array1a = []
    array1b = []
    array2a = []
    array2b = []
    array3a = []
    array3b = []
    # creating dictionary to eventually store city from array b with the index it was found in array a
    mydict = {}  # city: index
    mydict2 = {}
    mydict3 = {}

    with open('in2a.txt', 'r') as file:
        # all the lines in the text file
        file_lines = file.readlines()

        for line in file_lines:
            # skip if we are not looking at line with an array
            if ' = ' not in line:
                continue
            # key will be array1, values will list of values
            key, values = line.strip().split(' = ')
            # get rid of "", [] and
            values = [v.strip().strip('"')
                      for v in values.strip('[]\n').split(', ')]
            # allocate content to list container
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
        # need to reset array t
        array1a = array1a[0]
        array2a = array2a[0]
        array3a = array3a[0]
        #print("array1a: ", array1a)
        #print("array1b", array1b)
        print()
        for city in array1b:
            lenghtOF = len(city)
            clean_city = city[1:len(city)-1]
        # print("the lenght of clean city is",
        #       clean_city, "is ", len(clean_city))
            size_looking_for = len(clean_city)
            for index in range(1, len(array1a)):
                # print(" we are printing here",
                #      array1a[index: index + size_looking_for], "and the clean city is", clean_city)
                if clean_city == array1a[index: index + size_looking_for]:
                    #  print(" **************at index we have a match:",
                    #       index - 2, ":", clean_city)
                    mydict[clean_city] = index-2
        for city in array2b:
            lenghtOF = len(city)
            clean_city = city[1:len(city)-1]
        # print("the lenght of clean city is",
        #       clean_city, "is ", len(clean_city))
            size_looking_for = len(clean_city)
            for index in range(1, len(array2a)):
                # print(" we are printing here",
                #      array1a[index: index + size_looking_for], "and the clean city is", clean_city)
                if clean_city == array2a[index: index + size_looking_for]:
                    #  print(" **************at index we have a match:",
                    #       index - 2, ":", clean_city)
                    mydict2[clean_city] = index-2

        for city in array3b:
            lenghtOF = len(city)
            clean_city = city[1:len(city)-1]
        # print("the lenght of clean city is",
        #       clean_city, "is ", len(clean_city))
            size_looking_for = len(clean_city)
            for index in range(1, len(array3a)):
                # print(" we are printing here",
                #      array1a[index: index + size_looking_for], "and the clean city is", clean_city)
                if clean_city == array3a[index: index + size_looking_for]:
                    #  print(" **************at index we have a match:",
                    #       index - 2, ":", clean_city)
                    mydict3[clean_city] = index-2
        sorted_dict = dict(sorted(mydict.items(), key=lambda x: x[1]))
        # print(sorted_dict)
        Output_order = [sorted_dict[key] for key in sorted_dict.keys()]
        Output_array = [key for key in sorted_dict.keys()]
        # print(Output_order)
        # print(Output_array)

        sorted_dict2 = dict(sorted(mydict2.items(), key=lambda x: x[1]))
        # print(sorted_dict)
        Output_order2 = [sorted_dict2[key] for key in sorted_dict2.keys()]
        Output_array2 = [key for key in sorted_dict2.keys()]
        # print(Output_order2)
        # print(Output_array2)

        sorted_dict3 = dict(sorted(mydict3.items(), key=lambda x: x[1]))
        # print(sorted_dict)
        Output_order3 = [sorted_dict3[key] for key in sorted_dict3.keys()]
        Output_array3 = [key for key in sorted_dict3.keys()]
        # print(Output_order3)
        # print(Output_array3)
        return (Output_order, Output_array, Output_order2, Output_array2, Output_order3, Output_array3)


# print("--------------------------------------------------------------------------------------------------------------------------------")
print(Cities_in_California())
