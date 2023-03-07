# ddd" becomes "3d"
# • "heloooooooo there" becomes "hel8o there"  ** NOTE SPACES
# • "choosemeeky and tuition-free" becomes "ch2osem2eky and tuition-fr2e"
input_1 = "ddd"
input_2 = "heloooooooo there"
input_3 = "choosemeeky and tuition-free"


def string_compress(input_string):
    final_string = ""
    print("this is the final_Strin", final_string)
    mydict = dict()  # letter: frequency
    for element in input_string:
        if element not in mydict:
            mydict[element] = 1
            print(
                f'adding {element} to my dict with a frequency of {mydict[element]}')
        else:
            mydict[element] += 1
            print(
                f'incrementing {element} to a frequency of {mydict[element]}')
    unique_chars = dict()
    for letter in input_string:
        if letter not in unique_chars:
            unique_chars[letter] = 1
            print('we are adding {letter} to final_string: {final_string}')
            final_string = final_string + letter
            final_string = final_string + str(mydict[letter])
        elif unique_chars[letter] >= 1:
            continue
        else:
            unique_chars[letter] += 1

    print("this is the final_string", final_string)


string_compress(input_2)
