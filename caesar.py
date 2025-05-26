def caesar_decrypt(plain, shift):
    decrypted = []
    for x in plain:
        if 'A' <= x <= 'Z':
            decrypted.append(chr((ord(x) - ord('A') - shift) % 26 + ord('A')))
        elif 'a' <= x <= 'z':
            decrypted.append(chr((ord(x) - ord('a') - shift) % 26 + ord('a')))
        else:
            decrypted.append(x) # 記号や数字はそのまま
    return ''.join(decrypted)

cipher = input("cipher:")
for s in range(26):
    print(f"Shift {s:2d}: {caesar_decrypt(cipher, s)}")
