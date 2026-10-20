
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find the middle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split and reverse the second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Step 3: Merge the two halves
        list1 = head
        list2 = prev

        while list2:
            tmp1 = list1.next
            tmp2 = list2.next

            list1.next = list2
            list2.next = tmp1

            list1 = tmp1
            list2 = tmp2
