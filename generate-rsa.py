from Crypto.PublicKey import RSA
from Crypto import Random
import argparse
from key import save_rsa

parser = argparse.ArgumentParser(description='generate RSA private/public key pair.')
parser.add_argument('-n', type=str, help='filename for the key')

args = parser.parse_args()

random_generator = Random.new().read

key = RSA.generate(2048, random_generator)

save_rsa(args.n, key)
