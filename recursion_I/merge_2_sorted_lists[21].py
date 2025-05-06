# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # --------------
        def mergeHelper(
            runner: Optional[ListNode], list1: Optional[ListNode], list2: Optional[ListNode]
        ) -> Optional[ListNode]:
            if list1 is None:
                runner.next = list2
                return None
            elif list2 is None:
                runner.next = list1
                return None

            if list1.val <= list2.val:
                runner.next = list1
                list1 = list1.next
            else:
                runner.next = list2
                list2 = list2.next

            runner = runner.next

            return mergeHelper(runner, list1, list2)

        # --------------
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        head = None
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        runner = head
        mergeHelper(runner, list1, list2)

        return head
