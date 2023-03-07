# ddd" becomes "3d"
# • "heloooooooo there" becomes "hel8o there"  ** NOTE SPACES
# • "choosemeeky and tuition-free" becomes "ch2osem2eky and tuition-fr2e"
input_1 = "ddd"
input_2 = "heloooooooo there"
input_3 = "choosemeeky and tuition-free"
#input_2 = "h e l o o o o o o o o   there"
#           0 1 2 3 4 5 6 7 8 9 10
# initialize next = next +1, if next > len(input_string, then next % input_string


def string_compress(input_string):
    print(len(input_string)-1)
    my_dict = dict()
    final_string = ""
    consecutive_counter = 0
    o_counter = 0
    for i in range(len(input_string)):
        if i != len(input_string-1)
        if input_string[i] == input_string[i+1]:  # if next letter is the same EX. ooa
            consecutive_counter += 1
        elif input_string[i] != input_string[i+1]:
            if consecutive_counter == 1:
                final_string += input_string[i]
            elif consecutive_counter > 1:
                final_string += str(consecutive_counter) + input_string[i]
            consecutive_counter = 0  # reset consecutive counter to 0

    print("this is the final_String: ", final_string)


string_compress(input_2)
