from codage.file import readByteFile

encoded = readByteFile('assets/compressed.bin')
print(bytes(encoded))
binary_code = ''.join(f'{byte:08b}' for byte in encoded)
print(binary_code)