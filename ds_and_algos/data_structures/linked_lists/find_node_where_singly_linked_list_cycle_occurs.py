
def detectCycle(head):
    if head == None: return None
    if head.next == None: return None
    visited = {}
    visited[head] = True
    first = head.next

    while first:
        if first in visited:
            return first

        visited[first] = True
        first = first.next

    return None
