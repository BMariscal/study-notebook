from collections import OrderedDict


class Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = None
        self.history = None

    @property
    def at_capacity(self):
        return len(self.store) == (self.capacity)

    def store_historical_data(self, sentences, times):
        tuples_list = zip(sentences, times)
        sorted_tuples = sorted(tuples_list, key=lambda tup: (-tup[1], tup[0]))
        self.history = sorted_tuples
        self.add()

    def add(self, word=None, frequency=1):
        self.store = OrderedDict()
        found = False
        if word != None and self.history:

            index = None
            for i, item in enumerate(self.history):
                if item[0] == word:
                    index = i
                    found = True

            if found:
                print(found)
                item = self.history[index]
                del self.history[index]

                val = item[1] + frequency
                self.history.append((item[0], val))
        if not found and word != None:
            try:
                self.history.append((word, frequency))
            except AttributeError:
                self.history = []
                self.history.append((word, frequency))

        sorted_tuples = sorted(self.history, key=lambda tup: (-tup[1], tup[0]))
        i = 0
        while not self.at_capacity and i < len(sorted_tuples):
            tup = sorted_tuples[i]
            self.store[tup[0]] = tup[1]
            i += 1


class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.end_of_word = False
        self.counter = 1
        self.top_three = Cache(3)


class Trie(object):
    def __init__(self):
        self.root = TrieNode("*")

    def add(self, sentence, frequency):
        node = self.root
        for i in range(len(sentence)):
            char = sentence[i]
            not_found = True
            if char == "#":
                break
            for child in node.children:
                if char == child.char:
                    not_found = False
                    child.counter += 1
                    node = child
                    child.top_three.add(sentence[0:len(sentence) - 1], frequency)
                    break
            if not_found:
                new_node = TrieNode(char)
                new_node.top_three.add(sentence[0:len(sentence) - 1], frequency)
                node.children.append(new_node)
                node = new_node
        node.end_of_word = True

    def find_prefix(self, sentence, end=False):
        node = self.root
        if len(node.children) == 0:
            return []
        for char in sentence:
            not_found = True
            for child in node.children:
                if child.char == char:
                    not_found = False
                    node = child

        if not_found:
            return []

        if not node.end_of_word and end:
            return []

        return list(node.top_three.store.keys())


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.trie = Trie()
        self.current_sentence = ""

        for i, value in enumerate(sentences):
            val = value + "#"
            sentences[i] = val

        for index in range(len(sentences)):
            self.trie.add(sentences[index], times[index])

    def input(self, c):
        result = []
        # character # means return key/end of sentence
        if c == "#":
            active_sentence = self.current_sentence
            self.current_sentence = ""
            result = self.trie.find_prefix(active_sentence, True)
            self.trie.add(active_sentence, 1)

        else:
            self.current_sentence += c
            result = self.trie.find_prefix(self.current_sentence, False)
        return result


obj = AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
param_1 = obj.input("i")
print(param_1)
param_2 = obj.input(" ")
print(param_2)
param_3 = obj.input("love")
print(param_3)
param_4 = obj.input("#")
print(param_4)