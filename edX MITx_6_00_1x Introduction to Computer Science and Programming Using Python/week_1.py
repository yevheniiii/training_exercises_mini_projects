""" PROBLEM 1

Assume "s" is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string "s". Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5"""

# First way

s = 'azcbobobegghakl'

total = 0
for vowel in s:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        total = total + 1
print("Number of vowels: " + str(total))

# Second way

s = "rpnefeiwcxlhuuealr"
vowels = ["a", "o", "e", "u", "i"]
counter = 0

for letter in s:
    if letter in vowels:
        counter += 1

print("Number of vowels:" + str(counter))

#####################################################################################################

"""PROBLEM 2

Assume "s" is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program 
should print

Number of times bob occurs is: 2"""

s = 'azcbobobegghakl'
sb = 'bob'
sub_len = len(sb)
counter = 0
for i in range(len(s)):
    if s[i: i + sub_len] == sb:
        counter += 1
print("Number of times is: " + str(counter))

#####################################################################################################

"""PROBLEM 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc"""

s = 'azcbobobegghakl'
longest = ""
max = ""

for i in range(len(s) - 1):
    if(s[i] <= s[i + 1]):
        longest = longest + s[i]
        if(i == len(s) - 2):
            longest = longest + s[i + 1]
    else:
        longest = longest + s[i]
        if(len(longest) > len(max)):
            max = longest
        longest = ""

if(len(s) == 1):
    longest = s


if(len(longest) > len(max)):
    print("Longest substring in alphabetical order is: " + longest)
else:
    print("Longest substring in alphabetical order is: " + max)
