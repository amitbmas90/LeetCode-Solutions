class Solution {
    public int minCost(int[][] costs) {
        if (costs == null || costs.length == 0) return 0;
        int[] prev = null, cur = null;
        for (int[] cost: costs){
            cur = new int[3];
            if (prev == null){
                prev = cost;
                cur = cost;
            }
            else{
                cur[0] = cost[0] + Math.min(prev[1], prev[2]);
                cur[1] = cost[1] + Math.min(prev[0], prev[2]);
                cur[2] = cost[2] + Math.min(prev[0], prev[1]);
                prev = cur;
            }
        }
        return Math.min(cur[0], Math.min(cur[1],cur[2]));
    }
}
