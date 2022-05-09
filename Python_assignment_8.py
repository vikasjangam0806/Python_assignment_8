#Q-1 Python – Least Frequent Character in String

# Python 3 code to demonstrate 
# Least Frequent Character in String
# naive method 
  
# initializing string 
test_str = "GeeksforGeeks"
  
# printing original string
print ("The original string is : " + test_str)
  
# using naive method to get
# Least Frequent Character in String
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = min(all_freq, key = all_freq.get) 
  
# printing result 
print ("The minimum of all characters in GeeksforGeeks is : " + str(res))

#Q-2 Python | Maximum frequency character in String
# Finding most occuring character

# Get string from user
string = input("Enter some text: ")

# Set frequency as empty dictionary
frequency_dict = {}

for character in string:
    if character in frequency_dict:
        frequency_dict[character] += 1
    else:
        frequency_dict[character] = 1

most_occurring = max(frequency_dict, key=frequency_dict.get)

# Displaying result
print("\nMost occuring character is: ","most_occuring")
print("It is repeated %d times" %(frequency_dict[most_occurring]))

#Q-3 Python | Program to check if a string contains any special character

# Python3 program to check if a string
# contains any special character
 
# import required package
import re
 
# Function checks if the string
# contains any special character
def run(string):
 
    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
     
    # Pass the string in search
    # method of regex object.   
    if(regex.search(string) == None):
        print("String is accepted")
         
    else:
        print("String is not accepted.")
     
 
# Driver Code
if __name__ == '__main__' :
     
    # Enter the string
    string = "Geeks$For$Geeks"
     
    # calling run function
    run(string)

    
#Q-4 Generating random strings until a given string is generated

# Python program to generate and match 
# the string from all random strings
# of same length
  
# Importing string, random
# and time modules
import string
import random
import time
  
# all possible characters including 
# lowercase, uppercase and special symbols
possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'
                     
  
# string to be generated
t = "geek"
  
# To take input from user
# t = input(str("Enter your target text: "))
  
attemptThis = ''.join(random.choice(possibleCharacters)
                                for i in range(len(t)))
attemptNext = ''
  
completed = False
iteration = 0
  
# Iterate while completed is false
while completed == False:
    print(attemptThis)
      
    attemptNext = ''
    completed = True
      
    # Fix the index if matches with 
    # the strings to be generated
    for i in range(len(t)):
        if attemptThis[i] != t[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += t[i]
              
    # increment the iteration 
    iteration += 1
    attemptThis = attemptNext
    time.sleep(0.1)
  
# Driver Code
print("Target matched after " +
      str(iteration) + " iterations")

#Q-5 Find words which are greater than given length k
# Python program to find all string
# which are greater than given length k
 
# function find string greater than length k
def string_k(k, str):
     
    # create the empty string
    string = []
     
    # split the string where space is comes
    text = str.split(" ")
     
    # iterate the loop till every substring
    for x in text:
         
        # if length of current sub string
        # is greater than k then
        if len(x) > k:
             
            # append this sub string in
            # string list
            string.append(x)
             
     # return string list
    return string
 
 
# Driver Program    
k = 3
str ="geek for geeks"
print(string_k(k, str))

#Q-6 Python program for removing i-th character from a string

# Python code to demonstrate
# method to remove i'th character
# Naive Method
  
# Initializing String 
test_str = "GeeksForGeeks"
  
# Printing original string 
print ("The original string is : " + test_str)
  
# Removing char at pos 3
# using loop
new_str = ""
  
for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]
  
# Printing string after removal  
print ("The string after removal of i'th character : " + new_str)

#Q-7 Python program to split and join a string

# Python program to split a string and  
# join it using different delimiter
  
def split_string(string):
  
    # Split the string based on space delimiter
    list_string = string.split(' ')
      
    return list_string
  
def join_string(list_string):
  
    # Join the string based on '-' delimiter
    string = '-'.join(list_string)
      
    return string
  
# Driver Function
if __name__ == '__main__':
    string = 'Geeks for Geeks'
      
    # Splitting a string
    list_string = split_string(string)
    print(list_string)
  
     # Join list of strings into one
    new_string = join_string(list_string)
    print(new_string)

#Q-8 Python | Check if a given string is binary string or not
# Python program to check
# if a string is binary or not
 
# function for checking the
# string is accepted or not
def check(string) :
 
    # set function convert string
    # into set of characters .
    p = set(string)
 
    # declare set of '0', '1' .
    s = {'0', '1'}
 
    # check set p is same as set s
    # or set p contains only '0'
    # or set p contains only '1'
    # or not, if any one condition
    # is true then string is accepted
    # otherwise not .
    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else :
        print("No")
 
 
         
# driver code
if __name__ == "__main__" :
 
    string = "101010000111"
 
    # function calling
    check(string)

#Q-9 Python program to find uncommon words from two Strings
# Python3 program to find a list of uncommon words
  
# Function to return all uncommon words
def UncommonWords(A, B):
  
    # count will contain all the word counts
    count = {}
      
    # insert words of string A to hash
    for word in A.split():
        count[word] = count.get(word, 0) + 1
      
    # insert words of string B to hash
    for word in B.split():
        count[word] = count.get(word, 0) + 1
  
    # return required list of words
    return [word for word in count if count[word] == 1]
  
# Driver Code
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
  
# Print required answer
print(UncommonWords(A, B))

#Q-10 Python – Replace duplicate Occurrence in String
# Python3 code to demonstrate working of 
# Replace duplicate Occurrence in String
# Using split() + enumerate() + loop
  
# initializing string
test_str = 'Gfg is best . Gfg also has Classes now. \
                Classes help understand better . '
  
# printing original string
print("The original string is : " + str(test_str))
  
# initializing replace mapping 
repl_dict = {'Gfg' :  'It', 'Classes' : 'They' }
  
# Replace duplicate Occurrence in String
# Using split() + enumerate() + loop
test_list = test_str.split(' ')
res = set()
for idx, ele in enumerate(test_list):
    if ele in repl_dict:
        if ele in res:
            test_list[idx] = repl_dict[ele]
        else:
            res.add(ele)
res = ' '.join(test_list)
  
# printing result 
print("The string after replacing : " + str(res)) 