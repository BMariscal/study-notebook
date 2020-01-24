
"""
both
enqueue and dequeue
items in 𝑂(log𝑛).


# Input:
# k = 3, n =  4
# arr[][] = { {1, 3, 5, 7},
#             {2, 4, 6, 8},
#             {0, 9, 10, 11}} ;
#
# Output: 0 1 2 3 4 5 6 7 8 9 10 11

# MIN HEAP!!!

"""

import heapq


def merge_k_sorted_arrays(arr):
    arr1 = []
    for l in arr:
        for item in l:
            heapq.heappush(arr1, item)

    answer = []
    for i in range(len(arr1)):
        answer.append(heapq.heappop(arr1))
    return answer


arr = [
    [2, 6, 12, 34],
    [1, 9, 20, 1000],
    [23, 34, 90, 2000]
]
print('Merged Array is:')
answer = merge_k_sorted_arrays(arr)
print(answer)


# My Min-Heap implementation
# ----------------------------------

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


parent_list = []
aa = ListNode(1)
ab = ListNode(4)
ac = ListNode(5)
aa.next = ab
ab.next = ac
parent_list.append(aa)

ba = ListNode(3)
bb = ListNode(7)
bc = ListNode(9)
ba.next = bb
bb.next = bc
parent_list.append(ba)

ca = ListNode(2)
cb = ListNode(6)
ca.next = cb
parent_list.append(ca)


class MinHeap(object):
    def __init__(self):
        self.heap = [0]

    def heappush(self, x):
        self.heap.append(x)
        self.bubbleup(len(self.heap) - 1)

    def heappop(self):
        res = self.heap[1]
        self.__swap(1, -1)
        self.heap.pop()
        self.bubbledown(1)
        return res

    def bubbleup(self, idx):

        while idx > 1:
            parent = idx // 2
            if self.heap[parent][0] > self.heap[idx][0]:
                self.__swap(parent, idx)
            idx = parent

    def bubbledown(self, idx):

        while 2 * idx < len(self.heap):
            left_child = 2 * idx
            right_child = 2 * idx + 1

            if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[left_child][0]:
                left_child = right_child
            if self.heap[idx][0] > self.heap[left_child][0]:
                self.__swap(left_child, idx)

            idx = left_child

    def __swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]


def mergeKLists(lists):
    h = MinHeap()
    for i in lists:
        h.heappush((i.val, i))

    new_list = ListNode(0)
    superhead = new_list
    while len(h.heap) > 1:
        node = h.heappop()[1]
        if node.next:
            h.heappush((node.next.val, node.next))

        superhead.next = node
        superhead = superhead.next

    return new_list.next


new_l = mergeKLists(parent_list)
new_arr = []
while new_l != None:
    new_arr.append(new_l.val)
    new_l = new_l.next
print(new_arr)



# heap.push # bubble up
# heap.pop # bubble down
# parent = i // 2 (bubble up)
# left_child =  2 * i (bubble down)
# right_child = 2* i + 1
