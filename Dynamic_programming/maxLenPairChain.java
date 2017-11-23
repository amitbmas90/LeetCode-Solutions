// 646. Maximum Length of Pair Chain
class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b) -> (a[1] - b[1]));
        // Longest chain ending at each pair. Similar to longest increasing subsequence
        int[] dp = new int[pairs.length];           
        Arrays.fill(dp, 1); 
        for (int i = 1; i < pairs.length; i++){
            for (int j = 0; j < i; j++){
                dp[i] = pairs[i][0] > pairs[j][1] ? dp[j] + 1 : dp[j]
            }
        }
        
        return dp[pairs.length-1];
    }
}
