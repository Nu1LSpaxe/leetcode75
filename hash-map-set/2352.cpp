#include <bits/stdc++.h>

class Solution
{
public:
    int equalPairs(std::vector<std::vector<int>> &grid)
    {
        // Method 1: Iterate each row(column), check if matches with column(row) (through iteration).
        // Optimized: Using map stores appeared row, calculate the sum by checking columns in map.

        int pair{0};
        std::map<std::vector<int>, int> seen;

        // Initialize map based on row
        for (auto row : grid)
            seen[row]++;

        for (size_t i{0}; i < grid.size(); ++i)
        {
            std::vector<int> curr {};

            // Get column
            for (size_t j{0}; j < grid.size(); ++j)
            {
                curr.push_back(grid[j][i]);
            }

            pair += seen[curr];
        }
        return pair;
    }
};

int main()
{
    Solution sol;

    std::vector<std::vector<int>> grid{
        {3, 1, 2, 2},
        {1, 4, 4, 5},
        {2, 4, 2, 2},
        {2, 4, 2, 2}};

    std::cout << sol.equalPairs(grid) << std::endl;
}