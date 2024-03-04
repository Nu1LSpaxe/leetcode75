#include <bits/stdc++.h>

class Solution {
public:
    std::string _removeStars(std::string s) {
        std::string answer;
        std::stack<char> stack;

        // Initialize stack
        for (size_t i{0}; i < s.size(); ++i)
            stack.push(s[i]);

        int remain {0};

        while (!stack.empty())
        {
            if (stack.top() == '*')
            {
                remain++;
                stack.pop();
            }
            else if (remain > 0)
            {
                remain--;
                stack.pop();
            }
            else
            {
                answer.push_back(stack.top());
                stack.pop();
            }
        }
        std::reverse(answer.begin(), answer.end());
        return answer;
    }

    std::string removeStars(std::string s)
    {
        std::string answer {""};

        std::stack<char> stack;
        for (auto ele : s)
        {
            if (ele == '*')
                stack.pop();
            else
                stack.push(ele);
        }

        while (!stack.empty())
        {
            answer.push_back(stack.top());
            stack.pop();
        }

        std::reverse(answer.begin(), answer.end());
        return answer;
    }
};

int main()
{
    Solution sol;
    std::cout << sol.removeStars("leet**cod*e");
}