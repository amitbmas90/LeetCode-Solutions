# The key point is the non-zero values of A such as A[i][j] updates column values in B[j][k].
# The reduction of computation is #zeros elements in A * columns(B)
class Solution {
    public int[][] multiply(int[][] A, int[][] B) {
        int p = A.length, n = B[0].length;
        int[][] res = new int[p][n];
        int m = A[0].length;
        
        for (int i = 0; i < p; i++){
            for (int j = 0; j < m; j++){
                if (A[i][j] != 0){
                    for (int k = 0; k < n; k++){
                        res[i][k] += A[i][j] * B[j][k];
                    }
                }
            }
        }
        return res;
    }
}
