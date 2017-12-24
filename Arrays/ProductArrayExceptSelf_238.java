// Two pass. O(n) time complexity. O(1) extra space. 3ms runtime
class Solution {
    public int[] productExceptSelf(int[] nums) {
        if (nums == null || nums.length== 0) return new int[0];
        int[] res = new int[nums.length];
        res[0] = 1;
        // 1st pass, getting products of all numbers to i-th number's left
        for (int i = 1; i < nums.length; i++){
            res[i] = res[i-1] * nums[i-1];
        }
        // 2nd pass, getting products of all numbers to i-th number's right
        int right = nums[nums.length-1];
        for (int j = nums.length - 2; j >= 0; j--){
            res[j] *= right;
            right *= nums[j];
        }
        return res;
    }
}
