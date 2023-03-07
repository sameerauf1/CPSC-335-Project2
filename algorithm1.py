def Cities_in_California():
    # intializing list for array, 6 arrays for 3 test cases
    array1a = []
    array1b = []
    array2a = []
    array2b = []
    array3a = []
    array3b = []

    # creating dictionary to eventually store city from array b,  with the index it was found in array a
    mydict = {}  # city: index
    mydict2 = {}
    mydict3 = {}

    # load text with reader permission
    with open('in2a.txt', 'r') as file:

        # all the lines in the text file
        file_lines = file.readlines()

        # loop throu every line in the text file
        for line in file_lines:

            # skip line if there is no "=", means we are not looking at an array
            if ' = ' not in line:
                continue

            # we will split line into key: will be array name and values:  list of values
            key, values = line.strip().split(' = ')

            # get rid of [] and newline and sperate cities with a comma for each city & ultimatley creating a list of strings

            # if there are single quotes, we are keeping them so that b arrays values are not messed up
            values = [v.strip()
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

        # we want to look at a string, not a list of strings
        array1a = array1a[0]
        array2a = array2a[0]
        array3a = array3a[0]
        # test case 1:----------------------------------------------------------------
        # we looping through seperated cities in b arrays
        for city in array1b:

            # we will look only at the city, not the singlge quote ex. 'Brea' --> Brea
            clean_city = city[1:len(city)-1]

            # we will grab the length of the city to use as sliding window when looping through concatenated cities in a arrays
            size_looking_for = len(clean_city)

            # we will loop through a arrays, checking if sliding window from arrayb matches array a, skip first character which is: "
            for index in range(1, len(array1a)):
                # slicing the array from index to size_looking_for(Window)
                if clean_city == array1a[index: index + size_looking_for]:

                    #need to account for characters skipped 
                    mydict[clean_city] = index-1

        # sort dictionary, by looking at the key & returning the corresponding value for each pair to the sorted function
        sorted_dict = dict(sorted(mydict.items(), key=lambda x: x[1]))

        # create new list with city indexes in which they were listed
        Output_order = [sorted_dict[key] for key in sorted_dict.keys()]

        # create new  list with city names in order of index in which it appeared
        Output_array = [key for key in sorted_dict.keys()]
        # print(Output_order)
        # print(Output_array)
        # ----------------------------------------------------------------------------------------------------------------------------------------
        # test case 2 (Same Code & logic, but using array 2a and 2b and mydict2):----------------------------------------------------------------
        # we looping through seperated cities in b arrays
        for city in array2b:

            # we will look only at the city, not the singlge quote ex. 'Brea' --> Brea
            clean_city = city[1:len(city)-1]

            # we will grab the length of the city to use as sliding window when looping through concatenated cities in a arrays
            size_looking_for = len(clean_city)

            # we will loop through a arrays, checking if sliding window from arrayb matches array a
            for index in range(1, len(array2a)):
                # slicing the array from index to size_looking_for(Window)
                if clean_city == array2a[index: index + size_looking_for]:
                    mydict2[clean_city] = index-2
        # sort dictionary, by looking at the key & returning the corresponding value for each pair to the sorted function
        sorted_dict2 = dict(sorted(mydict2.items(), key=lambda x: x[1]))
        # print(sorted_dict)
        Output_order2 = [sorted_dict2[key] for key in sorted_dict2.keys()]
        Output_array2 = [key for key in sorted_dict2.keys()]
        # print(Output_order)
        # print(Output_array)

        # test case 3:----------------------------------------------------------------
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
        sorted_dict3 = dict(sorted(mydict3.items(), key=lambda x: x[1]))

        Output_order3 = [sorted_dict3[key] for key in sorted_dict3.keys()]
        Output_array3 = [key for key in sorted_dict3.keys()]
        # print(Output_order3)
        # print(Output_array3)
        return (Output_order, Output_array, Output_order2, Output_array2, Output_order3, Output_array3)


# print("--------------------------------------------------------------------------------------------------------------------------------")
print(Cities_in_California())
