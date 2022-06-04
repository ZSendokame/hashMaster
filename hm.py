import hashlib
import arguing
from timeit import timeit
import os
import hashUtil

arguing.set('-h')
arguing.set('-w')
arguing.set('-a', default='md5')

# Error
if not os.path.exists(arguing.get('-w')):
    exit('- Wordlist does not exists.')

if not arguing.get('-a') in hashlib.algorithms_available or arguing.check('-sa'):
    print('~ Supported algorithms.')
    exit(',\n'.join(algorithm for algorithm in hashlib.algorithms_available))

# Main
with open(arguing.get('-w')) as file:
    file = file.read().strip().split('\n')

start = timeit()
algorithm = hashUtil.algorithms[arguing.get('-a')]
print(f'~ Starting search for "{arguing.get("-h")}" in {arguing.get("-a")}.')

for password in file:
    hash = algorithm(bytes(password, 'utf-8')).hexdigest()

    if hash == arguing.get('-h'):
        print('\n+ The clear text hash is: ' + password)
        print(f'+ Hash cracked on {round(timeit() - start)}.')
        exit(1)

print(f'\n- Sorry, there is no match for "{arguing.get("-h")}" on {arguing.get("-a")}.')