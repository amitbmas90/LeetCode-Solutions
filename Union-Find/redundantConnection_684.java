// Given a list of lists representing an UNIDRECTED graph.
// Return an edge without which the graph has no cycle.
class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int[] groups = new int[2001];
        int[] ranks = new int[2001];
        Arrays.fill(groups, -1);
        for (int[] edge: edges)
        {
            int x = edge[0], y = edge[1];
            if (findGroup(x, groups) == findGroup(y, groups))
            {
                return edge;
            }
            else
            {
                int g1 = findGroup(x, groups), g2 = findGroup(y, groups);
                if (ranks[g1] > ranks[g2]){
                    groups[g2] = g1;
                }
                else if(ranks[g1] < ranks[g2]){
                    groups[g1] = g2;
                }
                else{
                    groups[g1] = g2;
                    ranks[g2] += 1;
                }
            }
        }        
        return new int[2];
    }
    
    private int findGroup(int node, int[] groups){
        if (groups[node] == -1) return node;
        return findGroup(groups[node], groups);
    }
}
