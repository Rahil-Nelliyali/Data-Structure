class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def remove(self, word):
        def _remove_helper(node, word, depth):
            if depth == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    return len(node.children) == 0
            else:
                char = word[depth]
                if char in node.children:
                    child_node = node.children[char]
                    if _remove_helper(child_node, word, depth + 1):
                        del node.children[char]
                        return len(node.children) == 0
            return False

        _remove_helper(self.root, word, 0)

    def update(self, old_word, new_word):
        if self.search(old_word):
            self.remove(old_word)
            self.insert(new_word)
            print("Word updated successfully!")
        else:
            print("Word not found.")


# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")

print(trie.search("apple")) 
print(trie.search("grape")) 
print(trie.starts_with("app"))
print(trie.starts_with("gr")) 

print("Before removal:")
print(trie.search("apple"))  

trie.remove("apple")
print("After removal:")
print(trie.search("apple"))

trie.update("banana", "grape")

print("After update:")
print(trie.search("banana"))  
print(trie.search("grape"))
