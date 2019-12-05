import collections


class LRU(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    @property
    def at_capacity(self):
        return len(self.cache) > self.capacity

    def add(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)

        if self.at_capacity:
            self.cache.popitem(last=False)

    def get(self, key):
        value = None
        try:
            value = self.cache[key]
            self.cache.move_to_end(key)
        except KeyError:
            return -1

        return value


class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.counter = 1
        self.end_of_word = False
        self.children = []
        self.top_five = LRU(5)


class Trie(object):
    def __init__(self):
        self.root = TrieNode('*')

    def add(self, word):
        node = self.root

        for char in word:

            found_in_children = False
            for child in node.children:

                if child.char == char:
                    found_in_children = True
                    node = child
                    child.counter += 1
                    child.top_five.add(word, ["Links"])

                    break

            if not found_in_children:
                new_node = TrieNode(char)
                new_node.top_five.add(word, ["Links"])
                node.children.append(new_node)
                node = new_node

        node.end_of_word = True


    def find_prefix(self, word):
        node = self.root
        if len(node.children) == 0:
            return False, 0, None

        for char in word:
            not_found = True
            for child in node.children:

                if child.char == char:
                    not_found = False
                    node = child
                    break

            if not_found:
                return False, 0, None

        return True, node.counter, word, node.top_five.cache.keys()


t = Trie()

t.add("apple pie and baseball")
t.add("apple pie and hot dogs")
t.add("apple pie and beer")
t.add("apple pie and country music")
t.add("apple pie and twins")
t.add("apple pie and hot twins")
t.add("apple pie and hot wings")
t.add("apple pie recipes")
print(t.find_prefix("apple pie and hot"))
print(t.find_prefix("apple"))