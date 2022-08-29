import hashlib
import arguing
from timeit import timeit
import os

algorithms = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha224': hashlib.sha224,
    'sha256': hashlib.sha256,
    'sha384': hashlib.sha384,
    'sha512': hashlib.sha512
}

hashed = arguing.set('-h')
wordlist = arguing.set('-w')
algorithm = arguing.set('-a', default='md5')

# Error
if not os.path.exists(wordlist):
    exit('- Wordlist does not exists.')

if algorithm not in hashlib.algorithms_available or arguing.check('-sa'):
    print('~ Supported algorithms:')
    exit(',\n'.join(algorithm for algorithm in list(algorithms)))

# Main
with open(wordlist) as file:
    file = file.read().strip().split('\n')

start = timeit()
algorithm = algorithms[algorithm]
print(f'~ Starting search for "{arguing.get("-h")}" in {arguing.get("-a")}.')

for password in file:
    hash = algorithm(bytes(password, 'utf-8')).hexdigest()

    if hash == hashed:
        print('\n+ The clear text hash is: ' + password)
        exit(f'+ Hash cracked on {round(timeit() - start)}.')

print(
    f'\n- There is no match for "{hashed}" on {algorithm.__qualname__}.')
