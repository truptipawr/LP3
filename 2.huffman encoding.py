import heapq

# Node structure for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison for priority queue
    def __lt__(self, other):
        return self.freq < other.freq


# Function to generate Huffman Codes recursively
def generate_codes(root, code, codes):
    if root is None:
        return
    if root.char is not None:  # Leaf node
        codes[root.char] = code
    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)


# Huffman Encoding Function
def huffman_encoding(text):
    # Step 1: Calculate frequency of each character
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # Step 2: Create a priority queue (min-heap)
    heap = [Node(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)

    # Step 3: Build Huffman Tree (Greedy Approach)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Step 4: Generate Huffman Codes
    root = heap[0]
    codes = {}
    generate_codes(root, "", codes)

    # Step 5: Encode the text
    encoded_text = "".join(codes[ch] for ch in text)
    return codes, encoded_text


# -------------------------------
# Main Program
# -------------------------------
text = input("Enter text to encode: ")

codes, encoded_text = huffman_encoding(text)

print("\nCharacter | Frequency | Huffman Code")
print("------------------------------------")
for ch, code in codes.items():
    print(f"   {ch}      |    {text.count(ch)}       |    {code}")

print("\nEncoded Huffman Text:", encoded_text)
