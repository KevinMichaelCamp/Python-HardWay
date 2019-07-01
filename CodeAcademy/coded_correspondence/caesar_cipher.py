message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
offset = 10

def caesar_cipher(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_message = ""
    for char in message:
        if char in alphabet:
            char_pos = alphabet.find(char) + offset
            if char_pos > 25:
                char_pos = char_pos % 26
                new_char = alphabet[char_pos]
            else:
                new_char = alphabet[char_pos]
            decoded_message = decoded_message + new_char
        else:
            decoded_message = decoded_message + char
    return decoded_message

print(caesar_cipher(message, offset))
