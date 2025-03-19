from codage.file import read_byte_file
from codage import get_binaries ,get_binaries_str

encoded = read_byte_file('assets/compressed.bin')
binary_code = get_binaries_str(encoded)
binary_list = get_binaries(encoded)
print(binary_code)