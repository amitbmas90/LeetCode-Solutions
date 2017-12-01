/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 * 8 - line Java solution, could be shorter.
 */
class Solution {
    public int minMeetingRooms(Interval[] intervals) {
        Arrays.sort(intervals, new Comparator<Interval>() {
        public int compare(Interval a, Interval b) { return a.start - b.start; }
        });
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for (Interval x: intervals){
            if (!q.isEmpty() && q.peek() <= x.start){
                q.poll();
            }
            q.offer(x.end);
        }
        return q.size();
    }
}
