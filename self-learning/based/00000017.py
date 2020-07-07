encoded_message = input()
key = sum(int(input()).to_bytes(2, 'little'))
# 1.
# tmp_list = []
# for i in encoded_message:
#     code_point = chr(ord(i) + key)
#     tmp_list.append(code_point)
# print("".join(tmp_list))

# 2.
print("".join([chr(ord(i) + key) for i in encoded_message]))