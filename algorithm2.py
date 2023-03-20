# Project 1, Algorithm 2:
# Names: Samee Rauf, Victoria Parry
# CSUF-supplied email address: srauf@csu.fullerton.edu, vjparry414@csu.fullerton.edu

# Test cases for algorithm:
input_1 = "ddd"
input_2 = "heloooooooo there"
input_3 = "choosemeeky and tuition-free"


def string_compress(input_string):
    final_string = ""
    consecutive_counter = 0
    # going to loop through each letter in the string
    for i in range(len(input_string)):
        # edge case1 last letter in entire string
        if i == len(input_string)-1:
            # edgcase1a: if last letter in entire string ,is last letter in run then increment consecutive counter
            if consecutive_counter >= 1 and input_string[i] == input_string[i-1]:
                final_string = final_string + str(consecutive_counter + 1)
                final_string = final_string + input_string[i]
            # edcase1b: if last letter in entire string, nonconsecutive letter, just add character to final string
            elif consecutive_counter == 0:
                final_string = final_string + input_string[i]
        # if next character is the same as current character, increment consecutive counter & go to next iteration
        elif input_string[i] == input_string[i+1]:
            consecutive_counter += 1
            continue
        # if curr character is not the same as the next character
        else:
            # if curr character is last consecutive character in the run, increment consecutive counter
            if (input_string[i] != input_string[i+1] and input_string[i] == input_string[i-1]):
                consecutive_counter += 1
            # if the consecutive counter >1 add it to the final string
            if consecutive_counter > 1:
                final_string = final_string + str(consecutive_counter)
            # reset the consecutive character count to 0 , now that we have processed last character in run
            consecutive_counter = 0
            # if the consecutive character is 0 then only add letter to the final string
            final_string = final_string + \
                input_string[i]
    return final_string


print(string_compress(input_2))
