from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto import Random

AES_KEY_SIZE = 32


def import_rsa_key(file_name: str):
    file = open(file_name, "rb")
    content = file.read()
    key = RSA.importKey(content)
    file.close()
    return key


def import_rsa_pub(key_name: str):
    return import_rsa_key(key_name + "_rsa.pub")


def import_rsa_private(key_name: str):
    return import_rsa_key(key_name + "_rsa")


def save_rsa(key_name: str, key) -> None:
    public_key = key.publickey()

    public_file = open(key_name + "_rsa.pub", "wb")
    public_file.write(public_key.exportKey("PEM"))

    private_file = open(key_name + '_rsa', "wb")
    private_file.write(key.exportKey("PEM"))

    public_file.close()
    private_file.close()


def save_aes(key_name: str, aes_key, iv, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(aes_key + iv)

    file = open(key_name + ".aes", "wb")
    file.write(encrypted)
    file.close()


def load_aes(key_name: str, rsa_private):
    rsa_cipher = PKCS1_OAEP.new(rsa_private)
    file = open(key_name + ".aes", "rb")
    content = file.read()
    decrypted = rsa_cipher.decrypt(content)
    return list((decrypted[:AES_KEY_SIZE], decrypted[-AES.block_size:]))


def generate_aes():
    aes_key = Random.new().read(AES_KEY_SIZE)
    iv = Random.new().read(AES.block_size)

    return list((aes_key, iv))
