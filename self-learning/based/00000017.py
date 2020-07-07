encoded_message = input()
key_number = abs(int(input()))
int_to_bytes = key_number.to_bytes(2, byteorder='little')