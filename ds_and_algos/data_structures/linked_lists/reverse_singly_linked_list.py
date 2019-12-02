import unittest

# attempt1
def reverse(head_of_list):
    # Reverse the linked list in place
    temp = head_of_list
    arr = []
    while head_of_list != None:
        arr.append(head_of_list.value)
        head_of_list = head_of_list.next

    head_of_list = temp
    temp1 = head_of_list
    if len(arr) >= 1:
        rev = reversed(arr)
        for e in rev:
            if head_of_list != None:
                head_of_list.value = e
                head_of_list = head_of_list.next

    return temp1

# attempt2
class LinkedListNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head_of_list):
    head = LinkedListNode('*')
    head.next = None
    reverse_list(head_of_list, head)

    return head.next


def reverse_list(head_of_list, head):
    if head_of_list and head_of_list.next == None:
        head.next = head_of_list
        return head_of_list

    if head_of_list:
        reverse_list(head_of_list.next, head)
        temp = head_of_list
        n_n_obj = head_of_list.next.next

        head_of_list = head_of_list.next
        head_of_list.next = temp
        head_of_list.next.next = n_n_obj



# attempt3
def reverse(head_of_list):
    current_node = head_of_list
    previous_node = None
    next_node = None

    # Until we have 'fallen off' the end of the list
    while current_node:
        # Copy a pointer to the next element
        # before we overwrite current_node.next
        next_node = current_node.next

        # Reverse the 'next' pointer
        current_node.next = previous_node

        # Step forward in the list
        previous_node = current_node
        current_node = next_node

    return previous_node


# Tests

class Test(unittest.TestCase):
    class LinkedListNode(object):
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def test_short_linked_list(self):
        second = Test.LinkedListNode(2)
        first = Test.LinkedListNode(1, second)

        result = reverse(first)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [2, 1]
        self.assertEqual(actual, expected)

    def test_long_linked_list(self):
        sixth = Test.LinkedListNode(6)
        fifth = Test.LinkedListNode(5, sixth)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)

        result = reverse(first)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [6, 5, 4, 3, 2, 1]
        self.assertEqual(actual, expected)

    def test_one_element_linked_list(self):
        first = Test.LinkedListNode(1)

        result = reverse(first)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [1]
        self.assertEqual(actual, expected)

    def test_empty_linked_list(self):
        result = reverse(None)
        self.assertIsNone(result)


unittest.main(verbosity=2)