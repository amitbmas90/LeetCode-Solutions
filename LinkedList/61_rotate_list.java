/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || k == 0) return head;
        // find length of the linked-list
        int len = 0;
        ListNode p = head;
        while (p != null){
            len += 1;
            p = p.next;
        }
        // calculate real k
        k = k % len;
        if (k == 0) return head;
        // connect rear section to front section
        k = len - k;
        ListNode p1 = head, p2 = p1, q1 = null, q2 = null;

        int count = 1;
        while (count < k){
            p2 = p2.next;
            count += 1;
        }

        q1 = p2.next;
        p2.next = null;
        q2 = q1;

        while (q2.next != null){
            q2 = q2.next;
        }
        q2.next = p1;
        return q1;
    }
}