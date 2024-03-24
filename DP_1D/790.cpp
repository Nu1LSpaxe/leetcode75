#include <vector>

class Solution {
public:
    int numTilings(int n) 
    {
        std::vector<unsigned int> dp(n+3); dp[0] = 1; dp[1] = 2; dp[2] = 5;
        for (int i = 3; i <= n; i++)
        {
            // 1e9 + 7 mod is used to avoid overflow
			dp[i] = (2 * dp[i - 1] + dp[i - 3]) % 1000000007;
		}
        return dp[n - 1];
    }
};