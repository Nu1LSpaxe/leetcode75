#include <iostream>
#include <vector>
#include <algorithm>

int compare(int x, int y) { return x > y;  }

class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end(), compare);
        return nums[k - 1];
    }
};