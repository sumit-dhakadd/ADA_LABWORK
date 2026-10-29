
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoder:
    def __init__(self):
        self.root = None
        self.codes = {}

    def build_tree(self, frequencies):
        heap = [Node(ch, freq) for ch, freq in frequencies.items()]
        heapq.heapify(heap)

        if len(heap) == 0:
            return None

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            new_node = Node(None, first.freq + second.freq)
            new_node.left = first
            new_node.right = second

            heapq.heappush(heap, new_node)

        self.root = heap[0]
        return self.root

    def generate_codes(self):
        self.codes = {}

        def create_code(node, path):
            if node is None:
                return

            if node.char is not None:
                self.codes[node.char] = path if path else "0"
                return

            create_code(node.left, path + "0")
            create_code(node.right, path + "1")

        create_code(self.root, "")
        return self.codes


frequencies = {
    'a': 5,
    'b': 9,
    'c': 12,
    'd': 13,
    'e': 16,
    'f': 45
}

coder = HuffmanCoder()
coder.build_tree(frequencies)

print("Huffman Codes:")
print(coder.generate_codes())
