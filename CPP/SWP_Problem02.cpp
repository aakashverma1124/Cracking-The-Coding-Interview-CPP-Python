/*
*
*	@author
*	Aakash Verma
*	
*	Problem: Given an array of positive numbers and a positive number ‘k’, 
*			 find the maximum sum of any contiguous subarray of size ‘k’.
*	
*	Sliding Window Pattern
*
*	Output: 9
*
*/

#include <iostream>
#include <vector>
using namespace std;

class SWP_Problem02 {
	public:
		static int contiguousSubArrayOfSizeKWithMaxSum(const vector<int>& arr, int k) {
			int maxSum = 0;
			int windowSum = 0;
			int windowStart = 0;
			for(int windowEnd = 0; windowEnd < arr.size(); windowEnd++) {
				windowSum += arr[windowEnd];
				if(windowEnd >= k - 1) {
					maxSum = max(maxSum, windowSum);
					windowSum -= arr[windowStart];
					windowStart++;
				}
			}
			return maxSum;
		}
};

int main(int argc, char * argv[]) {
	int k = 3;
	int sum = SWP_Problem02::contiguousSubArrayOfSizeKWithMaxSum(vector<int>{2, 1, 5, 1, 3, 2}, k);
	cout << sum << endl;
}