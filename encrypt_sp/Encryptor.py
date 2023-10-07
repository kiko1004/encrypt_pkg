import string
from encrypt_sp.helper.rot_13 import rot13

class Encryptor:
    def __init__(self, target_file, output = None):
        with open(target_file) as file:
            info = file.read()
        encrypted_info = rot13(info)

        if not output:
            with open(target_file, "w") as file:
                file.write(encrypted_info)








