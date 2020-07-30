	# @author Aakash.Verma
	# Problem: Given a string, find the length of the longest substring which has no repeating characters.
	
	# Example 1:
	# Input: String="aabccbb"
	# Output: 3
	# Explanation: The longest substring without any repeating characters is "abc".	
	
	# Example 2:
	# Input: String="abccde"
	# Output: 3
	# Explanation: Longest substrings without any repeating characters are "abc" & "cde".
	
	# Approach: 
	
	# We can use a Map to remember the last index of each character we have processed. 
	# Whenever we get a repeating character we will shrink our sliding window to ensure that we 
	# always have distinct characters in the sliding window.
	# i.e windowStart to windowEnd will always have unique characters.
	# So, whenever I get any character which is already processed, I'll make my windowStart as 
	# the last index of the character + 1.


def findLength(s):

	if(s == None or len(s) == 0):
		return -1

	windowStart = 0
	maxLength = 0
	dictionary = {}

	for windowEnd in range(len(s)):
		rightCharacter = s[windowEnd]

		if rightCharacter in dictionary:
			windowStart = max(windowStart, dictionary[rightCharacter] + 1)

		dictionary[rightCharacter] = windowEnd
		maxLength = max(maxLength, windowEnd - windowStart + 1)
			
	return maxLength

def main():
	s = "aabccbb"
	length = findLength(s)
	print(length)

main()