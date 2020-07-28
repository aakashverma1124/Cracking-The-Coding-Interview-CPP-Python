	
	# @author Aakash.Verma
	# Problem: Given a string, find the length of the longest substring in it with no more than 
	# K distinct characters.

	# Example 1:
	# Input: string = "araaci", k = 2
	# Output: 4
	# Explanation: The longest substring with no more than '2' distinct characters is "araa".
	
	# Example 2:
	# Input: string = "cbbebi", k = 3
	# Ouput: 5
	# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
	
	# Approach: 
	
	# We've taken a map to keep count of distinct character that we'll encounter during the process.
	# Until the size of map becomes greater than k, we'll keep adding the characters into map with their
	# frequency & we'll keep finding the maxLength.
	# As soon as size becomes greater than k, we will try to shrink the window from the beginning 
	# if the count of distinct characters in the map is larger than ‘k’. We will shrink the window until 
	# we have no more than ‘k’ distinct characters in the map. This is needed as we intend to find the longest window.
	# While shrinking, we’ll decrement the frequency of the character going out of the window and 
	# remove it from the map if its frequency becomes zero.
	# At the end of each step, we’ll check if the current window length is the longest so far, 
	# and if so, remember its length.


def findLength(s, k):

	if(s == None or len(s) < k or len(s) == 0):
		return -1

	windowStart = 0
	maxLength = 0
	dictionary = {}

	for windowEnd in range(len(s)):
		rightCharacter = s[windowEnd]
		if rightCharacter not in dictionary:
			dictionary[rightCharacter] = 0
		dictionary[rightCharacter] += 1

		while len(dictionary) > k:
			leftCharacter = s[windowStart]
			dictionary[leftCharacter] -= 1
			if dictionary[leftCharacter] == 0:
				del dictionary[leftCharacter]
			windowStart += 1

		maxLength = max(maxLength, windowEnd - windowStart + 1)
			
	return maxLength

def main():
	s = "araaci"
	k = 2
	length = findLength(s, k)
	print(length)

main()