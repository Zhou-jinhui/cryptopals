
# Fixed XOR

# Write a function that takes two equal-length buffers and produces 
# their XOR combination.

# If your function works properly, then when you feed it the string:

# 1c0111001f010100061a024b53535009181c

# ... after hex decoding, and when XOR'd against:

# 686974207468652062756c6c277320657965

# ... should produce:

# 746865206b696420646f6e277420706c6179




first_hex = "1c0111001f010100061a024b53535009181c"
second_hex = "686974207468652062756c6c277320657965"

def two_hex_XOR(first_hex, second_hex):
	f_num = int(first_hex, base=16)
	s_num = int(second_hex, base=16)
	result_of_XOR = f_num ^ s_num
	return str(hex(result_of_XOR))[2:]

print(two_hex_XOR(first_hex, second_hex))