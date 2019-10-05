import argparse
from key import import_rsa_private, load_aes
from Crypto.Cipher import AES

parser = argparse.ArgumentParser(description='decode file(s)')
parser.add_argument('-k', type=str, help='filename for the key')
parser.add_argument('-ext', type=str, default="", help='replacement for the .enc extension')
parser.add_argument('-f', action='append', help='file name(s) without .enc extension')

args = parser.parse_args()

rsa_private = import_rsa_private(args.k)
aes_key, iv = load_aes(args.k, rsa_private)
cipher = AES.new(aes_key, AES.MODE_CFB, iv)

for file in args.f:
    cipher_text = open(file, "rb").read()
    message = cipher.decrypt(cipher_text)
    save_file = open(file.replace(".enc", args.ext), "wb")
    save_file.write(message)
    save_file.close()

