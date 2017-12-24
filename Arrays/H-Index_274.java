// Binary-search based method. h-Index Search range is [0, maxCitation].
// Time complexity O(Nlog(M)), where M is the maximum citation of all papers.
class Solution {
    public int hIndex(int[] citations) {
        if (citations == null || citations.length == 0) return 0;
        int max = Integer.MIN_VALUE;
        for (int citation: citations){
            max = Math.max(max, citation);
        }
        int start = 0, end = max;
        while (start <= end){
            int mid = start + (end - start) / 2;
            if (atleastX(citations, mid)){
                start = mid + 1;
            }
            else
            {
                end = mid - 1;
            }
        }
        return end;
    }
    
    public boolean atleastX(int[] citations, int x){
        int count = 0;
        for (int citation: citations){
            if (citation >= x) count++;
        }
        return count >= x;
    }
}
