class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        if (m == 0) return 0;
        int n = grid[0].length;
        if (n == 0) return 0;
        int res = 0;
        int[] groups = new int[m * n];
        int[] ranks = new int[m * n];
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                groups[i * n + j] = i * n + j;
            }
        }
        
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (grid[i][j] == '1'){
                    grid[i][j] = '0';
                    res += 1;
                    if (i + 1 < m && grid[i+1][j] == '1'){
                        res = union(i*n+j, (i+1)*n+j, ranks, groups, res);
                    }
                    if (i - 1 >= 0 && grid[i-1][j] == '1'){
                        res = union(i*n+j, (i-1)*n+j, ranks, groups, res);
                    }
                    if (j + 1 < n && grid[i][j+1] == '1'){
                        res = union(i*n+j, i*n+j+1, ranks, groups, res);
                    }
                    if (j - 1 >= 0 && grid[i][j-1] == '1'){
                        res = union(i*n+j, i*n+j-1, ranks, groups, res);
                    }                  
                }       
            }
        }
        return res;      
    }
    
    public int find(int cur, int[] groups){
        int g = groups[cur];
        if (g == cur) return cur;
        return find(g, groups);
    }
    
    public int union(int x, int y, int[] ranks, int[] groups, int count){
        int gx = find(x, groups), gy = find(y, groups);
        if (gx == gy) return count;
        if (ranks[gx] > ranks[gy]){
            groups[gy] = groups[gx];
        }
        else if (ranks[gx] < ranks[gy]){
            groups[gx] = groups[gy];
        }
        else{
            ranks[gx]++;
            groups[gy] = groups[gx];
        }
        return --count;
    }
}
