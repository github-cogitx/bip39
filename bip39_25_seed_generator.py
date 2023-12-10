from mnemonic import Mnemonic
import binascii

def generate_bip39_seed_with_passphrase(num_words=24, passphrase=''):
if num_words not in [12, 15, 18, 21, 24]:
    raise ValueError('Number of words should be one of the following: 12, 15, 18, 21, 24')

mnemo = Mnemonic('english')
words = mnemo.generate(strength=num_words * 32 // 3)

# Adding your chosen passphrase
seed = mnemo.to_seed(words, passphrase=passphrase)

# Convert seed to hexadecimal string for Python 2
hex_seed = binascii.hexlify(seed)
return words, hex_seed

# Example usage with your passphrase 'sillysalad'
seed_phrase, hex_seed = generate_bip39_seed_with_passphrase(24, 'sillysalad')
print('BIP39 Mnemonic (24 words):', seed_phrase)
print('Seed with Passphrase:', hex_seed)
