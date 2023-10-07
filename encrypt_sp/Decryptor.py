from encrypt_sp.helper.rot_13 import rot13


class Decryptor:
    def __init__(self, target_file, output=None):
        with open(target_file) as file:
            info = file.read()
        encrypted_info = rot13(info, idx=-13)

        with open(target_file if not output else output, "w") as file:
            file.write(encrypted_info)
