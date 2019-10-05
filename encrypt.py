import argparse
from Crypto.Cipher import AES
from key import import_rsa_pub, generate_aes, save_aes

parser = argparse.ArgumentParser(description='encode file(s)')
parser.add_argument('-k', type=str, help='filename for the key')
parser.add_argument('-f', action='append', help='file name(s)')

args = parser.parse_args()

pub_key = key = import_rsa_pub(args.k)
aes_key, iv = generate_aes()
cipher = AES.new(aes_key, AES.MODE_CFB, iv)

save_aes(args.k, aes_key, iv, pub_key)

for file in args.f:
    text = open(file, "rb").read()
    encrypted = cipher.encrypt(text)
    open(file + '.enc', 'wb').write(encrypted)


