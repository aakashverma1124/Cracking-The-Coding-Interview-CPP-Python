# @author
# Aakash Verma

# Problem: Given an array of positive numbers and a positive number ‘S’, 
# find the length of the smallest contiguous subarray whose sum is greater than 
# or equal to ‘S’. Return 0, if no such subarray exists.

# Sliding Window Pattern

# Output: 2


import math

def smallestSubarrayWithGivenSum(arr, givenSum):
	minLength = math.inf
	windowSum = 0
	windowStart = 0

	for windowEnd in range(len(arr)):
		windowSum += arr[windowEnd]
		while windowSum >= givenSum:
			minLength = min(minLength, windowEnd - windowStart + 1)
			windowSum -= arr[windowStart]
			windowStart += 1

	if minLength == math.inf:
		return 0

	return minLength

def main():
	length = smallestSubarrayWithGivenSum([2, 1, 5, 2, 3, 2], 7)
	print(length)

main()