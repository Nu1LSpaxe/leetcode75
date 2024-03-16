#include <iostream>
#include <vector>
#include <stack>

class Solution {
public:
    std::vector<int> asteroidCollision(std::vector<int>& asteroids)
    {
        std::vector<int> result;

        for (int curr : asteroids)
        {
            bool canPush = true;

            if (curr > 0)
                result.push_back(curr);
            else // curr < 0
            {
                // Check collision with each previous 
                while (!result.empty())
                {
                    int prev = result.back();
                    if (prev < 0)
                        break;
                    else if (curr + prev == 0)
                    {
                        canPush = false;
                        result.pop_back();
                        break;
                    }
                    else if (curr + prev < 0)
                    {
                        result.pop_back();
                    }
                    else
                    {
                        canPush = false;
                        break;
                    }
                }
                
                if (canPush)
                    result.push_back(curr);
            }
        }
        return result;
    }
};