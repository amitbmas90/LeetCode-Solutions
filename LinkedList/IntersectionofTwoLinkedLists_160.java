/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        ListNode tailA = headA, tailB = headB;
        int lenA = 1, lenB = 1;
        while (tailA.next != null){
            lenA++;
            tailA = tailA.next;
        }
        while (tailB.next != null){
            lenB++;
            tailB = tailB.next;
        }
        if (tailA != tailB) return null;    // no intersection
        int diff = Math.abs(lenA-lenB);
        if (lenA > lenB){
            while (diff > 0){
                headA = headA.next;
                diff--;
            }
        }
        else if(lenA < lenB){
            while (diff > 0){
                headB = headB.next;
                diff--;
            }
        }
        
        while (headA != headB){
            headA = headA.next;
            headB = headB.next;
        }
        return headA;
    }
}
