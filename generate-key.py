import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import argparse

parser = argparse.ArgumentParser(description='generate private/public key pair.')
parser.add_argument('-n', type=str, help='filename for the key')

args = parser.parse_args()

random_generator = Random.new().read

private_key = RSA.generate(2048, random_generator)
public_key = private_key.publickey()

public_file = open(args.n + ".pub", "w")
private_file = open(args.n, "w")


print("{}".format(public_key.exportKey()), file=public_file)
print("{}".format(private_key.exportKey()), file=private_file)

public_file.close()
private_file.close()
