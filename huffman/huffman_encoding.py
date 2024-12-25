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
    symbol_count = 12
    encoded_size = 60
    codes = {
        ' ': '1011',
        '.': '1110',
        'D': '1000',
        'c': '000',
        'd': '001',
        'e': '1001',
        'i': '010',
        'm': '1100',
        'n': '1010',
        'o': '1111',
        's': '011',
        'u': '1101'
    }
    encoded_string = "100011110001001101000111111011001010011000010110011010111110"
    decoded_string = huffman_decode(codes, encoded_string)
    print(f"Decoded string: {decoded_string}")
