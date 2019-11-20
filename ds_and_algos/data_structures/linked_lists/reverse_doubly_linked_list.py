# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev

def reverse(head):
    temp = head.next
    head.next = head.prev
    head.prev = temp
    if temp == None:
        return head
    return reverse(temp)


