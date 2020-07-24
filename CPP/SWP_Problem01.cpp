/*
*
*	@author
*	Aakash Verma
*	
*	Problem: Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
*	Sliding Window Pattern
*
*	Output: 2.2 2.8 2.4 3.6 2.8
*	Time Complexity: O(N)
*
*/

#include <iostream>
#include <vector>
using namespace std;

class SWP_Problem01 {
	public:
		static vector<double> findAveragesOfSubarrays(const vector<int>& arr, int k) {
			vector<double> result(arr.size() - k + 1);
			double windowSum = 0;
			int windowStart = 0;
			for(int windowEnd = 0; windowEnd < arr.size(); windowEnd++) {
				windowSum += arr[windowEnd];
				if(windowEnd >= k - 1) {
					result[windowStart] = windowSum/k;
					windowSum -= arr[windowStart];
					windowStart++;
				}
			}
			return result;
		}
};

int main(int argc, char * argv[]) {
	int k = 5;
	vector<double> result = SWP_Problem01::findAveragesOfSubarrays(vector<int>{1, 3, 2, 6, -1, 4, 1, 8, 2}, k);
	for (double r : result) {
		cout << r << " ";
	}
	cout << endl;
}