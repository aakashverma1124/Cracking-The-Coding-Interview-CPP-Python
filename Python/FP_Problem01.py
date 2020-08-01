
	# @author Aakash.Verma
	
	# Problem: Given an array of sorted numbers and a target sum, find a pair in the array whose 
	# sum is equal to the given target.
	# Write a function to return the indices of the two numbers (i.e. the pair) such that 
	# they add up to the given target.
	
	# Example 1:
	# Input: [1, 2, 3, 4, 6], target=6
	# Output: [1, 3]
	# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
	
	# Example 2:
	# Input: [2, 5, 9, 11], target=11
	# Output: [0, 2]
	# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
	
	# Approach: 
	
	# We'll use two pointers, left and right.
	# The left pointer will point to 0th index and right pointer will point to the last index.
	# We do sum = arr[left] + arr[right], if sum is greater than target sum, we'll decrement right.
	# If sum is less than target sum then we'll increment left.
	# We'll keep on doing this, till left < right.
	# If left becomes greater than right and we do not found any pair which gives us as target sum.
	# Once we find the pair, we'll return the indices as an array.
	# Otherwise, we return [-1. -1].
	# Time Complexity:
	# The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.
	# Space Complexity:
	# The space complexity will also be O(N), as, in the worst case, we will be pushing ‘N’ numbers in the HashTable.


def search(arr, targetSum):
	left = 0
	right = len(arr) - 1

	while left < right:
		currentSum = arr[left] + arr[right]
		if(currentSum == targetSum):
			return [left, right]

		if targetSum > currentSum:
			left += 1
		else:
			right -= 1

	return [-1, -1]

def main():
	ans = search([1, 2, 3, 4, 6], 6)
	print(ans)

main()