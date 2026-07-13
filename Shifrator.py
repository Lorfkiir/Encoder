import base64

def XOR(word, key, depth):
    binary_word_spisok = [
        format(b, '08b')
        for b in word.encode("utf-8")
    ]

    bin_key = [
        format(b, '08b')
        for b in key.encode("utf-8")
    ]

    after_xor = []

    for symbol in binary_word_spisok:
        result = symbol

        for round_num in range(depth):
            current_key = bin_key[round_num % len(bin_key)]

            result = ''.join(
                str(int(a) ^ int(b))
                for a, b in zip(result, current_key)
            )

        after_xor.append(result)

    encrypted_bytes = bytes(
        int(b, 2)
        for b in after_xor
    )

    return base64.b64encode(encrypted_bytes).decode("utf-8")