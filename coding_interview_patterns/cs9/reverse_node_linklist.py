"""
Write a function that reverses the nodes of a linked list without allocating or freeing any
memory.



"""
# singly
def reverse_linklist(head):
    if not head.next:
        return head

    l = reverse_linklist(head.next)
    head.head.next = head
    head.next = None
    return l

# doubly
def reverse_linklist(head):
    temp = head.next
    head.next = head.previous
    head.previous = temp
    if not temp:
        return head

    reverse_linklist(temp)
