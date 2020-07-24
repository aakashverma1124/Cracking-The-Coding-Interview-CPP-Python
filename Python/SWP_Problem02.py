

# @author
# Aakash Verma

# Problem: Given an array of positive numbers and a positive number ‘k’, 
# 		 find the maximum sum of any contiguous subarray of size ‘k’.

# Sliding Window Pattern

# Output: 9




def contiguousSubArrayOfSizeKWithMaxSum(arr, k):
	maxSum = 0
	windowSum = 0
	windowStart = 0

	for windowEnd in range(len(arr)):
		windowSum += arr[windowEnd]
		if windowEnd >= k - 1:
			maxSum = max(maxSum, windowSum)
			windowSum -= arr[windowStart]
			windowStart += 1

	return maxSum

def main():
	arr = [2, 1, 5, 1, 3, 2]
	k = 3
	ans = contiguousSubArrayOfSizeKWithMaxSum(arr, k)
	print(ans)

main()