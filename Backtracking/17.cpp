#include <vector>
#include <string>
#include <map>

class Solution {
public:
    std::vector<std::string> letterCombinations(std::string digits) {
		std::vector<std::string> res;
		if (digits.empty()) return res;

		this->backtrack("", digits, res);
		return res;
    }

	void backtrack(std::string combination, std::string next_digits, std::vector<std::string>& result)
	{
		if (next_digits.empty()) result.push_back(combination);
		else
		{
			// Convert char into int
			std::string letters = m_sol[next_digits[0] - '0'];
			for (char letter : letters)
				backtrack(combination + letter, next_digits.substr(1), result);
		}
	}


private:
    std::map<int, std::string> m_sol = {
		{2, "abc"},
		{3, "def"},
		{4, "ghi"},
		{5, "jkl"},
		{6, "mno"},
		{7, "pqrs"},
		{8, "tuv"},
		{9, "wxyz"}
	};
};