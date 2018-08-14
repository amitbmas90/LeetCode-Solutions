class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b) -> (a[1] - b[1]));
        int cur = Integer.MIN_VALUE, res = 0;

        for (int[] pair: pairs){
            if (pair[0] > cur){
                res += 1;
                cur = pair[1];
            }
        }
        return res;
    }
}