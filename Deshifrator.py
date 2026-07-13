import base64

def Decrypt(cipher, key, depth):

    encrypted = base64.b64decode(cipher)

    bin_key = [
        format(b, '08b')
        for b in key.encode("utf-8")
    ]

    result = []

    for symbol in encrypted:

        byte = format(symbol, '08b')

        for round_num in range(depth):

            current_key = bin_key[round_num % len(bin_key)]

            byte = ''.join(
                str(int(a) ^ int(b))
                for a, b in zip(byte, current_key)
            )

        result.append(int(byte, 2))

    return bytes(result).decode("utf-8")