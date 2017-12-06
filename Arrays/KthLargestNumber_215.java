// Inspired by Quicksort partitioning function
// Worst case run time O(n^2)
class Solution {
    public int findKthLargest(int[] nums, int k) {
        k = nums.length - k;
        int start = 0, end = nums.length - 1;
        int p = 0;
        while (start <= end){
            p = partition(nums, start, end);
            if (p < k){
                start = p+1;
            }
            else if(p > k){
                end = p-1;
            }
            else{
                break;
            }
        }
        return nums[p];
    }
    
    private int partition(int[] nums, int p, int r){
        int pivot = nums[r];
        int i = p - 1;
        for (int j = p; j < r; j++){
            if (nums[j] <= pivot){
                i++;
                swap(nums, i, j);
            }
        }
        swap(nums, i+1, r);
        return i+1;
    }
    
    private void swap(int[] nums, int x, int y){
        int temp = nums[x];
        nums[x] = nums[y];
        nums[y] = temp;
    }
}
