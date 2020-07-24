
# 	@author
# 	Aakash Verma

#	Problem: Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# 	Sliding Window Pattern

#	Output: 2.2 2.8 2.4 3.6 2.8

#	Time Complexity: O(N)


def findAveragesOfSubarrays(arr, k):
	result = []
	windowSum = 0
	windowStart = 0

	for windowEnd in range(len(arr)):
		windowSum += arr[windowEnd]
		if windowEnd >= k - 1:
			result.append(windowSum/k)
			windowSum -= arr[windowStart]
			windowStart += 1

	return result

def main():
	arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
	k = 5
	ans = findAveragesOfSubarrays(arr, k)
	print(str(ans))

main()