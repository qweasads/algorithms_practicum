from collections import Counter
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes(node, current_code="", codes={}):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
    build_codes(node.left, current_code + "0", codes)
    build_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encode_string(input_string):
    frequencies = Counter(input_string)
    root = build_huffman_tree(frequencies)
    codes = build_codes(root)
    encoded_string = "".join(codes[char] for char in input_string)
    return codes, encoded_string

def huffman_decode(codes, encoded_string):
    code_to_symbol = {code: symbol for symbol, code in codes.items()}
    decoded_string, buffer = "", ""
    for bit in encoded_string:
        buffer += bit
        if buffer in code_to_symbol:
            decoded_string += code_to_symbol[buffer]
            buffer = ""
    return decoded_string

if __name__ == "__main__":
    input_string = "Errare humanum est."
    codes, encoded_string = huffman_encode_string(input_string)

    print(f"{len(codes)} {len(encoded_string)}")
    for char, code in sorted(codes.items()):
        print(f"'{char}': {code}")
    print(encoded_string)


    decoded_string = huffman_decode(codes, encoded_string)
    print(f"Decoded string: {decoded_string}")
