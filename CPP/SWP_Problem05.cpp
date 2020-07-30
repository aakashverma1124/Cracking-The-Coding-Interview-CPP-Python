/*	
	@author Aakash.Verma
	
	Problem: Given a string, find the length of the longest substring which has no repeating characters.
	
	Example 1:
	Input: String="aabccbb"
	Output: 3
	Explanation: The longest substring without any repeating characters is "abc".	
	
	Example 2:
	Input: String="abccde"
	Output: 3
	Explanation: Longest substrings without any repeating characters are "abc" & "cde".
	
	Approach: 
	
	We can use a Map to remember the last index of each character we have processed. 
	Whenever we get a repeating character we will shrink our sliding window to ensure that we 
	always have distinct characters in the sliding window.
	i.e windowStart to windowEnd will always have unique characters.
	So, whenever I get any character which is already processed, I'll make my windowStart as 
	the last index of the character + 1.
*/


#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class SWP_Problem05 {
	public:
		static int findLength(const string &s) {
			if(s.length() == 0) {
				return -1;
			}

			int windowStart = 0;
			int maxLength = 0;
			unordered_map<char, int> map;

			for(int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
				char rightCharacter = s[windowEnd];
				
				if(map.find(rightCharacter) != map.end()) {
					windowStart = max(windowStart, map[rightCharacter] + 1);
				}

				map[rightCharacter] = windowEnd;
				maxLength = max(maxLength, windowEnd - windowStart + 1);
			}
			return maxLength;
		}
};

int main(int argc, char *argv[]) {
	int length = SWP_Problem05::findLength("aabccbb");
	cout << length << endl;
}