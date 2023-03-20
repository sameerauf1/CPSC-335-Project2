import re

inputfile = open("in2C.txt")


my_list = inputfile.readlines()[2:]

Array_0 = []
Array_1 = []
Array_2 = []
Array_3 = []

for i in my_list:
    i = i.replace("\t","").replace("\n","").replace("=", "").replace("[", "")
    i = i.replace("]","")
    Array_0.append(''.join(x for x in i.split() if not x.startswith('Ar')))


i = 1
for s in range(len(Array_0)-1):
    if Array_0[s] == '' and Array_0[s+1] == '' and i == 1:
        Array_1 = Array_0[:s]
        i+=1
        j=s
    if Array_0[s] == '' and Array_0[s+1] == '' and i == 2:
        Array_2 = Array_0[j:s]
        Array_3 = Array_0[s:]


string_1 = ""
string_2 = ""
string_3 = ""

for k in Array_1:
    string_1 += k

for k in Array_2:
     string_2 += k

for k in Array_3:
     string_3 += k



temp1 = re.findall('[-]?\d+', string_1)
nums1 = list(map(int, temp1))

temp2 = re.findall('[-]?\d+', string_2)
nums2 = list(map(int, temp2))

temp3 = re.findall('[-]?\d+', string_3)
nums3 = list(map(int, temp3))

#print(nums1)
#print(nums2)
#print(nums3)

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
 
bubbleSort(nums1)
bubbleSort(nums2)
bubbleSort(nums3)

print(nums1)
print(nums2)
print(nums3)