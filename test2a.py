# ddd" becomes "3d"
# • "heloooooooo there" becomes "hel8o there"  ** NOTE SPACES
# • "choosemeeky and tuition-free" becomes "ch2osem2eky and tuition-fr2e"
input_1 = "ddd"
#input_1 = "d d d"
#          0 1 2
input_2 = "heloooooooo there"
input_3 = "choosemeeky and tuition-free"
#                                     26 27
# input_3 = "c h o o s e m e e k y
#           0 1 2 3 4 5 6 7 8 9 10 11
#           a  n  d tuition-free"
#           11 12 13 14

#input_2 = "h e l o o o o o o o o   there"
#           0 1 2 3 4 5 6 7 8 9 10
# how do we recognize that we have stopped a continous streak
# if input_string[i] != input_string[i+1] and input_string[i] == input_string[i+1]
# we increment the consecutive counter, everytime the next letter is the same- thats not correc tho, we need to look at the previous letter -to determine if curr is


def string_compress(input_string):
    print("----------------------------------------------------------------")
    print(input_string, len(input_string))
    final_string = ""
    consecutive_counter = 0
    o_counter = 0
    for i in range(len(input_string)):
        # if i == 3:
        #print('we are looking at first o')
        # if i == 10:
        #print('we are looking at last o')
        # if input_string[i] == 'o':
        #  print('we are lookint at o')
        #   o_counter += 1
        #print("o_counter", o_counter)
        # if we are the last character in the list- don't look out of bounds for next charcter
        if i == len(input_string)-1:  # edge case
            print('we are at the laster iteration.... line 51',
                  "consecutive count ", consecutive_counter)
            print("WE ARE AT THE LAST LETTER in the string",
                  input_string[i], "on iteration ", i)
            if consecutive_counter >= 1 and input_string[i] == input_string[i-1]:
                print('we are hitting the if in the edge case')
                print("*-_____we are on the last letter,", input_string[i],  "  of the consective run",
                      consecutive_counter, "at index", i)
                final_string = final_string + str(consecutive_counter + 1)
                final_string = final_string + input_string[i]
            elif consecutive_counter > 1:
                print('we are hitting the elif in the edge case')
                final_string = final_string + str(consecutive_counter)
                final_string = final_string + input_string[i]
            elif consecutive_counter == 0:
                final_string = final_string + input_string[i]
            continue
        elif input_string[i] == input_string[i+1]:  # if this
            print('we will see  Character:', input_string[i], ' again in the future!! ',
                  " we are on iteration i ", i, "its consective count will be", consecutive_counter + 1)
            consecutive_counter += 1
            continue
        # input_string[i] != input_string[i+1] and input_string[i] == input_string[i-1]
        else:
            if (input_string[i] != input_string[i+1] and input_string[i] == input_string[i-1]):
                consecutive_counter += 1
                # print("****we are on the last letter,", input_string[i],  "  of the consective run",
                #      consecutive_counter, "at index", i)
            if i == 10 and input_string[i] == 'o':
                print('we are hitting the last o on iteration ', i)
            if consecutive_counter > 1:
                final_string = final_string + str(consecutive_counter)
            consecutive_counter = 0
            final_string = final_string + \
                input_string[i]
    print("this is the final_String: ", final_string)


string_compress(input_1)
#ddd" becomes "3d"
# • "heloooooooo there" becomes "hel8o there"  ** NOTE SPACES
# • "choosemeeky and tuition-free" becomes "ch2osem2eky and tuition-fr2e"