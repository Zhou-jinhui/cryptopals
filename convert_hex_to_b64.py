# Convert hex to base64

# The string:

# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

# Should produce:

# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

# So go ahead and make that happen. You'll need to use this code for the rest of the exercises. 


from base64 import b64encode

hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

hex_data = bytes.fromhex(hex_str)
print(hex_data.decode())
base64 = b64encode(hex_data)
print(base64.decode())