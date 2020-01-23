
def hasCycle(head):
    fast_runner = head
    slow_runner = head


    # define by the fast runner
    while fast_runner != None and fast_runner.next != None:
        fast_runner = fast_runner.next.next
        slow_runner = slow_runner.next

        if slow_runner is fast_runner:
            return True

    return False