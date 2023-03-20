# Project 2, Algorithm 3:
# Names: Samee Rauf, Victoria Parry
# Email address: srauf@csu.fullerton.edu, vjparry414@csu.fullerton.edu

import re

#opens file
inputfile = open("in2C.txt")

#reads file and places contents into a list
my_list = inputfile.readlines()[2:]

#create empty lists 
Array_0 = []
Array_1 = []
Array_2 = []
Array_3 = []

#removes unnecessary characters from each index and saves it to a new list
for i in my_list:
    i = i.replace("\t","").replace("\n","").replace("=", "").replace("[", "")
    i = i.replace("]","")
    Array_0.append(''.join(x for x in i.split() if not x.startswith('Ar')))



#divides Array_0 into seperate lists 
i = 1
for s in range(len(Array_0)-1):
    if Array_0[s] == '' and Array_0[s+1] == '' and i == 1:
        Array_1 = Array_0[:s]
        i+=1
        j=s
    if Array_0[s] == '' and Array_0[s+1] == '' and i == 2:
        Array_2 = Array_0[j:s]
        Array_3 = Array_0[s:]


#create empty strings 
string_1 = ""
string_2 = ""
string_3 = ""

#converts the list to a string
for k in Array_1:
    string_1 += k

for k in Array_2:
     string_2 += k

for k in Array_3:
     string_3 += k


#converts the string to a list of ints 
temp1 = re.findall('[-]?\d+', string_1)
nums1 = list(map(int, temp1))

temp2 = re.findall('[-]?\d+', string_2)
nums2 = list(map(int, temp2))

temp3 = re.findall('[-]?\d+', string_3)
nums3 = list(map(int, temp3))


#Takes in and sorts the given list
def bubbleSort(arr):
    #gets the length of the list
    n = len(arr)
    #creates a bool for when an item is swapped
    swapped = False
    #for loop to iterate through list
    for i in range(n-1):
        #for loop to swap the smaller numbers 
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        #returns if not swapped
        if not swapped:
            return
 
#sorts lists  
bubbleSort(nums1)
bubbleSort(nums2)
bubbleSort(nums3)

#prints lists
print(nums1)
print(nums2)
print(nums3)