# A.J. Imholte
# Algorithm Design and Analysis
# HWB

def IsAnagram(string1, string2):
    if len(string1) == len(string2):
        str1Dict = {}
        str2Dict = {}
        for char in string1:
            if char not in str1Dict:
                str1Dict[char] = 1
            else:
                str1Dict[char] = str1Dict[char] + 1
        for char in string2:
            if char not in str2Dict:
                str2Dict[char] = 1
            else:
                str2Dict[char] = str2Dict[char] + 1
        if str1Dict == str2Dict:
            return True
        else:
            return False
    else:
        return False

print("Let's check to see if two words are anagrams!")

# The combination "exitation" and "intoxicate" is currently failing.
# The combination "cat" and "cow" is currently failing.
# Tested anagrams from http://www2.vo.lu/homepages/phahn/anagrams/oneword.htm

# TODO: test two words of the same length that have letters of different counts that are not anagrams
# print(IsAnagram("fall", "faal"))

# Debugging
# print(IsAnagram("cat", "cow"))
# print(IsAnagram("excitation", "intoxicate"))

# Uncomment the following lines of code to run with user input.

run = True
while run == True:
    input1 = input("What is the first word? ")
    input2 = input("What is the second word? ")
    ans = IsAnagram(input1, input2)
    if ans == True:
        print("Yay! The two words are anagrams!")
    else:
        print("The words are not anagrams. Sad!")
    response = input("Do you want to test another pair of words? ")
    if response == "no":
        run = False







