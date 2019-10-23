from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for item in range(size)]

    def hash(self, key):
        key_bytes = key.encode()
        return sum(key_bytes)

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        payload = Node([key, value])
        array_index = self.compress(self.hash(key))

        list_at_array = self.array[array_index]
        for element in list_at_array:
            linked_list_key = element[0]
            if linked_list_key == key:
                element[1] = value
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for element in list_at_index:
            linked_list_key = element[0]
            if linked_list_key == key:
                return element[1]
        return None


if __name__ == "__main__":
    blossom = HashMap(len(flower_definitions))
    for flower in flower_definitions:
        blossom.assign(flower[0], flower[1])

    daisy = blossom.retrieve('daisy')
    print(daisy)
    lavander = blossom.retrieve('lavender')
    print(lavander)