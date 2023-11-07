class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #The only way two strings can have a common divisor is if they are both composed of repeated sequences of that divisor. 
        #This if statement checks that. If not, return "" and we're done.
        if str1 + str2 != str2 + str1:
            return ""
        #If we pass the above test, we can move on to the following code.
        #First, we grab the gcd function from the python math module.
        #This function will not be directly applied to the strings. 
        #Rather, it will be applied to their length (hint: because length is a numerical value that gcd can work with).
        #length of strings is found by len(str1) and len(str2).
        #By doing this (finding the gcd), we will find the length of the answer, if any.
        #Elaborating, this number represents the length of the longest possible series of repeating characters that can be used to build either string.
        #Next, this result of gcd(len(str1), len(str2)) is used to slice str1.
        #Note that the slicing operation is a string operation rather than a numerical/mathmatical one.
        #The slicing operation starts are the beginning of str1 and "collects" characters up to the gcd that we just found.
        #Since we are doing this operation on a series of repeating character sequences, this results in our answer.
        from math import gcd
         return str1[:gcd(len(str1), len(str2))]
