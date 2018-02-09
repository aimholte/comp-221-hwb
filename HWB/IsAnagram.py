# A.J. Imholte
# Algorithm Design and Analysis
# HWB

import math

"""
A simple function to determine if two words are anagrams of each other.
"""
def IsAnagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower() # convert both strings to lowercase so that uppercase characters don't affect whether it evaluates true or false
    if len(string1) == len(string2):
        str1Dict = {}
        str2Dict = {} # create two dictionaries to store the counts of how many times specific characters happen
        for char in string1:
            if char not in str1Dict:
                str1Dict[char] = 1 # if the character is not in the dictionary, add it to the dictionary and increment its count to one
            else:
                str1Dict[char] = str1Dict[char] + 1 # if the dictionary already contains the character, increment the count.
        for char in string2: # do the same thing for the second string.
            if char not in str2Dict:
                str2Dict[char] = 1
            else:
                str2Dict[char] = str2Dict[char] + 1
        if str1Dict == str2Dict:
            return True # return true if the two dictionaries contain the same key-value pairs
        else:
            return False # otherwise return false
    else:
        return False # returns false right away if the two strings are not the same length


# Tested anagrams from http://www2.vo.lu/homepages/phahn/anagrams/oneword.htm

# Testing

print(IsAnagram("fall", "faal")) # expected output: false
print(IsAnagram("cat", "cow")) # expected output: false
print(IsAnagram("excitation", "intoxicate")) # expected output: true
print(IsAnagram("1101", "1110")) # expected output: true
print(IsAnagram("Here are some words: " + str(math.pi), "Here is pi: " + str(math.pi))) # expected output: false
print(IsAnagram("catalogue", "coagulate")) # expected output: true
print(IsAnagram("decimate", "medicate")) # expected output: true
print(IsAnagram("excitation", "intoxicate")) # expected output: true
print(IsAnagram("canoe", "ocean")) # expected output: true
print(IsAnagram("englander", "greenland")) # expected output: true
print(IsAnagram("sweat", "waste")) # expected output: true
print(IsAnagram("inapt", "paint")) # expected output: true
print(IsAnagram("observe", "verbose")) # expected output: true
print(IsAnagram("below", "elbow")) # expected output: true
print(IsAnagram("derision", "ironside")) # expected output: true
print(IsAnagram("domino", "monoid")) # expected output: true
print(IsAnagram("dusty", "study")) # expected output: true
print(IsAnagram("bedroom", "boredom")) # expected output: true
print(IsAnagram("meteor", "remote")) # expected output: true
print(IsAnagram("catalogue".capitalize(), "coagulate".capitalize())) # expected output: true
print(IsAnagram("decimate".capitalize(), "medicate")) # expected output: true
print(IsAnagram("excitaTion", "Intoxicate")) # expected output: true
print(IsAnagram("CanOE", "ocean")) # expected output: true
print(IsAnagram("eEnglanderR", "greenland")) # expected output: false
print(IsAnagram("sweaty", "waste")) # expected output: false
print(IsAnagram("Is this an anagram?", "Is this an anagram?")) # expected output: true...doesn't really match an anagram...
print(IsAnagram("Canoe", "Oacen")) # this probably should be false but returns true because they both have the same count of letters.

# Uncomment the following lines of code to run with user input.
# print("Let's check to see if two words are anagrams!")

# run = True
# while run == True:
#     input1 = input("What is the first word? ")
#     input2 = input("What is the second word? ")
#     ans = IsAnagram(input1, input2)
#     if ans == True:
#         print("Yay! The two words are anagrams!")
#     else:
#         print("The words are not anagrams. Sad!")
#     response = input("Do you want to test another pair of words? ")
#     if response == "no":
#         run = False







