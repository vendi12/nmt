'''
svakulenko
3 Jul 2018

Generate vocabulary
'''

# generate user vocabulary
words = []

# load patterns
with open('dev.user') as f:
    patterns = f.readlines()
    words.extend([word for pattern in patterns for word in pattern.split()])
    words = set(words)

# store vocabulary
with open('vocab.user', 'wb') as f:
    f.writelines('<unk>\n<s>\n</s>\n' + '\n'.join(words))
