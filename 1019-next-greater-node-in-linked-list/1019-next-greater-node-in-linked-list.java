/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nextLargerNodes(ListNode head) {
        int n = 0;
        ListNode temp = head;
        
        while(temp != null) {
            temp = temp.next;
            n++;
        }
        
        int[] arr = new int[n];
        temp = head;
        ListNode temp2; 
        int index = 0;
        
        while(temp.next != null) {
            boolean isFound = false;
            temp2 = temp;
            
            while(temp2 != null) {
                if(temp.val < temp2.val) {
                    arr[index] = temp2.val;
                    isFound = true;
                    break;
                }
                
                temp2 = temp2.next;
            }
    
            if(isFound == false)
                arr[index] = 0;
            index++;
            temp = temp.next;
        }
        
        return arr;
    }
}