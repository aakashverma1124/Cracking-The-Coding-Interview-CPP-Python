/*	
	@author Aakash.Verma
	
	Problem: Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, 
	hence, we can’t count 0s, 1s, and 2s to recreate the array.
	The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three 
	different numbers that is why it is called Dutch National Flag problem.
	
	Example 1:
	Input: [1, 0, 2, 1, 0]
	Output: [0, 0, 1, 1, 2]
	
	Example 2:
	Input: [2, 2, 0, 1, 2, 0]
	Output: [0 0 1 2 2 2 ]
	
	Approach: 
	
	One of the solution is that count the number of 0s, 1s, and 2s in the array and finally start putting into the array.
	But this method of solving the problem fails as it is asking for some in-place solution.
	
	We can use a Two Pointers approach while iterating through the array. Let’s say the two pointers are called low and high which 
	are pointing to the first and the last element of the array respectively. So while iterating, we will move all 0s before low and all 2s after high
	so that in the end, all 1s will be between low and high.
*/

#include <iostream>
#include <vector>
using namespace std;

class TP_Problem02 {
	public:
		static void sort(vector<int>& arr) {
			int low = 0, high = arr.size() - 1;

			for(int i = 0; i <= high;) {
				if(arr[i] == 0) {
					swap(arr, i, low);
					i++;
					low++;
				}
				else if(arr[i] == 1) {
					i++;
				}
				else {
					swap(arr, i, high);
					high--;
				}
			}
		}
	private:
		static void swap(vector<int>& arr, int i, int j) {
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
};

int main(int argc, char * argv[]) {
	vector<int> arr = {2, 2, 0, 1, 2, 0};
	TP_Problem02::sort(arr);
	for (auto num: arr) {
		cout << num << " ";
	}
}