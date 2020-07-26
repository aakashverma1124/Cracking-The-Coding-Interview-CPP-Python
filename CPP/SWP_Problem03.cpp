/*
*
*	@author
*	Aakash Verma
*	
*	Problem: Given an array of positive numbers and a positive number ‘S’, 
*	find the length of the smallest contiguous subarray whose sum is greater than 
*	or equal to ‘S’. Return 0, if no such subarray exists.
*	
*	Sliding Window Pattern
*
*	Output: 2
*
*/

#include <iostream>
#include <vector>
#include <limits>
using namespace std;

class SWP_Problem03 {
	public:
		static int smallestSubarrayWithGivenSum(const vector<int>& arr, int givenSum) {
			int minLength = numeric_limits<int>::max();
			int windowSum = 0;
			int windowStart = 0;
			for(int windowEnd = 0; windowEnd < arr.size(); windowEnd++) {
				windowSum += arr[windowEnd];
				while (windowSum >= givenSum) {
					minLength = min(minLength, windowEnd - windowStart + 1);
					windowSum -= arr[windowStart];
					windowStart++;
				}
			}

			if(minLength == numeric_limits<int>::max()) {
				return 0;
			}
			
			return minLength;
		}
};

int main(int argc, char * argv[]) {
	int length = SWP_Problem03::smallestSubarrayWithGivenSum(vector<int>{2, 1, 5, 2, 3, 2}, 7);
	cout << length << endl;
}