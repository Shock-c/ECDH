import tinyec
import secrets

from tinyec import registry


def compress(pubKey):
    print("compress",hex(pubKey.x),hex(pubKey.y % 2)[2:])
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

curve = registry.get_curve('secp224r1') #选择曲线

print('curve.field.n = ', curve.field.n)
print('curve.g', curve.g)
alicePrivKey = secrets.randbelow(269599466671506397946670150870196259404578077144243917216827223680611111111111111111)
print('private key:', alicePrivKey)
alicePubKey = alicePrivKey * curve.g
print("Alice public key:", compress(alicePubKey))

bobPrivKey = secrets.randbelow(curve.field.n)
bobPubKey = bobPrivKey * curve.g
print("Bob public key:", compress(bobPubKey))

print("Now exchange the public keys (e.g. through Internet)")

aliceSharedKey = alicePrivKey * bobPubKey
print("Alice shared key:", compress(aliceSharedKey))

bobSharedKey = bobPrivKey * alicePubKey
print("Bob shared key:", compress(bobSharedKey))

print("Equal shared keys:", aliceSharedKey == bobSharedKey)