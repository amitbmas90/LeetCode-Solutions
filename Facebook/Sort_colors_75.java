// Given an array with n objects colored red, white or blue, 
// sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
// Try to do with one pass time complexity and O(1) extra space.
// Solution inspired by the fantastic idea from @DIETPEPSI

class Solution {
    public void sortColors(int[] nums) {
        int red_start, white_start, blue_start;
        red_start = white_start = blue_start = 0;
        for (; blue_start < nums.length; blue_start++){
            int v = nums[blue_start];
            nums[blue_start] = 2;
            if (v < 2){
                nums[white_start] = 1;
                white_start += 1;
            }
            if (v == 0){
                nums[red_start] = 0;
                red_start += 1;
            }
        }
    }
}
